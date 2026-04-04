Gestión de la capacidad personal sobre los proyectos. Cada área agrupa proyectos según un eje de [Dirección](../estrategia/Direccion.md).

## Estructura

```
proyectos/
├── proyectos.md          ← índice general (para humanos)
├── AGENTS.md             ← este archivo (para agentes)
├── <Área>/
│   ├── <Área>.md         ← front page del área (tabla de proyectos)
│   ├── proyecto-a.md     ← página de proyecto (archivo plano)
│   └── proyecto-b.md
```

## Front page de área (`<Área>.md`)

Tabla con estado y prioridad de cada proyecto. Secciones opcionales: "En Espera", "Historial".

```markdown
## Proyectos Activos

| Proyecto | Estado | Prioridad |
|---|---|---|
| [Nombre](archivo.md) | Estado breve | Alta/Media/Baja |

## En Espera
- [Nombre](archivo.md): Razón de la espera.

## Historial
```

### Regla de actualización
Al detectar que un proyecto cambió de estado o prioridad, actualizar la front page del área correspondiente.

## Página de proyecto (`proyecto.md`)

Empieza mínimo. Escala a subdirectorio solo cuando duela no tenerlo.

```markdown
> [!info]
> Prioridad [alta/media/baja]. Justificación desde la perspectiva del usuario.

Repositorio: [org/repo](https://github.com/org/repo)
Estado: Descripción breve del estado actual.

---
## Bitácora
- **YYYY-MM-DD**: Decisión o hito de gestión. Una línea por fecha.

---
## Prioridades
- [ ] Siguiente acción de gestión.
```

### Reglas semánticas
- La **prioridad** refleja la importancia para el usuario, no para el proyecto.
- El **callout** explica por qué esa prioridad importa para la estrategia del usuario.
- La **bitácora** registra decisiones de gestión, sorpresas y aprendizajes con impacto en el proyecto. No registra tareas operativas ni commits rutinarios.
  - **Decisiones:** cambios de dirección, elección de herramientas, cambios de prioridad.
  - **Sorpresas:** desvíos significativos del plan.
  - **Aprendizajes:** evidencia que obliga a cambiar de approach.
- Las **prioridades** son las próximas acciones del usuario, no el backlog del proyecto.

## Alta de un proyecto nuevo

Al recibir una instrucción de alta de proyecto:

1. Crear la página del proyecto (`<área>/<nombre>.md`) siguiendo el template de arriba.
2. Agregar la entrada en la front page del área (`<área>/<Área>.md`).
3. Registrar el alta en la bitácora de la semana en curso.
4. Registrar el alta en el log de largo plazo (`actividad/actividad.md`).

El agente debe deducir el área correcta según [Dirección](../estrategia/Direccion.md), y preguntar si no es evidente. La prioridad inicial es siempre **Baja** salvo que el usuario indique otra cosa.

## Límites

| Nivel | Regla |
|---|---|
| **Hacer siempre** | Actualizar la front page si un estado o prioridad cambió. Usar `> [!info]` como callout. |
| **Hacer siempre** | Al dar de alta un proyecto, seguir los 4 pasos del procedimiento de alta. |
| **Preguntar primero** | Crear un área nueva. Mover un proyecto entre áreas. Cambiar la prioridad de un proyecto. |
| **Nunca hacer** | Volcar tareas operativas del proyecto aquí. Crear subdirectorios sin necesidad comprobada. |
