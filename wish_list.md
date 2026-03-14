# Wish List para MaC

Este archivo recopila ideas, sugerencias y posibles mejoras o iteraciones para la metodología de **Management as Code (MaC)**. Su propósito es capturar el conocimiento o problemas que surjan durante la operación diaria para integrarlos en futuras versiones del método, que se iran integrando en futuras versiones del [método MaC](../docs/metodo-mac.md).

---

## Gestión de Conocimiento

### Conclusiones (sesión 2026-03-14)

1. **Hay dos tipos de conocimiento en un proyecto MaC:**
   - **Conocimiento de gestión** — cómo se dirige el proyecto (ritual de sesión, log, roadmap). Vive dentro de `MaC/`.
   - **Conocimiento operativo** — cómo se hacen las cosas aquí: herramientas, convenciones, estándares técnicos. Es el saber tácito que un profesional trae de su experiencia y que necesita externalizar para que los agentes IA lo puedan consumir.

2. **El conocimiento operativo es una "política débil"** en términos del Método MaC. Se parece a las políticas de la capa de Capacidad (qué podemos hacer y cómo), pero no tiene la rigidez de una política formal. Guía sin mandar.

3. **El conocimiento operativo vive fuera de `MaC/`**, en un directorio separado (`playbook/`). Conceptualmente pertenece a otra capa (Capacidad) y mezclarlo con la gestión (Acción/Aprendizaje) generaría confusión a medida que crece.

4. **El `playbook/` es el manual de jugadas del proyecto.** Contiene guías que un humano o agente debe consultar antes de ejecutar tareas relacionadas. Ejemplo concreto: `docsify-github-pages.md`.

5. **Las convenciones de documentación** (como `#AI-TODO`) también viven en el playbook. Son estándares de cómo se escribe y se comunica dentro del proyecto.

6. **El agente necesita saber que el playbook existe**, pero no leerlo entero al inicio de cada sesión. Solo debe consultarlo cuando va a ejecutar una tarea que lo requiera. Esto aún está pendiente de implementar en las reglas del agente.

### Respuestas a preguntas abiertas (Actualizado 2026-03-14)

~~- ¿Cómo compartir conocimiento operativo (playbooks) entre organizaciones o proyectos distintos?~~
**Respuesta:** Como los playbooks son directorios con archivos Markdown planos, son 100% portables. Pueden versionarse como submódulos de Git (para compartirlos vivamente entre repositorios) o simplemente copiarse. El formato agnóstico e independiente en la carpeta `playbook/` asegura que no estén atados a la gestión interna de un solo proyecto.

~~- ¿Debería el Método MaC formalizar el concepto de playbook como parte de su estructura recomendada?~~
**Respuesta:** ¡Absolutamente! El Playbook es la materialización directa de la capa de **Políticas** (Pilar de Aprendizaje). Cuando el equipo enfrenta repetidamente fricciones técnicas (como el setup de Docsify, el comportamiento de Mermaid o convenciones de Markdown), usa el proceso **Consolidar** para transformar esas decisiones en el Playbook. Por tanto, el Playbook es el repositorio estructural del conocimiento operativo de MaC.

~~- ¿Cuál es el mecanismo para que un agente IA sepa *cuándo* consultar el playbook sin que se le diga explícitamente?~~
**Respuesta:** La inyección de contexto en las instrucciones base del Agente. En este repositorio lo resolvimos agregando una directriz explícita global en `AGENTS.md` bajo los *Tipos de Trabajo Operativo*: **"Antes de implementar un ítem, consultar el directorio playbook/ por si hay una guía relevante"**. El agente lee esta regla fundacional y de forma autónoma inspecciona y lee las lecciones consolidadas antes de actuar.
