# NovaTech — MaC cuando el sistema ya existe pero no conversa

*Una historia de cómo un manager de operaciones conecta lo que se vende con lo que se puede hacer, sin pedir permiso.*

---

**Víctor Morales, 50 años.** Manager de Operaciones en NovaTech Integraciones, una empresa de 80 personas que desarrolla e integra software B2B para logística y cadena de suministro en Latinoamérica. Víctor lleva doce años en la empresa. Entró como ingeniero, subió a líder técnico, y hace cuatro años es manager del área de Operaciones: 20 personas entre ingenieros de soporte, especialistas en integración y analistas de datos.

Reporta a Andrea Fuentes, gerenta general. Coordina diariamente con Comercial (que vende), Desarrollo (que construye) y Soporte (que apaga incendios). Tiene un escritorio en el cuarto piso de una oficina en Providencia con una taza que dice "Keep Calm and Read the Logs" y una pila de post-its que se cae todos los jueves.

Víctor es bueno en lo que hace. Conoce cada sistema instalado, cada cliente legacy, cada trampa técnica que puede hacer caer una integración en producción. Su equipo confía en él. Andrea lo respeta. El problema no es Víctor.

El problema es que Víctor vive entre dos mundos que no conversan.

---

## Antes de MaC — Lo que ya tienen y lo que ya falla

NovaTech no es un startup. Lleva quince años funcionando. Tiene procesos, herramientas, cadencias. El problema no es la ausencia de sistema — es que los sistemas no se hablan entre sí.

**Lo que ya existe:**

| Herramienta / Proceso | Para qué la usan | Quién la mantiene |
|---|---|---|
| JIRA | Tickets de soporte y tareas de desarrollo | Cada área administra su proyecto |
| Google Calendar | Reuniones, deadlines | Cada persona |
| Correo (Gmail corporativo) | Comunicación con clientes y entre áreas | Todos |
| Google Sheets | Tracking de FTEs, horas por proyecto | Víctor + RRHH |
| Reunión semanal de equipo | Cada persona reporta qué hizo | Víctor facilita |
| Reporte trimestral | Estado de proyectos + métricas para gerencia | Víctor lo arma manualmente |
| Team building anual | Día y medio de planificación + actividad | Andrea lo convoca |

Parece mucho. Pero la pregunta que nadie puede responder es:

> *¿Por qué estamos haciendo lo que estamos haciendo?*

Los tickets de JIRA dicen *qué* hay que hacer. El calendar dice *cuándo*. El correo dice *quién pidió qué*. Pero ningún sistema conecta el ticket de hoy con el objetivo del trimestre, ni el objetivo del trimestre con la razón de ser de la empresa. Víctor lo llama "el agujero del medio": información arriba (lo que Andrea quiere), información abajo (lo que el equipo hizo), y nada que las conecte.

Un martes de febrero, la desconexión explota.

Sebastián, director comercial, cierra una venta grande: un cliente de minería necesita integrar tres sistemas de logística en seis meses. Es el contrato más grande del año. Sebastián lo celebra en el grupo de WhatsApp con emojis de champagne.

Víctor lee el mensaje y siente un escalofrío. Abre JIRA. Su equipo tiene 14 tickets activos de alta prioridad. Tres de sus ingenieros están asignados parcialmente a otros departamentos en modo matrix. El módulo que el cliente minero necesita tiene deuda técnica acumulada de dos años. Seis meses es imposible. Nueve, tal vez. Doce, seguro.

Llama a Andrea.

> **— Andrea, ¿viste lo de minería?**
> **— Sí, es enorme. Sebastián está feliz.**
> **— Sebastián está feliz porque no sabe lo que tenemos debajo. Ese módulo está con deuda técnica de dos años. No podemos integrar tres sistemas en seis meses sin parar todo lo demás.**
> **— ¿Y eso dónde está escrito?**

Silencio.

No está escrito. Está en la cabeza de Víctor. En las conversaciones de pasillo entre sus ingenieros. En los tickets de JIRA que llevan seis meses abiertos y que nadie mira porque siempre hay algo más urgente.

> **— Víctor, necesito que me muestres eso. En datos. Porque si yo no lo veo, Sebastián tampoco.**

Víctor vuelve a su escritorio. Tiene un problema y una idea.

---

## Fase 1 — El MaC personal de Víctor (Trimestre 1)

Víctor no le propone a nadie "implementar un sistema". No pide presupuesto ni aprobación. Abre Obsidian en su laptop — lo usa hace años para notas técnicas — y crea una carpeta nueva: `MaC-Víctor`.

No sabe que se llama MaC. Lo llama "mi cuaderno de mando". La idea es simple: replicar en un solo lugar lo que hoy está disperso en JIRA, Sheets, correo y su cabeza.

### Mes 1 — Leer lo que ya existe

Lo primero que hace Víctor no es escribir, sino *leer*. Pasa dos semanas cruzando fuentes manualmente:

- Exporta los tickets de JIRA de su área (abiertos, cerrados, bloqueados)
- Exporta el sheet de asignación de FTEs
- Revisa los correos de los últimos tres meses con clientes internos (las áreas que le piden capacidad)
- Revisa las actas informales de sus reuniones semanales (notas en su cuaderno físico)

Y lo sintetiza en un solo documento:

> `MaC-Víctor/estado-del-area.md — Febrero 2026`
>
> **Equipo:** 20 personas. 14 jornada completa en Operaciones, 6 en modo matrix (prestados a Desarrollo y Soporte).
>
> **Carga actual:**
> - 47 tickets activos en JIRA (14 alta prioridad, 22 media, 11 baja)
> - 3 proyectos de integración en curso (Minera del Sur, Logística Central, RetailPro)
> - 6 FTEs comprometidos con otros departamentos hasta abril
>
> **Lo que no está en JIRA:**
> - Deuda técnica del módulo de integración logística: ~400h estimadas de refactoring
> - 2 personas del equipo están aprendiendo un stack nuevo sin que esté planificado
> - La documentación de 3 integraciones legacy la tiene solo Rodrigo (single point of failure)
>
> **Sorpresas del último trimestre que nadie registró:**
> - El proyecto RetailPro se extendió 6 semanas por un cambio de alcance que comercial aceptó sin consultar
> - Soporte pidió 2 FTEs extra en diciembre que nunca se devolvieron
> - El onboarding de nuevos clientes pasó de 3 semanas a 5 sin que nadie lo decidiera explícitamente

Ese documento no existe en ningún otro lugar de NovaTech. JIRA tiene los tickets pero no el contexto. Sheets tiene los FTEs pero no las dependencias. El correo tiene las quejas pero no el patrón.

Víctor mira el documento y piensa: *si Andrea pudiera ver esto, la conversación sobre minería sería completamente distinta.*

> [!NOTE]
> **¿Qué proceso MaC acaba de ocurrir?**
> **Registrar** (Proceso 5): Tareas → Resultados con sorpresas. Pero con una diferencia crucial respecto a Javiera o Nexo: Víctor no registra desde cero. *Lee sistemas que ya existen y los sintetiza en un formato que conecta lo que antes estaba disperso.* Esa síntesis — cruzar JIRA con Sheets con correos con conversaciones informales — es lo que genera visibilidad nueva.

### Mes 2 — Bitácora personal de gestión

Víctor empieza algo más: una bitácora semanal donde anota qué hizo como *manager*, no como técnico. No lo que su equipo hizo — eso está en JIRA. Lo que él hizo: decisiones, conversaciones, problemas que escaló, cosas que vio.

> `MaC-Víctor/bitacora/semana-2026-03-10.md`
>
> - Reunión con Andrea: presenté el estado del área. Reacción: sorpresa con el dato de deuda técnica. Me pidió que lo cuantifique en horas y costo. ✓
> - Hablé con Sebastián sobre minería. Le expliqué la situación del módulo. No le gustó pero entendió. Pidió que le dé "la versión de 3 frases que pueda decirle al cliente". Pendiente.
> - **Sorpresa:** Descubrí que el equipo de Soporte está usando un workaround en producción que nadie documentó. Si falla, se cae la integración de Logística Central. Se lo dije a Patricia (jefa de Soporte) por Slack. No respondió.
> - Reunión semanal de equipo: Rodrigo mencionó que lleva tres sprints posponiendo el refactoring del módulo logístico porque siempre entra algo más urgente. El equipo asintió — todos lo sabían, nadie lo había dicho en voz alta.
> - **Decisión informal (no registrada en ningún lado):** Le dije a Carla que posponga la documentación de RetailPro y se enfoque en minería. No lo consulté con nadie. Probablemente debería haberlo hecho.

Al final del mes, Víctor tiene cuatro bitácoras. Las relee un domingo. Ve algo que no veía en el día a día: pasa el 40% de su tiempo coordinando entre áreas — reuniones con Soporte, con Comercial, con Andrea — y solo el 20% haciendo gestión real de su equipo. El otro 40% se va en apagar incendios.

> [!TIP]
> **MaC Tip — En una organización, el primer log no es de tareas sino de gestión.** Víctor no necesita registrar qué hizo su equipo — JIRA ya lo hace. Lo que necesita registrar es lo que *él* hace como manager: las decisiones informales, las conversaciones de pasillo, los compromisos que asumió por teléfono. Eso es lo que no tiene sistema y lo que más impacto tiene.

### Mes 3 — La primera decisión documentada

El log de Víctor acumula tres meses de bitácoras. El patrón más visible: cada vez que comercial cierra una venta, el alcance técnico es diferente a lo que operaciones puede entregar. No es mala fe — es que Sebastián no tiene visibilidad de la capacidad real.

Víctor escribe su primera decisión:

> `MaC-Víctor/decisiones.md`
>
> `2026-04-14` — **Validación técnica pre-venta**
> **Decisión:** A partir de ahora, pido que me incluyan en la revisión técnica de toda propuesta comercial que involucre integración, antes de que se envíe al cliente. No para vetar — para anotar las restricciones técnicas reales.
> **Motivo:** 3 de los últimos 4 proyectos tuvieron desfases de alcance porque la propuesta comercial no consideró el estado real de la plataforma.
> **Quién decide:** Yo (Víctor). Necesito que Andrea lo valide para que Sebastián acepte.
> **Revisar si:** Comercial adopta un proceso propio de validación técnica que haga esto innecesario.

Se la presenta a Andrea con los datos de las tres bitácoras. Andrea lee, mira los números, y dice:

> **— ¿Tres de cuatro?**
> **— Tres de cuatro. Y el cuarto fue porque era un cliente que ya conocíamos.**
> **— Okay. Se lo digo a Sebastián. Pero vas a tener que ir a las reuniones de pre-venta.**
> **— Prefiero ir a la reunión de pre-venta que a la reunión de crisis tres meses después.**

Andrea sonríe. Es la primera vez que Víctor llega con datos en vez de con quejas.

> [!IMPORTANT]
> **Coherencia vertical.** Lo que Víctor está construyendo sin saberlo es lo que MaC llama "coherencia vertical" — la conexión entre lo que se hace abajo (tickets, tareas) y por qué se hace arriba (objetivos, estrategia). En NovaTech esa conexión no existía. JIRA decía qué hacer; Andrea decía hacia dónde ir; pero nadie conectaba las dos cosas. El `estado-del-area.md` de Víctor es el primer documento que cruza niveles.

---

## Fase 2 — El agente como lector de sistemas (Trimestre 2)

Víctor lleva tres meses haciendo la síntesis entre JIRA, Sheets y correo a mano. Le toma dos horas cada semana. Funciona, pero no escala.

Un ingeniero de su equipo, Luis, le propone algo:

> **— Víctor, ¿y si automatizo la parte tediosa? Puedo hacer un agente que lea JIRA y el sheet de FTEs y te arme el borrador del estado del área.**
> **— ¿Cuánto te toma?**
> **— Dame un viernes.**

Luis construye un agente con acceso a JIRA vía API y al Google Sheet de FTEs vía MCP. El agente lee ambas fuentes cada viernes y genera un borrador en la carpeta de Víctor en Obsidian.

### Lo que el agente genera automáticamente

> `🤖 Estado del área — Semana del 12 de mayo`
>
> **Fuentes:** JIRA (proyecto OPS), Sheet FTE-asignaciones, Calendar Víctor
>
> **Tickets activos:** 43 (↓4 vs semana pasada)
> - Alta prioridad: 12 (↓2) — 3 cerrados, 1 nuevo
> - Bloqueados: 4 — *MIN-234 (esperando input de Comercial, 8 días), LOG-189 (dependencia de Desarrollo, 12 días ⚠️)*
>
> **FTEs esta semana:**
> - En Operaciones: 14.5
> - Prestados a Desarrollo: 3
> - Prestados a Soporte: 2.5
> - **Cambio:** Soporte pidió +0.5 FTE el miércoles. No está formalizado en el sheet. ⚠️
>
> **Métricas:**
> - Tiempo promedio de resolución tickets alta prioridad: 4.2 días (target: 3 días)
> - Tickets reabiertos este mes: 7 (vs 3 el mes anterior ⚠️)
>
> **Lo que no pude inferir:**
> - _¿El bloqueo de MIN-234 tiene alternativa o hay que escalar?_
> - _¿El aumento de tickets reabiertos tiene una causa común?_
> - _¿La asignación extra a Soporte fue acordada o fue un favor informal?_
> - _¿Hubo conversaciones con clientes que cambiaron prioridades esta semana?_

Víctor mira el borrador. El 70% está hecho. Completa las preguntas en diez minutos: MIN-234 necesita escalamiento, los tickets reabiertos son porque cambiaron un componente compartido sin avisar, y lo de Soporte fue un favor de Víctor a Patricia que no estaba planificado.

Esas diez minutos le devuelven las dos horas que antes pasaba cruzando sistemas.

> [!TIP]
> **MaC Tip — En una organización, el agente no reemplaza herramientas: las lee.** Víctor no migró JIRA ni el sheet a Obsidian. El agente lee esos sistemas y sintetiza en un formato que conecta lo que antes estaba disperso. MaC no compite con JIRA — se sienta encima y le da contexto.

### El agente empieza a preguntar

Al segundo mes, Luis agrega una función: el agente cruza los tickets de JIRA con el `decisiones.md` personal de Víctor y genera preguntas de coherencia.

> `🤖 Revisión mensual — Junio`
>
> **Coherencia con decisiones:**
> - Decisión del 14/4: "Validación técnica pre-venta para toda propuesta de integración." He detectado 2 propuestas comerciales enviadas en mayo sin tag de revisión técnica en el workflow. ¿Se aplicó la decisión?
>
> **Capacidad:**
> - La suma de FTEs comprometidos (14.5 + 3 + 2.5 + estimación de minería) excede los 20 FTEs disponibles en 1.5. Esto no incluye vacaciones de julio (3 personas). ¿Hay que renegociar asignaciones matrix?
>
> **Patrones en tickets:**
> - LOG-189 lleva 12 días bloqueado esperando input de Desarrollo. Es la tercera vez en 4 meses que un ticket se bloquea por la misma dependencia (módulo compartido con Desarrollo). ¿Hay que escalar o formalizar una política de SLA interno?

La pregunta sobre las propuestas sin validación técnica es incómoda. Víctor revisa: efectivamente, dos propuestas salieron sin su revisión. Sebastián "se olvidó" de incluirlo. Víctor lleva los datos a Andrea, que convierte la decisión personal de Víctor en un paso formal del workflow de Comercial.

> [!NOTE]
> **¿Qué proceso MaC acaba de ocurrir?**
> **Interpretar** (Proceso 6): Resultados → Decisión documentada. Pero también está ocurriendo algo más sutil: la decisión personal de Víctor (*"pido que me incluyan"*) se convirtió en un proceso organizacional (*paso formal en el workflow de Comercial*). El aprendizaje de un manager subió un nivel. Esto es el inicio de **Actualizar** — cuando una decisión local afecta la estrategia o los procesos de la organización.

---

## Fase 3 — Del MaC personal al MaC de equipo (Trimestre 3)

Algo empieza a pasar en las reuniones semanales de Víctor con su equipo. Antes, la reunión era un reporte: cada persona decía qué hizo, Víctor anotaba en su cuaderno, y al final preguntaba "¿algo más?" que siempre significaba "nada más".

Ahora Víctor llega con datos. Sabe exactamente qué tickets están bloqueados, hace cuánto, y por qué. Sabe quién está sobrecargado y quién tiene capacidad. Sabe qué cosas se decidieron informalmente y cuáles siguen flotando.

El equipo nota la diferencia.

> **— Víctor, ¿de dónde sacas todo eso?**

Rodrigo se lo pregunta un lunes después de que Víctor identificara un bloqueo cruzado entre tres tickets que nadie había conectado.

> **— Tengo un agente que lee JIRA y el sheet de FTEs, y yo completo con lo que pasa fuera del sistema. Todo queda en unos archivos de texto.**
> **— ¿Podemos verlo?**
> **— No es secreto. Es solo mi forma de no perder el hilo.**

Víctor no impone nada. Pero empieza a hacer dos cosas en la reunión semanal que antes no hacía:

**1. Muestra el plan de la semana antes de discutirlo.** El agente ya genera un borrador de prioridades. Víctor lo proyecta en la tele de la sala y pregunta: *"¿Esto es lo correcto o hay algo que cambiar?"*

**2. Pide anotar las sorpresas.** No un reporte formal. Solo una línea: *¿Qué pasó esta semana que no esperabas?*

Al principio, las respuestas son tímidas. "Nada especial." "Todo normal." Pero después de tres semanas, Carla dice:

> **— El onboarding de Minera del Sur está tomando el triple de lo estimado porque su sistema legacy tiene una API no documentada. No es un bug, es que nadie sabía que existía ese componente.**

Ese dato no estaba en JIRA. Estaba en la cabeza de Carla. Ahora está escrito.

### El vault del equipo

En julio, Víctor crea un vault compartido en Obsidian. No migra nada de JIRA — el vault es una capa de *gestión* que lee los sistemas existentes.

> `MaC-OPS/` (Vault del equipo de Operaciones)
> ```
> MaC-OPS/
> ├── identidad.md              ← ¿Por qué existe este equipo?
> ├── direccion.md              ← Objetivos del semestre
> ├── capacidad.md              ← FTEs, restricciones, dependencias
> ├── plan-semanal.md           ← Prioridades de la semana (agente propone)
> ├── log-semanal/              ← Semana a semana, con sorpresas
> │   ├── semana-2026-07-07.md
> │   ├── semana-2026-07-14.md
> │   └── ...
> ├── decisiones.md             ← Decisiones del equipo con trazabilidad
> ├── politicas/                ← Políticas consolidadas
> └── reportes/                 ← Reportes trimestrales (agente genera borrador)
> ```

Y en paralelo, Víctor mantiene su vault personal:

> `MaC-Víctor/` (Vault personal de Víctor)
> ```
> MaC-Víctor/
> ├── bitacora/                 ← Lo que Víctor hace como manager
> ├── decisiones.md             ← Decisiones personales (qué escalar, qué no)
> ├── notas-andrea.md           ← Preparación para reuniones con gerencia
> └── reflexiones.md            ← Lo que Víctor piensa pero no dice en reunión
> ```

Los dos vaults están conectados: el agente lee ambos y puede cruzar información entre el nivel personal de Víctor y el nivel del equipo.

> [!IMPORTANT]
> **Anidamiento de MaC: persona ↔ equipo ↔ organización.** Víctor tiene un MaC personal que alimenta y se alimenta del MaC de su equipo. Su bitácora personal incluye cosas que no comparte con el equipo (sus reflexiones sobre Andrea, sus dudas sobre Sebastián). El vault del equipo incluye cosas que Víctor no genera solo (las sorpresas de Carla, las alertas de Rodrigo). El agente es el puente: sintetiza del nivel individual al colectivo, y traduce del nivel colectivo al reporte que Víctor lleva a gerencia.

---

## Fase 4 — Identidad y Dirección del equipo (Trimestre 3–4)

Con el vault funcionando y la reunión semanal convertida en algo útil, Víctor se hace una pregunta que nunca se había hecho:

> *¿Por qué existe mi equipo?*

No la empresa — eso lo sabe todo el mundo (NovaTech existe para ser el socio tecnológico invisible de la cadena de suministro). Sino su equipo específico. Operaciones. ¿Qué resuelve? ¿Para quién existe dentro de la empresa?

Lo pregunta en una reunión semanal. Las respuestas son reveladoras:

> **Rodrigo:** "Mantenemos todo funcionando."
> **Carla:** "Integramos los sistemas de los clientes con la plataforma."
> **Luis:** "Apagamos incendios."
> **Una analista junior:** "Hacemos lo que Comercial promete."

Esa última frase golpea. Víctor la anota. Es honesta y es el problema.

Después de la reunión, Víctor escribe un borrador de identidad del equipo. Lo lleva a la siguiente reunión para validar:

> `MaC-OPS/identidad.md`
>
> **¿Por qué existe Operaciones?**
> Para que las integraciones de NovaTech funcionen de manera estable y predecible, hoy y mañana. Somos el equipo que convierte la promesa comercial en realidad técnica sostenible.
>
> **¿Qué nos diferencia dentro de NovaTech?**
> Somos los únicos que ven el sistema completo: las integraciones activas, la deuda técnica, las dependencias entre clientes. Comercial ve la oportunidad. Desarrollo ve el código. Nosotros vemos cómo se comporta todo junto en producción.
>
> **¿Para quién trabajamos?**
> Primariamente: los clientes que ya están integrados (estabilidad). Secundariamente: los clientes nuevos que están en onboarding (implementación). Terciariamente: otros departamentos que nos piden capacidad (matrix).
>
> **¿Qué NO somos?**
> No somos el equipo de overflow de Desarrollo. No somos soporte de primer nivel. No somos el lugar donde se mandan las cosas que nadie más quiere hacer.
>
> **Principio no negociable:**
> No comprometemos la estabilidad de producción para cumplir una fecha que alguien más prometió sin consultarnos.

Hay un silencio largo después de que Víctor lee el último punto. Rodrigo dice:

> **— Si eso hubiera existido hace un año, el incidente de RetailPro no habría pasado.**
> **— Lo sé** — dice Víctor —. **Por eso lo estoy escribiendo ahora.**

Con la Identidad escrita, Víctor arma la Dirección del equipo:

> `MaC-OPS/direccion.md — Objetivos S2 2026`
>
> 1. Reducir tickets reabiertos a ≤3/mes (hoy: 7/mes promedio)
> 2. Documentar las 5 integraciones legacy críticas para eliminar dependencia de Rodrigo
> 3. Formalizar proceso de validación técnica con Comercial (que cada propuesta tenga review técnico antes de salir)
> 4. Reducir tiempo de onboarding de nuevos clientes de 5 semanas a 3.5

Cada objetivo lo contrasta con la Identidad antes de confirmarlo. El objetivo 3 es coherente: si la promesa comercial no pasa por Operaciones, la estabilidad de producción se compromete. El objetivo 4 es coherente: el onboarding rápido es lo que hace a NovaTech confiable.

Esto es **Enmarcar**.

Luego dimensiona:

> `MaC-OPS/capacidad.md — Actualización agosto`
>
> **FTEs disponibles para objetivos internos:** 5 (de 20, descontando operación diaria y matrix)
> **Restricción 1:** Rodrigo es single point of failure para integraciones legacy. Si se enferma, 3 clientes quedan sin soporte L3.
> **Restricción 2:** La revisión mensual de FTEs matrix compite con los objetivos internos — cada mes el equipo puede perder o ganar 1-2 FTEs sin aviso.
> **Restricción 3:** El team building anual (noviembre) consume una semana real entre preparación y asistencia.
> **Dependencia externa:** Desarrollo tiene un release cycle de 4 semanas. Cualquier mejora que necesite código nuevo tarda al menos un ciclo completo.

Con esos números, el objetivo 2 (documentar integraciones legacy) necesita 6 meses, no 3, porque Rodrigo no puede parar de hacer soporte para documentar. Víctor ajusta el plazo.

> [!NOTE]
> **¿Qué procesos MaC se activaron?**
> - **Enmarcar** (1): Identidad → Dirección. *¿Estos objetivos son coherentes con lo que somos?*
> - **Dimensionar** (2): Dirección → Capacidad revisada. *¿Tenemos los medios realmente?*
>
> Lo interesante es que Víctor puede responder preguntas que antes nadie hacía: *¿Los objetivos más exigentes están asignados a los períodos de mayor capacidad?* No — están asignados a los períodos donde hay más FTEs prestados a otros departamentos. *¿Hay dependencias externas que aparecen en más de un objetivo sin plan B?* Sí — el release cycle de Desarrollo afecta al objetivo 1 y al 4. Estas son preguntas de la capa de Capacidad que antes no tenían dónde vivir.

---

## Fase 5 — El reporte trimestral que cambió la conversación (Trimestre 4)

Llega octubre y Víctor tiene que preparar el reporte trimestral para Andrea. Antes, esto le tomaba un día entero: abrir JIRA, exportar datos, armar un PowerPoint, inventar métricas que sonaran bien, y presentar algo que Andrea leía una vez y archivaba.

Esta vez, el agente genera el borrador.

> `🤖 Borrador reporte-trimestral — Q3 2026`
>
> **Fuentes:** JIRA (OPS), Sheet FTEs, `MaC-OPS/log-semanal/*`, `MaC-OPS/decisiones.md`, `MaC-OPS/direccion.md`
>
> **Estado de objetivos S2:**
> | Objetivo | Estado | Comentario |
> |---|---|---|
> | Reducir tickets reabiertos a ≤3/mes | 🟡 En progreso | Julio: 6, Agosto: 5, Sept: 4. Tendencia positiva. |
> | Documentar integraciones legacy | 🟡 30% completado | 2 de 5 documentadas. Rodrigo al 95% de capacidad. |
> | Validación técnica pre-venta | ✅ Implementado | 8 de 8 propuestas revisadas en Q3. 2 ajustes de alcance detectados pre-venta. |
> | Onboarding 5 → 3.5 semanas | 🔴 Sin avance | Bloqueado por dependencia de Desarrollo (modificación del wizard de onboarding). Ticket DEV-890 abierto hace 6 semanas sin asignación. |
>
> **Decisiones tomadas en el trimestre:** 4
> - Formalización de review técnico pre-venta (ahora en workflow de Comercial)
> - Política de SLA interno con Desarrollo para tickets bloqueantes (72h máximo)
> - Reasignación de Carla a documentación legacy 2 días/semana
> - Postergación de onboarding improvement hasta Q4 (por bloqueo de Desarrollo)
>
> **Sorpresas del trimestre:**
> - El componente compartido entre OPS y DEV genera el 40% de los tickets reabiertos. Patrón visible desde hace 3 meses.
> - La asignación matrix está consumiendo 2h semanales de coordinación que no se contabilizan.
>
> **Preguntas para gerencia:**
> - _¿El objetivo de onboarding sigue siendo prioridad si Desarrollo no puede asignar recursos hasta Q1 2027?_
> - _¿El modelo matrix actual es sostenible si la carga de Operaciones sigue creciendo?_
>
> **Lo que no pude incluir:**
> - _Feedback cualitativo de clientes (no tengo acceso a encuestas de satisfacción)_
> - _Impacto de la deuda técnica en velocidad de entrega (requiere estimación humana)_

Víctor revisa el borrador. Agrega dos párrafos de contexto y cambia el orden. Le toma cuarenta y cinco minutos en vez de un día.

Pero lo importante no es el ahorro de tiempo. Lo importante es que el reporte tiene una sección que antes no existía: **"Preguntas para gerencia"**. No son quejas. Son preguntas específicas que necesitan respuesta de alguien con autoridad para decidir.

Andrea lee el reporte y llama a Víctor:

> **— Esta es la primera vez que tu reporte me hace pensar en vez de solo informarme.**
> **— Antes no tenía los datos para hacer las preguntas correctas.**
> **— La pregunta sobre matrix me la llevo a la reunión con directores. Necesito que prepares un escenario alternativo.**

> [!TIP]
> **MaC Tip — El reporte no es para informar, es para decidir.** Un reporte que solo muestra métricas se archiva. Un reporte que termina con preguntas que requieren decisión de alguien con autoridad se convierte en una herramienta de gestión. El agente puede generar las métricas. El humano aporta las preguntas que las métricas provocan.

---

## Fase 6 — Consolidar: de decisiones a políticas (Trimestre 4–5)

El `decisiones.md` del equipo tiene 14 entradas. El agente detecta patrones:

> `🤖 Patrones detectados en decisiones.md`
>
> **Patrón 1 — Asignación matrix (3 decisiones):**
> - `2026-07-18`: "No aceptar asignaciones matrix sin 48h de aviso"
> - `2026-08-29`: "Registrar toda asignación matrix en el sheet antes de que empiece"
> - `2026-09-15`: "Si una asignación matrix supera 2 semanas, requiere aprobación de Víctor"
>
> **Patrón 2 — Gestión de deuda técnica (2 decisiones):**
> - `2026-08-05`: "Dedicar 1 día/sprint a deuda técnica del módulo logístico"
> - `2026-09-22`: "No aceptar workarounds como solución definitiva — crear ticket de deuda por cada workaround"
>
> ¿Quieren consolidar alguno en política?

Víctor lleva los patrones a la reunión semanal. El equipo consolida el primero:

> `MaC-OPS/politicas/matrix.md`
>
> **Política: Gestión de asignaciones matrix**
> *Origen: Decisiones del 18/7, 29/8 y 15/9*
>
> 1. Toda asignación matrix se registra en el Sheet de FTEs antes de iniciar. Sin registro, no empieza.
> 2. Se requiere un aviso mínimo de 48 horas hábiles antes de la asignación.
> 3. Asignaciones de más de 2 semanas requieren aprobación de Víctor y quedan registradas en `decisiones.md` con impacto en capacidad.
> 4. En la revisión mensual de FTEs, se evalúa si las asignaciones matrix del mes afectaron los objetivos del equipo.
>
> **Para quién aplica:** Toda solicitud de FTE de otro departamento.
> **Revisar si:** Cambia la estructura organizacional o se crea un pool formal de recursos compartidos.

Víctor lleva la política a Andrea. Andrea la valida y la comunica a los otros directores. Es la primera vez que una regla de funcionamiento de Operaciones nace desde la evidencia del equipo y sube hasta la gerencia.

> [!NOTE]
> **Proceso MaC: Consolidar (7)**
> Decisiones → Política. La pregunta clave: *¿Esto ya es una regla o seguimos decidiendo caso a caso?*
>
> En una organización mediana, consolidar tiene un efecto que no existe en escalas menores: la política cruza fronteras departamentales. La política de matrix no solo afecta a Operaciones — cambia cómo Desarrollo y Soporte piden recursos. Una decisión local se convirtió en una regla organizacional.

---

## Fase 7 — El agente como consultor estratégico (Trimestre 5–6)

El agente de Víctor ha evolucionado. Ya no solo llena borradores (prótesis cognitiva) ni solo hace preguntas de coherencia (asesor de gestión). Ahora cruza información entre el vault personal de Víctor, el vault del equipo, y los sistemas corporativos para señalar tensiones *estratégicas*.

### Lo que el agente detecta en diciembre

> `🤖 Revisión estratégica — Diciembre 2026`
>
> **Cruce: Identidad OPS vs. realidad operativa**
> La Identidad del equipo dice: *"No comprometemos la estabilidad de producción para cumplir una fecha que alguien más prometió."* Sin embargo, en los últimos 3 meses:
> - 2 releases se desplegaron fuera del proceso normal por presión de Comercial
> - 1 incidente en producción fue causado por un deploy acelerado que saltó la validación
> - Los 3 casos están documentados en `log-semanal` pero no generaron ninguna decisión
>
> ¿La Identidad sigue siendo lo que el equipo practica, o hay que actualizar la Identidad o cambiar la práctica?
>
> **Cruce: Capacidad OPS vs. plan comercial 2027**
> He leído el borrador del plan comercial 2027 (compartido por Andrea en Drive). Contempla 4 nuevos clientes de integración en S1. Según la capacidad actual del equipo (5 FTEs disponibles para nuevos proyectos, 6 en matrix), NovaTech necesitaría:
> - +3 FTEs para cubrir los 4 onboardings sin afectar operación
> - O reducir asignaciones matrix de 6 a 3 FTEs
> - O extender el timeline de onboarding de 3.5 a 6 semanas por cliente
>
> Esta tensión no está visible en ningún documento activo. ¿Quieres que prepare un escenario para presentar a Andrea?
>
> **Cruce: Decisiones Víctor vs. decisiones equipo**
> En tu vault personal tienes 3 decisiones que no están en el vault del equipo:
> - "Postergar evaluación de Rodrigo hasta que termine la documentación" (14/11)
> - "No escalar el tema matrix a directores hasta tener 3 meses de datos" (2/10)
> - "Pedir a Andrea presupuesto para un ingeniero senior adicional" (28/11)
> Las 3 afectan la capacidad del equipo. ¿Alguna debería comunicarse al equipo o registrarse en su vault?

Víctor mira esa revisión un sábado por la mañana. La segunda alerta — la de capacidad vs. plan comercial — es exactamente el tipo de dato que Andrea necesita *antes* de aprobar el plan, no después. La tercera alerta le recuerda que tiene decisiones personales que afectan a su equipo y que nadie más conoce.

El lunes, Víctor prepara el escenario que el agente sugirió y lo incluye en su reunión con Andrea. Es la primera vez que Operaciones llega a la conversación de planificación anual con un análisis de capacidad *antes* de que el plan se apruebe.

> **— Víctor, esto es exactamente lo que necesitaba para la reunión con directores.**
> **— No te voy a mentir, Andrea. Gran parte de esto lo armó el agente. Yo puse el criterio de qué importa y qué no.**
> **— Me da igual quién lo armó. Me importa que existe.**

> [!WARNING]
> **El agente como consultor estratégico es el nivel más potente y más riesgoso.** Cuando el agente cruza el plan comercial de 2027 con la capacidad de Operaciones, está haciendo algo que antes solo haría un consultor externo o un COO muy atento. El riesgo: que el manager confíe ciegamente en el cruce sin validar los supuestos. El agente lee datos; el humano entiende la política interna, las relaciones de poder, y el contexto que no está en ningún archivo. El agente señala la tensión. Víctor decide si la surfacea, cómo y cuándo.

---

## Fase 8 — Actualizar: el team building que no fue team building (Mes 12)

Noviembre. El team building anual de todo NovaTech. Un día y medio en un hotel fuera de Santiago. Parrilla, actividades, y la temida "sesión de planificación estratégica" de la mañana del segundo día, que históricamente consiste en Andrea presentando un PowerPoint y todos asintiendo.

Este año, Andrea le pide a Víctor que presente algo diferente.

Víctor trae los datos del año. Pero no los presenta como métricas — los presenta como aprendizajes. Lo que el equipo descubrió, decide y cambió a lo largo de doce meses.

> **Lo que aprendimos en 2026:**
> 1. El 40% de los desfases de proyecto se originan en propuestas comerciales que no pasan por validación técnica *(dato de 8 propuestas revisadas vs. 4 que no lo fueron)*
> 2. Las asignaciones matrix sin proceso consumen 2h semanales de coordinación invisible *(dato de 6 meses de registro)*
> 3. La deuda técnica no registrada es una bomba de tiempo: el incidente de octubre costó 80h de trabajo reactivo *(dato del log)*
> 4. El conocimiento concentrado en una persona es el mayor riesgo operativo que tenemos *(dato: 2 de 5 integraciones legacy documentadas en 6 meses porque Rodrigo no puede parar)*

Sebastián escucha lo del punto 1 y dice:

> **— Pero la validación técnica ralentiza el proceso comercial.**
> **— Ralentiza la propuesta 48 horas. Sin validación, el proyecto se extiende 6 semanas. ¿Qué es más lento?**

Andrea interviene. No para mediar — para proponer algo que nadie esperaba:

> **— Lo que Víctor construyó en Operaciones debería existir en cada área. No el sistema exacto — el principio. Que cada equipo pueda responder por qué existe, hacia dónde va, con qué cuenta, y qué aprendió.**

Víctor no tiene que vender MaC. Los resultados lo hicieron por él.

La reunión termina con tres acuerdos que modifican la estrategia de NovaTech:

> `decisiones.md — Team building 2026`
>
> `2026-11-15` — **Validación técnica obligatoria**
> **Decisión:** Toda propuesta comercial que involucre integración pasa por revisión técnica de Operaciones. Sin excepción.
> **Ahora es una política organizacional, no del equipo de Víctor.**
>
> `2026-11-15` — **Modelo matrix formalizado**
> **Decisión:** Las asignaciones matrix entre áreas se formalizan con un proceso trimestral de negociación de FTEs, no ad-hoc.
> **Impacto:** Cambia cómo Operaciones, Desarrollo y Soporte planifican capacidad.
>
> `2026-11-15` — **Plan de documentación de conocimiento crítico**
> **Decisión:** Cada área identifica sus single points of failure y presenta un plan de mitigación en Q1 2027.
> **Impacto:** El problema de Rodrigo no es solo de Operaciones — Desarrollo tiene el mismo problema con su arquitecto principal.

Esto es **Actualizar**: cuando el aprendizaje acumulado de un área modifica la estrategia de la organización completa. Las tres decisiones nacieron en el vault de Operaciones, subieron a la gerencia a través de los reportes de Víctor, y ahora bajan como políticas organizacionales.

> [!IMPORTANT]
> **Actualizar en una organización mediana es un acto político, no solo documental.** Cuando Javiera actualiza su Identidad, solo ella cambia. Cuando Nexo actualiza, 6 personas se alinean. Cuando NovaTech actualiza, 80 personas cambian su forma de trabajar — y eso requiere poder, timing y datos. Víctor no propuso MaC en enero. Construyó evidencia durante un año, demostró resultados con su propio equipo, y cuando la organización estaba lista para escuchar, tenía los datos para respaldar todo lo que decía. El sistema no se impuso. Se contagió.

---

## Lo que Víctor tiene al mes 12

### 📂 Dos vaults conectados

**Vault personal (`MaC-Víctor/`):**

| Documento | Contenido | Frecuencia de cambio |
|---|---|---|
| `bitacora/semana-*.md` | Lo que Víctor hace como manager | Semanal |
| `decisiones.md` | Decisiones personales (qué escalar, qué no) | Cuando decide algo |
| `notas-andrea.md` | Preparación para reuniones con gerencia | Antes de cada reunión |
| `reflexiones.md` | Lo que piensa pero no dice en reunión | Cuando necesita pensar |

**Vault del equipo (`MaC-OPS/`):**

| Documento | Contenido | Frecuencia de cambio |
|---|---|---|
| `identidad.md` | Por qué existe Operaciones, qué no son | 1-2 veces al año |
| `direccion.md` | 4 objetivos semestrales con métricas | Revisión trimestral |
| `capacidad.md` | FTEs, restricciones, dependencias, matrix | Mensual |
| `plan-semanal.md` | Prioridades, responsables, bloqueos | Cada lunes (agente propone) |
| `log-semanal/*.md` | Qué hizo el equipo, sorpresas | Cada viernes (agente + equipo) |
| `decisiones.md` | Decisiones con trazabilidad | Cuando se decide algo |
| `politicas/*.md` | Matrix, deuda técnica, validación pre-venta | Cuando se consolida un patrón |
| `reportes/*.md` | Informes trimestrales para gerencia | Trimestral (agente genera borrador) |

### 🤖 Lo que hace el agente

| Función | Frecuencia | Fuentes | Tipo |
|---|---|---|---|
| Borrador de estado del área | Semanal | JIRA, Sheet FTEs, Calendar | Prótesis cognitiva |
| Propuesta de prioridades semanales | Lunes | `direccion.md`, JIRA, `capacidad.md` | Prótesis cognitiva |
| Alerta de tickets bloqueados >72h | Diaria | JIRA | Asesor de gestión |
| Alerta de capacidad (FTEs vs. compromisos) | Cuando detecta exceso | Sheet FTEs, JIRA, `capacidad.md` | Asesor de gestión |
| Detección de patrones en decisiones | Mensual | `decisiones.md` | Asesor de gestión |
| Revisión de coherencia (identidad vs. práctica) | Mensual | Todo el vault OPS | Asesor de gestión |
| Borrador de reporte trimestral | Trimestral | Todo el vault + JIRA + Sheets | Asesor de gestión |
| Cruce entre plan comercial y capacidad OPS | Cuando hay nuevo plan | Drive (compartido), `capacidad.md` | Consultor estratégico |
| Alerta de decisiones personales con impacto colectivo | Mensual | `MaC-Víctor/decisiones.md` vs `MaC-OPS/` | Consultor estratégico |

### ⏱️ Cuánto le cuesta

**A Víctor (como manager):**

| Actividad | Tiempo |
|---|---|
| Completar borrador del agente (estado semanal) | 10 min |
| Bitácora personal de gestión | 15 min |
| Reunión semanal con equipo (revisar plan + sorpresas) | 30 min |
| Revisión mensual de FTEs y decisiones | 45 min |
| Reporte trimestral (revisar borrador del agente) | 45 min |
| **Total semanal promedio** | **~60 min** |

**Al equipo (por persona):**

| Actividad | Tiempo |
|---|---|
| Participar en reunión semanal | 30 min |
| Anotar sorpresas de la semana | 5 min |
| **Total semanal por persona** | **~35 min** |

---

## Recapitulación: El camino de Víctor y NovaTech

```
FASE 1 (T1)   ──→  REGISTRAR (personal)     Víctor sintetiza JIRA + Sheets + correo en un solo lugar.
                    INTERPRETAR              Bitácora de gestión. Detecta patrones en su propio trabajo.
                    DECIDIR (personal)       Primera decisión: validación técnica pre-venta.

FASE 2 (T2)   ──→  AGENTE (prótesis)        Agente lee JIRA y Sheets, genera estado del área.
                    INTERPRETAR (agente)     El agente cruza decisiones con realidad y hace preguntas.

FASE 3 (T3)   ──→  REGISTRAR (equipo)       Log semanal colectivo con sorpresas.
                    PRIORIZAR                Plan semanal visible, con lo que entra y lo que no.
                    ENMARCAR                 Identidad del equipo. "¿Por qué existimos?"
                    DIMENSIONAR              Capacidad real: FTEs, matrix, dependencias.

FASE 4 (T4)   ──→  AGENTE (asesor)          Borrador de reporte trimestral. Preguntas para gerencia.
                    CONSOLIDAR               Decisiones repetidas → políticas (matrix, deuda técnica).

FASE 5 (T5-6) ──→  AGENTE (consultor)       Cruza plan comercial con capacidad OPS. Alerta estratégica.
                    ACTUALIZAR               El aprendizaje de OPS cambia la estrategia de NovaTech.
```

> [!IMPORTANT]
> **La estrategia brownfield: no reemplazar, leer.** Víctor no migró JIRA a Obsidian. No eliminó los Sheets. No canceló las reuniones existentes. Creó una capa de gestión que *lee* los sistemas existentes y les da coherencia vertical — la conexión entre lo que se hace abajo y por qué se hace arriba. El agente es el puente entre sistemas que no conversan. Y lo más importante: Víctor no pidió permiso para empezar. Empezó solo, con su vault personal, y dejó que los resultados hicieran la venta interna. Cuando Andrea pidió que el equipo hiciera lo mismo, no fue una imposición — fue una validación.

### Lo más importante

NovaTech sigue usando JIRA, Sheets y correo. Pero ahora hay alguien — un agente y un manager con un sistema — que lee todo eso junto y hace las preguntas que nadie tenía tiempo de hacer.

> **— Víctor, ¿qué cambiaste exactamente?** — le pregunta un par de otra empresa en un almuerzo.
> **— Nada, técnicamente. Seguimos usando las mismas herramientas. Lo que cambié fue la capa de encima: un lugar donde todo eso se junta, se cruza y se pregunta si tiene sentido. Y un agente que lo hace por mí cuando yo no puedo.**
> **— ¿Y la gerencia lo aceptó?**
> **— La gerencia no lo aceptó. La gerencia lo pidió. Pero eso pasó después de un año de datos.**