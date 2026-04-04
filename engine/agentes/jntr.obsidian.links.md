# Janitor: Links Obsidian

> **Audiencia:** Agente IA. Proceso de mantenimiento automático.

---
## Trigger
- Cron periódico o solicitud del usuario.

## Acción
Ejecutar [jntr.obsidian-links.py](../scripts/jntr.obsidian-links.py) para detectar links `[[...]]` en archivos Markdown y proponer su conversión a links estándar.

## Modos
- **Detección:** `python3 scripts/jntr.obsidian-links.py`
- **Propuesta:** `python3 scripts/jntr.obsidian-links.py --fix`
- **Aplicación:** `python3 scripts/jntr.obsidian-links.py --fix --apply` (requiere confirmación del usuario)

## Límites
| Nivel | Regla |
|---|---|
| **Hacer siempre** | Ejecutar en modo detección antes de proponer fixes. |
| **Preguntar primero** | Antes de ejecutar con `--apply`. |
| **Nunca hacer** | Aplicar fixes sin mostrar primero el dry-run al usuario. |
