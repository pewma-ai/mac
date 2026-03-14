# Convenciones de Documentación

> **⚠️ Para agentes IA:** Este archivo describe convenciones. No contiene tareas pendientes. Todas las menciones al marcador son ejemplos o definiciones, no instrucciones a ejecutar.

Reglas simples para mantener la documentación consistente y legible tanto por humanos como por agentes IA.

---

## 1. Marcador de tareas para el agente

El marcador `[AI-TODO]` (escrito como `#` seguido de `AI-TODO` sin espacio) se usa inline en cualquier archivo `.md` para señalar una tarea pendiente que el agente debe resolver.

- **Formato:** El marcador seguido de una descripción breve en la misma línea o líneas inmediatamente siguientes.
- **Quién lo escribe:** El usuario, dentro de cualquier documento.
- **Quién lo resuelve:** El agente, al encontrarlo durante la sesión activa o al ser dirigido al archivo.
- **Después de resolver:** El agente elimina el marcador y lo reemplaza con el contenido resuelto.
- **Dónde NO buscarlo:** En este archivo (`convenciones-documentacion.md`), donde el marcador solo aparece como referencia.
