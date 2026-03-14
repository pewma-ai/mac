# Log

> **Sugerencia de escritura:** Priorizar la acción y el valor aportado sobre el nombre del archivo para una lectura más fluida del progreso. Sigue los ejemplos anteriores.

## 2026-03-05 - Configuración inicial
- Traducción y formalización (`MaC.md`) al español.
- Estructura de carpetas (centralizando roadmap y log en la raíz).
- Creación de esqueletos de documentos estratégicos (`roadmap.md` y `log.md`).
- Implementación de reglas automatizadas (`.cursorrules` y `.agents/rules/mac-protocol.md`) 

## 2026-03-07 - Evolución conceptual de MaC
- Definición de los principios fundamentales de la organización bajo MaC (Decisiones, Comunicación incompleta, Aprendizaje por sorpresas).
- Estructuración del sistema documental en 6 capas funcionales (Identidad, Dirección, Capacidad, Acción, Decisiones, Aprendizaje) en la guía para impacientes.
- Acuñamiento del término **Ensoñación** para describir el estado de desdibujamiento de límites durante el diseño prolongado humano-IA.

## 2026-03-10 - Refinamiento del Paradigma
- Evolución de la definición de MaC de "sistema" a "paradigma" de gestión.
- Incorporación del modelo de arquitectura de MaC mediante diagramas Mermaid (Estrategia, Acción, Evolución).
- Simplificación del Roadmap para centrarlo en iteraciones evolutivas del método.
- Adopción de un modelo de arquitectura no-lineal (flujo bidireccional) entre los tres pilares del paradigma.
- Unificación de la nomenclatura de documentos basada en archivos .md reales para aterrizar la teoría a la práctica del repositorio.
- Definición de un estándar estético de visualización técnica para diagramas Mermaid.
- Creación de un catálogo detallado de preguntas por capa y escala en `docs/preguntas-mac.md`.
- Corrección de consistencia ortográfica en la guía para impacientes y el catálogo de preguntas.
## 2026-03-13 - Lanzamiento de MaC v1.0
- Primera versión pública del método. Repositorio reorganizado, historias integradas, documentación estabilizada.
- **Decisión:** `MaC.md` renombrado a `ritual_de_sesion.md` — el protocolo operativo se separa del concepto.
- **Decisión:** `log.md` y `roadmap.md` centralizados en `MaC/` — gestión del proyecto separada de la documentación del método.
- **Decisión:** `log.md` pasa a ser registro histórico de hitos y decisiones. El detalle operativo vive en el log de cada sesión.

## 2026-03-14 - Playbook y Docsify
- Creación del directorio `playbook/` como repositorio de conocimiento operativo del proyecto (4 guías: Docsify, convenciones de documentación, convenciones Git, configuración de agentes).
- **Decisión:** El playbook vive en la raíz, no dentro de `MaC/` — es conocimiento operativo (capa Capacidad), no gestión (capa Acción).
- **Decisión:** `AGENTS.md` reemplaza a `.agents/` y `.cursorrules` como fuente de verdad para agentes IA.
- Sitio web de MaC publicado con Docsify en https://pewma-ai.github.io/mac/ — identidad corporativa PEWMA (Merriweather, terracota `#D35400`, modo claro).
- Las 3 preguntas abiertas sobre formalización del Playbook en el Método MaC fueron respondidas con la experiencia práctica de esta sesión.
