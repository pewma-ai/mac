# Proceso: Mantener README.md principal

> **Audiencia:** Agente IA. Instrucciones para mantener [README](../README.md) actualizado. Este archivo es el **panel de control** del proyecto: quien lo lea (humano o agente) debe saber en segundos qué está pasando y dónde ir.

---
## Registro
- No registrar el cambio en ningún log, sesión o archivo de registro.
## Estructura del README

El README.md tiene cuatro bloques, siempre en este orden:

### 1. Encabezado
```markdown
# MaC de <NOMBRE DEL PROYECTO>
```
- `<NOMBRE DEL PROYECTO>` se toma del `README.md` raíz del repositorio.

### 2. Estado Actual (callouts)
Tres bloques de tipo callout, inmediatamente después del encabezado:

```markdown
## Estado

> [!summary] [Semana en curso](<enlace al archivo de la semana en curso>)
> 1. ...

> [!Attention] 💡 Radar MaC
> ...

> [!tip] Tip <FECHA>
> ...

```

**Reglas:**
- Para la semana en curso, escribe de uno a tres bullets muy concisos de lo más relevante recientemente para que el usuario tenga contexto y pueda decidir cómo continuar las siguientes horas.
- Radar: Cuando el radar de contexto quiera informar algo relevante al usuario, escribe en este README el callout necesario. Si el radar detecta algo más prioritario, reemplaza el contenido. Mantén solo un ítem. 
- Tip diario: Utiliza la información de la semana en curso y la anterior, más alguna buenas prácticas del método MaC, y escribe un tip personalizado para el usuario que ayude a destrabar su trabajo. Anota la fecha a la derecha.
- Si el tip diario está vacío, agrega uno.

### 3. Últimas semanas
Sección final con "Últimas semanas" mantiene el enlace a las últimas 4 semanas, especificando la semana en curso.

### 4. Estrategia
No cambia.

### 5. Acerca de
No cambia.

## Principio rector
**Brevedad y precisión.** Este archivo se lee de un vistazo. No agregar prosa, explicaciones largas ni secciones adicionales.
