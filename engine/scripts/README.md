# Scripts MaC

Scripts de mantenimiento. Ejecutar con `--help` para opciones.

## Janitor Scripts
Pequeños asistentes o "prótesis cognitivas". Automatizan tareas de mantenimiento tediosas para mantener el repositorio limpio y consistente. Todos los utilitarios de este tipo siguen el prefijo `jntr.`.

| Script                   | Qué hace                                            | Defaults                                 |
| ------------------------ | --------------------------------------------------- | ---------------------------------------- |
| `jntr.obsidian-links.py`         | Detecta y corrige links Obsidian `[[...]]` en `.md`              | dir: `.`, min-age: 5 min, sin submódulos |
| `jntr.find-tags.py`              | Busca y agrupa tags (`#TODO`, `#WISH`, etc)                      | dir: `.`, todos los tags, sin submódulos |
| `jntr.check-md-broken-links.py`  | Detecta links rotos y archivos huérfanos                         | dir: `.`, check: all, sin submódulos     |
