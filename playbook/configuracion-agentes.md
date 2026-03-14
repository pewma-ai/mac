# Configuración de Agentes IA en un Repositorio

> **Para humanos y agentes IA.**
> Este documento describe cómo configurar agentes IA en un repositorio, qué archivo lee cada herramienta, y cómo mantener una sola fuente de verdad.

---

## El problema

Cada herramienta de codificación IA tiene su propio archivo de instrucciones:

| Herramienta | Archivo nativo |
|---|---|
| Claude Code | `CLAUDE.md` |
| Gemini CLI | `GEMINI.md` |
| Cursor | `.cursorrules` → `.cursor/rules/*.mdc` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| OpenAI Codex CLI | `AGENTS.md` |
| Windsurf | `.windsurfrules` |

El contenido es casi idéntico en todos. Mantenerlos separados es un problema de sincronización garantizado.

## La solución: `AGENTS.md` como estándar

`AGENTS.md` es el estándar emergente. Adoptado por la Linux Foundation (diciembre 2025) bajo la Agentic AI Foundation (AAIF). Más de 60.000 repositorios open source lo usan (marzo 2026).

### Compatibilidad nativa con `AGENTS.md`

- ✅ OpenAI Codex CLI (lo originó)
- ✅ Cursor (también lee `.cursorrules` y `.cursor/rules/`)
- ✅ GitHub Copilot
- ✅ Windsurf
- ✅ Gemini CLI (configurable vía `settings.json`)
- ✅ Aider, Zed, Warp, RooCode, Kilo Code
- ⚠️ Claude Code — no nativo; workaround: referenciar desde `CLAUDE.md`

---

## Estrategia de este repositorio

### Estructura

```
/
├── AGENTS.md              ← fuente de verdad compartida
├── .cursorrules           ← apunta a AGENTS.md (compatibilidad legacy)
└── playbook/              ← guías operativas detalladas
```

### Cadena de lectura del agente

```
AGENTS.md / .cursorrules       ← "lee el ritual primero"
    ↓
MaC/ritual_de_sesion.md        ← reglas de gestión (sesiones, log, modos)
    ↓ §3: "antes de implementar"
playbook/README.md             ← índice de guías operativas
    ↓ según la tarea
playbook/<guía-específica>.md  ← instrucciones detalladas
```

El agente **no necesita leer todo**. Solo sigue la cadena:
1. Lee el ritual (obligatorio al inicio).
2. Lee el índice del playbook (antes de implementar).
3. Lee la guía específica (solo si aplica a la tarea).

---

## Anatomía de un buen `AGENTS.md`

Las secciones que más impactan el comportamiento del agente:

1. **Descripción del proyecto** — Una oración. El agente ancla todas sus decisiones ahí.
2. **Comandos** — Con flags exactos. Ponerlos temprano — el agente los referencia continuamente.
3. **Estructura del proyecto** — Dónde vive qué. Rutas relativas, nunca absolutas.
4. **Convenciones y estilo** — Reglas concretas. Un ejemplo de código vale más que tres párrafos.
5. **Límites en tres niveles** — Qué puede hacer sin preguntar, qué requiere confirmación, qué nunca hacer.
6. **Contexto adicional** — Referencias a documentos que el agente puede consultar.

### Reglas de escritura efectiva

- **Brevedad.** ~150 líneas máximo. Los archivos largos entierran lo importante.
- **Ejemplos sobre descripciones.** Un fragmento real vale más que párrafos.
- **Iterar, no planificar.** El mejor AGENTS.md crece con el tiempo — agregar una regla la segunda vez que el agente comete el mismo error.
- **Tratar como código.** Revisar en PRs, versionar, mantener actualizado.

---

## Cómo replicar en otro repositorio

1. Crear `AGENTS.md` en la raíz como fuente de verdad.
2. Si se usa Claude Code: crear `CLAUDE.md` que referencie `@AGENTS.md`.
3. Si se usa Cursor legacy: crear `.cursorrules` con el mismo contenido o una referencia.
4. Crear el ritual de sesión si se aplica MaC.
5. Crear `playbook/` con un `README.md` que indexe las guías operativas.
6. En el ritual, incluir la instrucción de consultar el playbook antes de implementar.

---

## Recursos

- Especificación AGENTS.md: https://agents.md
- GitHub Blog (análisis de 2.500+ repos): https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
- Guía completa: https://www.aihero.dev/a-complete-guide-to-agents-md
