#!/usr/bin/env python3
"""
Identifica y opcionalmente corrige links estilo Obsidian ([[...]]) en archivos Markdown.

Uso:
    python jntr.obsidian-links.py [directorio] [--git-modules] [--min-age N]
    python jntr.obsidian-links.py [directorio] --fix [--apply]

Parámetros:
    directorio     Directorio de inicio (default: ".")
    --git-modules  Buscar también dentro de git submodules (default: False)
    --min-age N    Solo reportar archivos modificados hace más de N minutos (default: 5)
    --fix          Mostrar reemplazos propuestos (dry-run)
    --apply        Junto con --fix, escribe los cambios en los archivos

Salida:
    Sin --fix: archivo:línea: contenido del link
    Con --fix: muestra el reemplazo propuesto o indica si no pudo resolver
"""

import argparse
import os
import re
import subprocess
import sys
import time

OBSIDIAN_LINK = re.compile(r'\[\[([^\]]+)\]\]')
INLINE_CODE = re.compile(r'`[^`]+`')


def strip_md_ext(name):
    """Quita solo la extensión .md, preservando puntos internos (ej. PEWMA.AI.md → PEWMA.AI)."""
    return name[:-3] if name.endswith('.md') else name


def find_markdown_files(start_dir, include_git_modules=False):
    """Encuentra archivos .md, opcionalmente dentro de submódulos."""
    md_files = []

    if include_git_modules:
        try:
            result = subprocess.run(
                ['git', 'ls-files', '--recurse-submodules', '*.md'],
                capture_output=True, text=True, cwd=start_dir
            )
            if result.returncode == 0:
                for f in result.stdout.strip().split('\n'):
                    if f:
                        md_files.append(os.path.join(start_dir, f))
                return md_files
        except FileNotFoundError:
            pass

    for root, dirs, files in os.walk(start_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if not include_git_modules:
            gitmodules_path = os.path.join(start_dir, '.gitmodules')
            if os.path.exists(gitmodules_path):
                try:
                    result = subprocess.run(
                        ['git', 'config', '-f', gitmodules_path,
                         '--get-regexp', 'submodule\\..*\\.path'],
                        capture_output=True, text=True, cwd=start_dir
                    )
                    submodule_paths = [
                        line.split()[-1] for line in result.stdout.strip().split('\n') if line
                    ]
                    dirs[:] = [d for d in dirs if os.path.relpath(
                        os.path.join(root, d), start_dir
                    ) not in submodule_paths]
                except FileNotFoundError:
                    pass

        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    return md_files


def build_file_index(start_dir, md_files):
    """Construye un índice de nombre_base → [rutas relativas] para resolver links."""
    index = {}
    for filepath in md_files:
        rel = os.path.normpath(os.path.relpath(filepath, start_dir))
        basename = strip_md_ext(os.path.basename(filepath))
        index.setdefault(basename, []).append(rel)
    return index


def resolve_obsidian_link(raw_link, source_file, start_dir, file_index):
    """
    Intenta resolver un link Obsidian a un link Markdown estándar.

    Retorna (link_text, rel_path) si resuelve, o (None, razón) si no.
    """
    # Separar alias: [[path|alias]]
    if '|' in raw_link:
        path_part, alias = raw_link.split('|', 1)
    else:
        path_part = raw_link
        alias = None

    # Separar anchor: [[path#heading]]
    if '#' in path_part:
        file_part, anchor = path_part.split('#', 1)
    else:
        file_part = path_part
        anchor = None

    # Buscar el archivo: primero relativo al fuente, luego global
    source_dir = os.path.dirname(os.path.relpath(source_file, start_dir))
    target_name = strip_md_ext(os.path.basename(file_part))

    # 1. Resolución relativa: buscar junto al archivo fuente
    local_candidate = os.path.join(source_dir, file_part)
    if not local_candidate.endswith('.md'):
        local_candidate += '.md'
    local_candidate = os.path.normpath(local_candidate)
    if local_candidate in file_index.get(target_name, []):
        resolved = local_candidate
    else:
        # 2. Fallback: buscar en todo el repo
        candidates = file_index.get(target_name, [])
        if '/' in file_part:
            normalized = file_part if file_part.endswith('.md') else file_part + '.md'
            candidates = [c for c in candidates if c.endswith(normalized)]

        if len(candidates) == 0:
            return None, f"archivo '{target_name}' no encontrado"
        if len(candidates) > 1:
            return None, f"ambiguo: {len(candidates)} archivos coinciden ({', '.join(candidates)})"
        resolved = candidates[0]

    # Calcular ruta relativa desde el archivo fuente
    target_rel = os.path.relpath(resolved, source_dir)

    # Construir link Markdown
    display = alias if alias else strip_md_ext(os.path.basename(resolved))
    href = target_rel
    if anchor:
        href += f"#{anchor}"

    return display, href


def scan_file(filepath):
    """Busca links Obsidian en un archivo. Retorna lista de (línea, raw_link, col_start, col_end)."""
    findings = []
    in_code_block = False
    try:
        with open(filepath, 'r', encoding='utf-8') as fh:
            for line_num, line in enumerate(fh, 1):
                stripped = line.strip()
                if stripped.startswith('```') or stripped.startswith('~~~'):
                    in_code_block = not in_code_block
                    continue
                if in_code_block:
                    continue
                clean_line = INLINE_CODE.sub(lambda m: ' ' * len(m.group()), line)
                for m in OBSIDIAN_LINK.finditer(clean_line):
                    findings.append((line_num, m.group(1), m.start(), m.end()))
    except (UnicodeDecodeError, PermissionError):
        pass
    return findings


def main():
    parser = argparse.ArgumentParser(
        description='Identifica y corrige links estilo Obsidian ([[...]]) en archivos Markdown.'
    )
    parser.add_argument(
        'directory', nargs='?', default='.',
        help='Directorio de inicio (default: ".")'
    )
    parser.add_argument(
        '--git-modules', action='store_true', default=False,
        help='Buscar también dentro de git submodules'
    )
    parser.add_argument(
        '--min-age', type=int, default=5,
        help='Solo reportar archivos modificados hace más de N minutos (default: 5)'
    )
    parser.add_argument(
        '--fix', action='store_true', default=False,
        help='Mostrar reemplazos propuestos (dry-run)'
    )
    parser.add_argument(
        '--apply', action='store_true', default=False,
        help='Junto con --fix, escribe los cambios'
    )
    parser.add_argument(
        '--show', action='store_true', default=False,
        help='Mostrar detalle por línea (default: solo nombres de archivo)'
    )
    args = parser.parse_args()

    if args.apply and not args.fix:
        print("Error: --apply requiere --fix.", file=sys.stderr)
        sys.exit(1)

    start_dir = os.path.abspath(args.directory)
    if not os.path.isdir(start_dir):
        print(f"Error: {start_dir} no es un directorio.", file=sys.stderr)
        sys.exit(1)

    md_files = find_markdown_files(start_dir, args.git_modules)
    file_index = build_file_index(start_dir, md_files) if args.fix else None

    total_findings = 0
    total_fixed = 0
    total_skipped = 0
    now = time.time()
    min_age_seconds = args.min_age * 60

    for filepath in sorted(md_files):
        try:
            mtime = os.path.getmtime(filepath)
            if (now - mtime) < min_age_seconds:
                continue
        except OSError:
            continue

        findings = scan_file(filepath)
        if not findings:
            continue

        rel_path = os.path.relpath(filepath, start_dir)

        if not args.fix:
            # Modo detección
            total_findings += len(findings)
            if args.show:
                for line_num, raw_link, _, _ in findings:
                    print(f"{rel_path}:{line_num}: [[{raw_link}]]")
            else:
                print(rel_path)
        else:
            # Modo fix: leer archivo, proponer/aplicar reemplazos
            with open(filepath, 'r', encoding='utf-8') as fh:
                lines = fh.readlines()

            modified = False
            # Procesar de atrás hacia adelante para no invalidar posiciones
            for line_num, raw_link, col_start, col_end in reversed(findings):
                display, href = resolve_obsidian_link(raw_link, filepath, start_dir, file_index)
                total_findings += 1

                if display is None:
                    print(f"  ⚠ {rel_path}:{line_num}: [[{raw_link}]] → NO RESUELTO ({href})")
                    total_skipped += 1
                else:
                    md_link = f"[{display}]({href})"
                    old = f"[[{raw_link}]]"
                    print(f"  ✓ {rel_path}:{line_num}: {old} → {md_link}")
                    total_fixed += 1

                    if args.apply:
                        line = lines[line_num - 1]
                        lines[line_num - 1] = line[:col_start] + md_link + line[col_end:]
                        modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as fh:
                    fh.writelines(lines)
                print(f"  💾 {rel_path} guardado.")

    # Resumen
    if total_findings == 0:
        print("No se encontraron links Obsidian.")
    elif args.fix:
        status = "aplicados" if args.apply else "propuestos"
        print(f"\n{total_fixed} fix(es) {status}, {total_skipped} sin resolver.")
    else:
        print(f"\n{total_findings} link(s) Obsidian en {len(md_files)} archivo(s) escaneados.")

    sys.exit(0 if total_findings == 0 else 1)


if __name__ == '__main__':
    main()
