Registro semanal de actividad del proyecto. Cada archivo de bitácora representa una "semana" rítmica según [Cadencias](../estrategia/Cadencias.md).

## Convenciones
Seguir las reglas de markdown en el [playbook](../playbook/README.md).

## README de este directorio = Log del proyecto
Este README es la **memoria a largo plazo** del proyecto. Alguien que lo lea de reojo debería entender la evolución estratégica sin abrir los archivos semanales. El nivel de control granular (tareas operativas) reside en el log del proyecto o repositorio asociado y NO debe volcarse aquí.

- **Frecuencia de actualización:** Al iniciar y cerrar un bloque rítmico semanal.
- **Formato y Anidación:** Entradas agrupadas en orden cronológico descendente.
- Cada entrada se escribe con su título enlazado seguido de un guión y la etiqueta textual del periodo.
- Las viñetas anidadas documentan en **una sola línea** qué hito se cumplió o qué desviación hubo, agrupado por actividad/proyecto mayor (`- **Nombre Proyecto:** Resumen`).
- Tanto el agente como el usuario escriben en el registro. Nunca modificar el contenido estructural y manual del propio usuario, asume que sus ediciones dictan el estándar base.

- **Formato esperado (ejemplo literal):**
```markdown
- [2026-01-13](2026-01-13%20semana.md) - semana (en curso)
  - **Proyecto X:** Primer hito completado; agente estabilizado.
  
- [2026-01-06](2026-01-06%20semana.md) - semana
  - **Proyecto Y:** Decisión de usar tecnología Z.
```

## Plantilla de semana
Al empezar una nueva semana utilizar [`_template.md`](_template.md) y seguir las instrucciones en los comentarios inline. Verificar las fechas en [Cadencias](../estrategia/Cadencias.md) y en la secuencia lógica en [Log de actividad](actividad.md).

Al terminar la semana, seguir las instrucciones TL;DR en el `_template`

## Límites
| Nivel                 | Regla                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Hacer siempre**     | Verificar cuál es la semana en curso antes de escribir. Leer contexto en sub-archivos para deducir resúmenes válidos. |
| **Preguntar primero** | Antes de crear una nueva semana o cerrar la actual. Modificar el registro de semanas anteriores.                      |
| **Nunca hacer**       | Saturar el README con logs sueltos sub-atómicos. Borrar semanas anteriores.                                           |
| **Nunca hacer**       | Escribir semanas en el futuro |
