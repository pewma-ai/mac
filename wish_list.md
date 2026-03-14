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

### Preguntas abiertas

- ¿Cómo compartir conocimiento operativo (playbooks) entre organizaciones o proyectos distintos?
- ¿Debería el Método MaC formalizar el concepto de playbook como parte de su estructura recomendada?
- ¿Cuál es el mecanismo para que un agente IA sepa *cuándo* consultar el playbook sin que se le diga explícitamente?
