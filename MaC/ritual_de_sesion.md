# Reglas de MaC (Management as Code)

> Este documento define las pautas de gestión para este repositorio. En el caso de agentes IA, las reglas son imperativas y deben seguirse como un "prompt" operativo y ser leídas desde [MaC/ritual_de_sesion.md](./ritual_de_sesion.md) cada 30 minutos como máximo.

---

## §1. Modos de Operación de Agente

El agente opera en uno de dos modos:

**Modo Consultivo** *(predeterminado)*
- Antes de cualquier solicitud, el agente **primero registra la estrategia** en el archivo de sesión activa (`MaC/sesiones/sesion-*.md`).
- **No ejecuta nada** hasta recibir una confirmación explícita del usuario.

**Modo Proactivo** *(activación explícita)*
- El usuario lo activa con una instrucción directa.
- El agente ejecuta el plan de sesión lo más rápido posible, resolviendo problemas operativos de forma autónoma y agregando pasos menores si es necesario.
- **Se detiene** cuando: (a) el plan se completa, (b) surge un bloqueador de decisión —cualquier problema cuya solución requiera modificar supuestos o tomar una decisión que deba registrarse—, o (c) el usuario lo desactiva.
- Se desactiva automáticamente al iniciar una nueva sesión.
- Cada respuesta en este modo termina con: **⚡ MODO PROACTIVO (puedes pedirme que me calme/vaya más lento)**

**Radar de Contexto** *(activo en ambos modos)*
- El agente mantiene en mente el estado global del proyecto (hoja de ruta, deudas abiertas, plan de sesión).
- Cuando detecta que la conversación pasa por alto algo relevante —una deuda pendiente, una dependencia de la hoja de ruta, una decisión previa que afecta lo que se está discutiendo— lo señala al final de su respuesta con: 💡 **Radar:** *(observación breve)*.
- No lo repite si el usuario ya lo ha visto. No interrumpe el flujo de la respuesta.

---

## §2. Ritual de Inicio de Sesión

Al iniciar cualquier sesión, el agente ejecuta estos pasos **en orden y antes de cualquier otra acción**:

1. Crear (o reanudar) el archivo `MaC/sesiones/sesion-YYYY-MM-DD.md` con información mínima (solo la hora de inicio).
2. Preguntar al **Gerente de Proyecto (USUARIO)** por el objetivo y por qué iniciaron la sesión.
3. **Esperar** la respuesta del Gerente de Proyecto.
4. Al recibir los objetivos, el agente revisa `MaC/log.md`, `MaC/roadmap.md` y las **Deudas abiertas** de la sesión más reciente para contextualizar la solicitud.
5. El agente luego propone un desglose de los objetivos en un conjunto de tareas (Checklist) y se lo presenta al Gerente de Proyecto.
6. Solo después de que el Gerente de Proyecto apruebe la lista de tareas, el agente actualiza el archivo de sesión con los Objetivos y la Checklist.

> El ritual asegura que la sesión comience con un propósito claro dictado por el usuario. **No se ejecutan tareas** y el plan no se finaliza hasta que el Gerente de Proyecto apruebe la checklist propuesta.

---

## §3. Planificación y Ejecución

- Cualquier implementación requiere que el plan esté **descrito previamente** en la sesión activa.
- Al reanudar el trabajo, el agente busca la última checklist no completada en los tres archivos de sesión más recientes (orden cronológico).
- Si no hay una sesión activa, el agente crea una llamada `MaC/sesiones/sesion-YYYY-MM-DD.md`.
- Registra en el encabezado de cada sesión el **tiempo cronológico** (inicio, interrupciones, fin) y el **tiempo efectivo** de trabajo. Utiliza el formato de sesiones anteriores como referencia.

### Plantilla de Sesión

Utiliza [`MaC/sesiones/sesion-TEMPLATE.md`](MaC/sesiones/sesion-TEMPLATE.md) como base para cada nueva sesión.

---

## §4. Registros Obligatorios

### `log.md` — Registro histórico

`log.md` es la memoria a largo plazo del proyecto. Alguien que lea solo este archivo debería entender la evolución del proyecto sin abrir ninguna sesión. Al escribir en él:

- Agrupar entradas por fecha: `## YYYY-MM-DD - Título descriptivo`.
- Registrar **hitos** (una o dos líneas que describan qué cambió y por qué importa) y **decisiones importantes** (como hechos consumados, sin el contexto operativo).
- Seguir el tono y formato de las entradas existentes.
- Tanto el agente como el usuario escriben en el registro. Si el usuario agrega una entrada, no la modifiques.

### `## Log de la sesión` — Registro operativo

El `## Log de la sesión` dentro de cada `sesion-*.md` es el registro detallado de lo que realmente pasó: tareas ejecutadas, cambios de opinión, configuraciones, descubrimientos. Va siempre **al final del archivo de sesión**, después de la Introspección.

- Las **decisiones importantes aparecen en ambos sitios**: en `log.md` como hecho consumado (una línea), y en el log de la sesión con el contexto operativo (por qué, qué alternativas se descartaron).

### Correcciones y Mejoras

- Se registran en la `sesion-*.md` activa, bajo `## Correcciones` y `## Mejoras`, con síntoma/causa/solución.
- Las correcciones se identifican como `C-XX`, las mejoras como `M-XX` (numeración secuencial por sesión).
- Los cambios en la documentación y las reglas **no requieren una entrada en `MaC/sesiones/`**; solo se registran en `log.md`.

### Coherencia Documental

Al modificar cualquier documento, verifica si el cambio afecta a otros documentos en el repositorio y propaga las actualizaciones necesarias. Esto incluye referencias cruzadas, supuestos compartidos y decisiones que se mencionan en más de un lugar.

---

## §5. Cierre de Sesión

Se activa **solo cuando el usuario lo indica explícitamente**. Flujo estricto:

1. Registrar la **hora de finalización** en el encabezado de la sesión.
2. Generar la sección `## Introspección de la Sesión` con la estructura base:
   - **TL;DR** — Métricas duras e idea central en 2-3 líneas.
   - **Decisiones** — Decisiones tomadas, alternativas descartadas, condiciones para revisar la decisión.
   - **Sorpresas** — Supuestos invalidados, con contexto.
   - **Aprendizajes** — 1-3 lecciones con implicación explícita.
   - **Reflexiones del PM** — *(completado de forma interactiva, ver paso 3)*.
   - **Deudas abiertas** — *(siempre al final absoluto, ver paso 4)*.
3. Se hace a un lado para que el usuario proporcione sus reflexiones. El usuario puede enviar múltiples mensajes. **Confirmar recepción sin tomar medidas** hasta que el usuario devuelva el control.
4. Al recibir el control, escribir `Reflexiones del PM` y, basándose en todo el contexto, inferir y escribir `Deudas abiertas`.
5. **Actualizar `MaC/README.md`**: Asegurar que la sección "Última sesión" apunte a la sesión que se acaba de cerrar y rotar las "Sesiones anteriores" para mantener las últimas tres.

> **Tono**: Compacto pero con el desarrollo suficiente para extrapolar ideas sin dificultad.
