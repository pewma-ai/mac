#!/usr/bin/env python3
"""
Busca tags de IA (#TODO, #AI-TODO, #WISH, #IDEA, #ASK-USER) en archivos Markdown,
agrupándolos por categoría. Ignora submódulos y contenido dentro de bloques de código.

Uso:
    python jntr.find-tags.py [directorio] [--tag TAG] [--git-modules]

Parámetros:
    directorio     Directorio de inicio (default: ".")
    --tag TAG      Filtra por un tag específico (ej: TODO, WISH)
    --git-modules  Buscar también dentro de git submodules (default: False)

Salida:
    Archivo:línea: contenido (agrupado por tag)
"""

import argparse
import os
import re
import subprocess
import sys

# AI-TODO antes de TODO para que la alternancia lo pruebe primero
VALID_TAGS = ['#AI-TODO', '#TODO', '#WISH', '#IDEA', '#ASK-USER']
# Lookahead: el tag debe ir seguido de espacio, puntuación o fin de línea
TAGS_REGEX = re.compile(
    r'(' + '|'.join(re.escape(t) for t in VALID_TAGS) + r')(?=[\s:,.\-)\]!?]|$)(.*)',
    re.IGNORECASE
)
INLINE_CODE = re.compile(r'`[^`]+`')


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

    # Precalcular rutas de submódulos una sola vez
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


def scan_file(filepath, specific_tag=None):
    """Busca tags en un archivo. Ignora bloques de código y backticks inline."""
    findings = []
    in_code_block = False
    try:
        with open(filepath, 'r', encoding='utf-8') as fh:
            for line_num, line in enumerate(fh, 1):
                stripped = line.strip()
                # Ignorar bloques de código fenced
                if stripped.startswith('```') or stripped.startswith('~~~'):
                    in_code_block = not in_code_block
                    continue
                if in_code_block:
                    continue
                # Eliminar contenido dentro de backticks inline
                clean_line = INLINE_CODE.sub('', line)
                match = TAGS_REGEX.search(clean_line)
                if match:
                    tag = match.group(1).upper()
                    if specific_tag and tag != specific_tag:
                        continue
                    context = match.group(2).strip()
                    findings.append((line_num, tag, context))
    except (UnicodeDecodeError, PermissionError):
        pass
    return findings


def main():
    parser = argparse.ArgumentParser(
        description='Busca y agrupa tags MaC de IA en archivos Markdown.'
    )
    parser.add_argument(
        'directory', nargs='?', default='.',
        help='Directorio de inicio (default: ".")'
    )
    parser.add_argument(
        '--tag', nargs='?', const=None, default=None,
        help='Filtra por un tag específico (ej: WISH, AI-TODO). Default: todos'
    )
    parser.add_argument(
        '--git-modules', action='store_true', default=False,
        help='Buscar en submódulos (default: no)'
    )
    args = parser.parse_args()

    if args.tag:
        args.tag = args.tag if args.tag.startswith('#') else '#' + args.tag
        args.tag = args.tag.upper()

    start_dir = os.path.abspath(args.directory)
    if not os.path.isdir(start_dir):
        print(f"Error: {start_dir} no es un directorio.", file=sys.stderr)
        sys.exit(1)

    md_files = find_markdown_files(start_dir, args.git_modules)

    total_findings = 0
    grouped_findings = {t: [] for t in VALID_TAGS}

    for filepath in sorted(md_files):
        findings = scan_file(filepath, args.tag)
        if findings:
            rel_path = os.path.relpath(filepath, start_dir)
            for line_num, tag, context in findings:
                ctx_display = (context[:250] + '...') if len(context) > 250 else context
                entry = f"{rel_path}:{line_num}: {ctx_display}"
                if tag in grouped_findings:
                    grouped_findings[tag].append(entry)
                else:
                    grouped_findings[tag] = [entry]
                total_findings += 1

    if total_findings == 0:
        print("No se encontraron tags.")
        sys.exit(0)

    # Imprimir agrupado
    for tag in VALID_TAGS:
        if args.tag and tag != args.tag:
            continue
        items = grouped_findings.get(tag, [])
        if items:
            print(f"\n=== {tag} ({len(items)}) ===")
            for entry in items:
                print(entry)

    print(f"\nTotal: {total_findings} tag(s).")
    sys.exit(0)


if __name__ == '__main__':
    main()
