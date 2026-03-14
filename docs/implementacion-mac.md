# Implementación de MaC

## El principio: de menos a más, siempre

MaC no se instala. Se cultiva. Empiezas con un archivo y una cadencia. Después agregas capas solo cuando la capa anterior genera una necesidad visible. Si empiezas con todo el sistema armado, vas a abandonarlo en un mes.

La regla es simple: **no agregues una capa hasta que duela no tenerla.**

---

## Greenfield vs. Brownfield

**Greenfield** — No tienes sistema de gestión. Empiezas de cero.
- Típico en: freelancers, startups, equipos nuevos.
- Ventaja: puedes diseñar desde el inicio.
- Riesgo: sobrediseñar antes de necesitarlo.

**Brownfield** — Ya tienes herramientas (JIRA, Sheets, correo, reuniones). MaC no las reemplaza.
- Típico en: equipos dentro de organizaciones, empresas con procesos existentes.
- Ventaja: no rompes lo que funciona.
- Estrategia: MaC se sienta **encima** de los sistemas existentes como una capa de gestión que los lee y les da coherencia vertical.

> En brownfield, el primer paso no es escribir: es **leer**. Sintetizar en un solo lugar lo que hoy está disperso en tickets, calendarios, correos y conversaciones informales. Esa síntesis ya genera visibilidad nueva.

---

## Ruta de implementación por escala

| Fase | 1 persona | 2–10 personas | Organización mediana |
|---|---|---|---|
| **Empieza con** | Log semanal personal | Log semanal colectivo | Síntesis de sistemas existentes |
| **Segundo paso** | Plan semanal | Plan semanal + dependencias | Log de gestión personal del líder |
| **Tercer paso** | Decisiones cuando hay sorpresa | Identidad del equipo | Plan visible para el equipo |
| **El sistema crece cuando** | No puedes decir que no | El equipo diverge sin criterio | Las áreas no conversan |
| **Herramientas** | Obsidian personal | Obsidian compartido + Git/Drive | Obsidian como capa + JIRA/ERP/Sheets |

---

## Los primeros 30 días

### Semana 1 — Solo registrar

Crea `log-semanal.md`. Cada viernes, anota:
- Qué hiciste (o qué hizo tu equipo).
- Qué fue distinto a lo esperado.

No necesitas más. El objetivo de la semana 1 es crear el hábito de cerrar la semana con 10 minutos de registro.

**En equipo:** Cada persona aporta 2-3 líneas. Alguien consolida.
**En organización:** Si ya tienes JIRA o similar, empieza leyendo esos sistemas y sintetizando en un solo documento lo que hoy está disperso.

### Semana 2 — Abrir con plan

Crea `plan-semanal.md`. Cada lunes:
- Qué entra esta semana.
- Qué queda fuera (y por qué).

**En equipo:** Agregar quién hace qué y qué depende de qué. Las dependencias entre personas son la parte que siempre se olvida y la que más daño causa.

### Semana 3 — Primera decisión

Cuando un resultado te sorprenda, anótalo en `decisiones.md`:
- Fecha.
- Qué decidiste.
- Por qué.
- Bajo qué condición revisarías esta decisión.

**En equipo:** Agregar quién decidió. La trazabilidad es lo que evita que alguien diga "yo nunca estuve de acuerdo" tres meses después.

### Semana 4 — Revisar

Relee los 3 archivos. ¿Ves un patrón? ¿Algo que se repite? ¿Algo que no esperabas?

Si sí: felicidades, el sistema está funcionando. La información que emerga te dirá qué capa agregar después (Identidad, Capacidad, Políticas).

Si no: sigue registrando. A veces toma dos meses ver el primer patrón.

---

## Evolución natural

No todas estas capas son necesarias para todas las escalas. Agrégalas en este orden general, pero solo cuando las necesites:

```
Mes 1–2    →  Registrar + Priorizar          Los cimientos: qué pasó y qué sigue.
Mes 3–4    →  Decidir + Descomponer          Las sorpresas generan decisiones. Las tareas se hacen explícitas.
Mes 4–6    →  Identidad + Capacidad          El "por qué" y el "con qué" aparecen cuando necesitas filtrar.
Mes 6–9    →  Consolidar                     Decisiones repetidas se convierten en políticas.
Mes 9–12   →  Actualizar                     Lo que aprendiste cambia quién eres o hacia dónde vas.
```

> Este orden no es rígido. En equipos, la Identidad puede aparecer antes (mes 2-3) si el equipo necesita alinear criterio para tomar decisiones juntos. En organizaciones, Registrar puede significar sintetizar sistemas existentes, no crear nuevos.

---

## Cadencias y rituales

Las cadencias son cuándo revisas qué. Los rituales son cómo lo haces. No necesitas todas desde el día uno.

| Cadencia | Qué revisas | Cuándo adoptar | Duración |
|---|---|---|---|
| **Semanal** | Log + Plan | Desde el día 1 | 15–30 min |
| **Mensual** | Decisiones + Políticas | Cuando acumules 4+ decisiones | 30–60 min |
| **Trimestral** | Dirección + Capacidad | Cuando tengas objetivos escritos | 60–90 min |
| **Anual** | Identidad | Cuando lleves 6+ meses con el sistema | Medio día |

**Ritual semanal — Cerrar y abrir ciclo:**
- Viernes: registrar qué pasó, qué fue diferente.
- Lunes: planificar qué entra, qué no.

**Ritual mensual — Revisión de aprendizaje:**
- ¿Hay decisiones cuya condición de revisión ya se cumplió?
- ¿Hay patrones que merecen convertirse en política?
- ¿Hay políticas que nadie aplica?

**Ritual trimestral — Revisión de estrategia:**
- ¿Los objetivos siguen siendo los correctos?
- ¿Los medios siguen siendo suficientes?
- ¿Hay que ajustar horizontes?

**Ritual anual — Revisión de identidad:**
- ¿Seguimos siendo lo que decimos ser?
- ¿Lo que aprendimos este año cambia quiénes somos?

---

## Documentos por capa

| Pilar | Capa | Documento típico | Contenido mínimo |
|---|---|---|---|
| **Estrategia** | Identidad | `identidad.md` | Por qué existimos, qué nos diferencia, qué NO somos |
| | Dirección | `direccion.md` | 3-5 objetivos con horizonte y responsable |
| | Capacidad | `capacidad.md` | Recursos reales, restricciones, dependencias externas |
| **Acción** | Planificación | `plan-semanal.md` | Qué entra, qué no, dependencias |
| | Tareas | JIRA, kanban, o lista en `.md` | Quién, qué, cuándo, estado |
| | Resultados | `log-semanal.md` | Qué se hizo, qué fue diferente, sorpresas |
| **Aprendizaje** | Decisiones | `decisiones.md` | Fecha, qué, por qué, condición de revisión |
| | Políticas | `politica-X.md` | Regla + origen (qué decisiones la generaron) |

---

## De manual a automatizado: el camino de los agentes

MaC está diseñado para funcionar sin automatización. Un humano puede ejecutar todos los procesos con archivos `.md` y disciplina semanal.

Pero cada proceso tiene partes tediosas y repetitivas que un agente IA puede absorber. Si tienes la capacidad técnica — o acceso a herramientas de agentes — puedes empezar a automatizar gradualmente, en el orden en que los procesos aparecen en tu implementación:

| Nivel | Qué automatiza | Ejemplo |
|---|---|---|
| **Prótesis cognitiva** | Lo tedioso: llenar borradores, cruzar fuentes, generar propuestas de plan | El agente lee tu calendar y JIRA, y te propone un borrador de log semanal. Tú completas lo que falta. |
| **Asesor de gestión** | Lo que requiere cruzar documentos: detectar patrones, alertar inconsistencias | El agente nota que llevas 3 decisiones similares y pregunta si quieres consolidar una política. |
| **Consultor estratégico** | Lo que requiere visión transversal: cruzar capacidad con plan comercial, detectar divergencias entre identidad y práctica | El agente cruza un plan nuevo con la capacidad actual y alerta que los números no cierran. |

> **No necesitas esperar.** Si ya practicas MaC manualmente y tienes acceso a un agente IA (Claude, Gemini, GPT con acceso a archivos), puedes empezar a delegarle las tareas de prótesis cognitiva desde hoy. El agente necesita leer tu vault — todo lo demás es configuración. Cada tarea que automatizas libera tiempo para la gestión que sí requiere juicio humano.

---

## Señales de que funciona

- Puedes responder "¿por qué estamos haciendo esto?" mirando un documento, no recordando una conversación.
- Las reuniones son más cortas porque la información ya está escrita.
- Dices que no a cosas que antes habrías aceptado — y puedes explicar por qué.
- Las sorpresas del log se convierten en decisiones, y las decisiones en políticas.
- La planificación se siente como revisar y ajustar, no como construir desde cero.

## Señales de que algo falla

- Escribes los documentos pero nadie los lee (ni tú).
- El plan del lunes no tiene relación con lo que realmente hiciste el viernes.
- Las decisiones se toman en conversaciones informales y nunca se registran.
- Todo aparece como "urgente" y nada se saca de la lista.
- El sistema siente como trabajo extra, no como ahorro de tiempo.

> Si el sistema se siente pesado, probablemente tienes más capas de las que necesitas. Vuelve a lo mínimo: log + plan + decisiones. Todo lo demás se agrega solo cuando duele no tenerlo.

---

## Historias de referencia

Tres organizaciones ficticias que ilustran cómo se implementa MaC a escalas distintas. Sus ejemplos cortos están integrados en el documento de [Procesos entre capas](procesos-mac.md); las historias completas están en el directorio `historias/`.

- **[Javiera](historias/javiera%20-%20relato%20de%20un%20independiente.md)** — Diseñadora freelance (1 persona). Empieza anotando qué pasó. Termina con un sistema que le permite decir que no.
- **[Nexo](historias/nexo%20-%20relato%20de%202%20a%2010%20personas.md)** — Consultora de 6 personas. El equipo promete más de lo que puede cumplir. MaC les da visibilidad de capacidad y criterio compartido.
- **[NovaTech](historias/novatech%20-%20relato%20empresa%20mediana.md)** — Empresa tech de 80 personas. Un manager implementa MaC como capa sobre JIRA y Sheets. Un año después, la gerencia lo pide para toda la empresa.

---

- → **[MaC para gente impaciente](mac-para-impacientes.md)** — El resumen de 2 minutos.
- → **[Método MaC](metodo-mac.md)** — La referencia completa: modelo, procesos, cadencias, preguntas.
- → **[Procesos entre capas](procesos-mac.md)** — Detalle de cada proceso con ejemplos por escala.
- → **[Preguntas que responde MaC](preguntas-mac.md)** — Catálogo completo de preguntas por capa.
