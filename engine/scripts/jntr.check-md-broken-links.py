#!/usr/bin/env python3
"""
Detecta problemas de integridad en links Markdown: links rotos y archivos huérfanos.
Solo diagnostica, no corrige — su output es input para un LLM que decide las acciones.

Uso:
    python jntr.check-md-broken-links.py [directorio] [--check MODE] [--git-modules]

Parámetros:
    directorio     Directorio de inicio (default: ".")
    --check MODE   broken, orphans, o all (default: all)
    --git-modules  Buscar también dentro de git submodules (default: no)
"""

import argparse
import os
import re
import subprocess
import sys

# Captura links markdown estándar: [texto](ruta)
# Ignora URLs externas (http://, https://, mailto:)
MD_LINK = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
INLINE_CODE = re.compile(r'`[^`]+`')
EXTERNAL = re.compile(r'^(https?://|mailto:|#)')


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

    submodule_paths = set()
    if not include_git_modules:
        gitmodules_path = os.path.join(start_dir, '.gitmodules')
        if os.path.exists(gitmodules_path):
            try:
                result = subprocess.run(
                    ['git', 'config', '-f', gitmodules_path,
                     '--get-regexp', r'submodule\..*\.path'],
                    capture_output=True, text=True, cwd=start_dir
                )
                for line in result.stdout.strip().split('\n'):
                    if line:
                        submodule_paths.add(line.split()[-1])
            except FileNotFoundError:
                pass

    for root, dirs, files in os.walk(start_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if submodule_paths:
            dirs[:] = [d for d in dirs
                       if os.path.relpath(os.path.join(root, d), start_dir)
                       not in submodule_paths]
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    return md_files


def extract_links(filepath):
    """Extrae links markdown de un archivo. Ignora bloques de código y backticks."""
    links = []
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
                clean_line = INLINE_CODE.sub('', line)
                for match in MD_LINK.finditer(clean_line):
                    text = match.group(1)
                    href = match.group(2)
                    # Ignorar links externos y anclas puras
                    if EXTERNAL.match(href):
                        continue
                    # Separar anchor del path
                    path = href.split('#')[0] if '#' in href else href
                    # Decodificar %20 → espacio
                    path = path.replace('%20', ' ')
                    if path:
                        links.append((line_num, text, path, href))
    except (UnicodeDecodeError, PermissionError):
        pass
    return links


def check_broken(start_dir, md_files):
    """Detecta links que apuntan a archivos o directorios inexistentes."""
    broken = []
    for filepath in sorted(md_files):
        rel_path = os.path.relpath(filepath, start_dir)
        file_dir = os.path.dirname(filepath)
        links = extract_links(filepath)
        for line_num, text, path, href in links:
            target = os.path.normpath(os.path.join(file_dir, path))
            if not os.path.exists(target):
                broken.append({
                    'source': rel_path,
                    'line': line_num,
                    'text': text,
                    'href': href,
                    'target': os.path.relpath(target, start_dir),
                })
    return broken


def check_orphans(start_dir, md_files):
    """Detecta archivos .md que no son referenciados por ningún otro archivo."""
    # Construir set de todos los archivos md (rutas relativas)
    all_files = set()
    for f in md_files:
        all_files.add(os.path.relpath(f, start_dir))

    # Construir set de archivos referenciados
    referenced = set()
    for filepath in md_files:
        file_dir = os.path.dirname(filepath)
        links = extract_links(filepath)
        for _, _, path, _ in links:
            target = os.path.normpath(os.path.join(file_dir, path))
            target_rel = os.path.relpath(target, start_dir)
            referenced.add(target_rel)

    # Excluir README.md de la raíz (punto de entrada), AGENTS.md (leído por agentes),
    # y templates (referenciados por convención, no por link)
    excluded = {'README.md', 'AGENTS.md'}
    orphans = []
    for f in sorted(all_files):
        basename = os.path.basename(f)
        if basename in excluded or basename.startswith('_'):
            continue
        if f not in referenced:
            orphans.append(f)

    return orphans


def main():
    parser = argparse.ArgumentParser(
        description='Detecta links markdown rotos y archivos huérfanos.'
    )
    parser.add_argument(
        'directory', nargs='?', default='.',
        help='Directorio de inicio (default: ".")'
    )
    parser.add_argument(
        '--check', choices=['broken', 'orphans', 'all'], default='all',
        help='Tipo de verificación (default: all)'
    )
    parser.add_argument(
        '--git-modules', action='store_true', default=False,
        help='Buscar en submódulos (default: no)'
    )
    args = parser.parse_args()

    start_dir = os.path.abspath(args.directory)
    if not os.path.isdir(start_dir):
        print(f"Error: {start_dir} no es un directorio.", file=sys.stderr)
        sys.exit(1)

    md_files = find_markdown_files(start_dir, args.git_modules)
    total_issues = 0

    if args.check in ('broken', 'all'):
        broken = check_broken(start_dir, md_files)
        if broken:
            print(f"\n## BROKEN LINKS ({len(broken)})")
            for b in broken:
                print(f"- {b['source']}:{b['line']} → [{b['text']}]({b['href']}) — archivo destino no existe: {b['target']}")
            total_issues += len(broken)

    if args.check in ('orphans', 'all'):
        orphans = check_orphans(start_dir, md_files)
        if orphans:
            print(f"\n## ORPHANS ({len(orphans)})")
            for o in orphans:
                print(f"- {o} — ningún archivo lo referencia")
            total_issues += len(orphans)

    if total_issues == 0:
        print("No se encontraron problemas.")
    else:
        print(f"\nTotal: {total_issues} problema(s).")

    sys.exit(0 if total_issues == 0 else 1)


if __name__ == '__main__':
    main()
