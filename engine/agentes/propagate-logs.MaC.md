# Destilado de Logs a Proyectos

> **Audiencia:** Agente IA. Proceso de gestión bajo demanda.

---
## Trigger
- Solicitud del usuario: "destila los logs de la semana" / "destila el día X".
- Al cierre de una semana (antes de archivar la bitácora semanal).

## Objetivo
Extraer de la bitácora semanal (`actividad/`) las entradas relevantes para cada proyecto y registrarlas en la sección **Bitácora** de cada página de proyecto (`proyectos/<Área>/<proyecto>.md`). Inyección selectiva: solo lo que el proyecto necesita saber.

---
## Entrada
- **Semana completa:** El archivo activo en `actividad/` (o uno específico indicado por el usuario).
- **Día específico:** Solo la sección `## <Día>` indicada por el usuario.

## Salida
- Líneas nuevas en la sección `## Bitácora` de cada proyecto afectado.
- Actualización de la front page del área si un estado o prioridad cambió.

---
## Procedimiento

### 1. Identificar los proyectos activos
Leer el directorio `proyectos/` y listar todos los archivos de proyecto (excluyendo `AGENTS.md`, `proyectos.md` y las front pages `<Área>.md`).

### 2. Leer la bitácora semanal
Según el alcance (semana o día), cargar las entradas relevantes de `actividad/`.

### 3. Clasificar cada entrada
Para cada entrada del log (línea o bloque), evaluar:

| Pregunta | Si la respuesta es NO → descartar |
|---|---|
| ¿Es una **decisión de gestión**, un **hito**, una **sorpresa** o un **aprendizaje** vinculado a algún proyecto? | Descartar tareas operativas, commits rutinarios, reflexiones personales sin impacto en un proyecto. |
| ¿Se puede **vincular inequívocamente** a un proyecto existente en `proyectos/`? | Descartar si es transversal sin dueño claro. |

> [!important] Criterio de relevancia (de `proyectos/AGENTS.md`)
> La bitácora de un proyecto registra **decisiones, sorpresas y aprendizajes** con impacto en el proyecto. No registra tareas operativas ni commits rutinarios.
> - **Decisiones:** cambios de dirección, elección de herramientas, cambios de prioridad.
> - **Sorpresas:** desvíos significativos del plan (más tiempo del presupuestado, dependencias inesperadas, bloqueos externos).
> - **Aprendizajes:** evidencia que obliga a cambiar de approach, descubrimientos que redefinen el alcance.

### 4. Formular la línea de bitácora
El formato de cada entrada es:
```
- **YYYY-MM-DD**: Descripción concisa de la decisión, sorpresa o aprendizaje. Una línea.
```

Reglas:
- **Una línea por fecha por proyecto.** Si hay múltiples eventos del mismo proyecto en un día, condensarlos en una sola línea.
- **Voz pasiva o impersonal.** No escribir "X decidió..." sino "Decisión: ...".
- **Sin prefijo `***amigo-mac***`.** Eso es notación de la bitácora semanal, no del proyecto.
- **Sin tags** (`#TODO`, `#WISH`, etc.). Los tags viven en la bitácora semanal.

### 5. Insertar en los proyectos
Agregar la línea en la sección `## Bitácora` de cada proyecto afectado, respetando el orden cronológico (la más reciente al final).

### 6. Actualizar front pages
Si alguna entrada implica un cambio de estado o prioridad, actualizar la tabla en la front page del área (`<Área>.md`), según la regla en `proyectos/AGENTS.md`.

### 7. Reportar al usuario
Al finalizar, presentar un resumen con:

| Proyecto | Entrada destilada |
|---|---|
| `<área>/<proyecto>.md` | Texto insertado |
Indicar también si algún log fue **descartado** por no cumplir el criterio de relevancia, con una breve justificación.

---
## Límites

| Nivel | Regla |
|---|---|
| **Hacer siempre** | Presentar el reporte completo al usuario antes de escribir en los archivos. |
| **Hacer siempre** | Respetar el criterio semántico de `proyectos/AGENTS.md`: decisiones, sorpresas y aprendizajes. |
| **Preguntar primero** | Si una entrada podría pertenecer a más de un proyecto. |
| **Preguntar primero** | Si una entrada sugiere un cambio de prioridad o estado. |
| **Nunca hacer** | Insertar tareas operativas puras, reflexiones personales sin impacto en un proyecto, o logs técnicos de implementación. |
