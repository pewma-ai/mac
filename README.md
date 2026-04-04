# Management as Code (MaC)

MaC es un paradigma de gestión basado en documentos y procesos que articula el ciclo Acción → Aprendizaje siguiendo una estrategia común.

🌐 https://pewma-ai.github.io/mac/

## Instalación

```bash
npx @pewma-ai/mac init ./mac-mi-proyecto --name "Mi Proyecto"
```

Esto genera un repositorio MaC completo con `.mac/` (engine), estrategia, actividad, proyectos, procesos, scripts y playbook. [Más detalles →](docs/implementacion-mac.md)

### Actualizar el engine

```bash
npx @pewma-ai/mac update .
```

### Directamente desde GitHub (sin npm)

```bash
npx github:pewma-ai/mac#v2 init ./mac-mi-proyecto --name "Mi Proyecto"
```

## Estructura del engine

```
engine/
├── agentes/    → plantillas de agentes MaC (amigo, readme, destilado, janitor)
├── scripts/    → janitors de mantenimiento (links, tags, broken links)
├── templates/  → scaffolds para cada archivo del usuario
├── metodo/     → documentación completa del método MaC
└── version.json
```

```
bin/
└── mac.js      → CLI: init, update, version
```

## Desarrollo

> [!NOTE]
> **Este repositorio se gestiona con MaC.** El directorio [`MaC/`](./MaC/) contiene el ritual de sesión, el log y el roadmap que se usaron para construir este proyecto.

* [`AGENTS.md`](AGENTS.md) — Instrucciones para agentes IA: ritual obligatorio, tipos de trabajo y límites.
* [`playbook/`](playbook/README.md) — Guías operativas del proyecto: convenciones de git, documentación, Docsify y configuración de agentes.
* [`MaC/`](MaC/README.md) — Gestión del proyecto: sesiones de trabajo, log histórico y roadmap.

## Autor

**Juan Pablo Gil**  
[![Email](https://img.shields.io/badge/Email-juanpablogil%40gmail.com-blue?style=flat-square&logo=gmail)](mailto:juanpablogil@gmail.com)

## Acerca de PEWMA.AI

Este proyecto está respaldado por **PEWMA.AI**, un laboratorio de innovación dedicado a la creación de herramientas y soluciones basadas en inteligencia artificial para el Sur Global.

🌐 [pewma.ai](https://pewma.ai)

## Licencia

Este proyecto está licenciado bajo la licencia **Apache 2.0**. Ver el archivo [LICENSE](LICENSE) para más detalles.
