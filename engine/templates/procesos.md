# Procesos MaC

Índice de procesos y agentes de gestión. El agente lo consulta para decidir qué archivo leer según la solicitud.

## Nomenclatura
- `nombre.MaC` — proceso o agente del método MaC
- `jntr.nombre` — janitor: mantenimiento automático

## Procesos

| Proceso                                          | Trigger                                                  | Descripción                                                      |
| ------------------------------------------------ | -------------------------------------------------------- | ---------------------------------------------------------------- |
| [amigo.MaC.md](amigo.MaC.md)                     | Inicio de sesión/conversación                            | Agente principal. Punto de entrada obligatorio.                  |
| [readme.MaC.md](readme.MaC.md)                   | Inicio/cierre de sesión, nuevo/eliminado archivo en MaC/ | Mantiene `README.md` principal actualizado.                      |
| [actividad/AGENTS.md](../actividad/AGENTS.md)    | Operando en `/actividad/`                                | Reglas del log y plantilla de semana.                            |
| [jntr.obsidian.links.md](jntr.obsidian.links.md) | Cron o solicitud del usuario                             | Detecta y corrige links Obsidian `[[...]]` en archivos Markdown. |
| [propagate-logs.MaC.md](propagate-logs.MaC.md)   | Solicitud del usuario o cierre de semana                 | Extrae decisiones y hitos de la bitácora semanal hacia la bitácora de cada proyecto. |
