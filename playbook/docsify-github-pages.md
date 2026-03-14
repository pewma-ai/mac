# Publicar `/docs/` como sitio Docsify en GitHub Pages

> **Para humanos y agentes IA.**  
> Este documento describe el estado objetivo del repositorio para publicar la carpeta `/docs/` como un sitio de documentación navegable usando Docsify, sin proceso de build, con publicación automática en cada `git push`.

---

## Estado objetivo

Cuando este setup está completo, el repositorio debe tener:

```
/docs/
  index.html        ← motor Docsify (único archivo de infraestructura)
  _sidebar.md       ← navegación lateral (editable como cualquier MD)
  *.md              ← contenido, sin modificar
```

Y en GitHub → Settings → Pages:
- **Source**: `Deploy from a branch`
- **Branch**: `main` / **Folder**: `/docs`

Resultado: cada `git push` publica en `https://<org>.github.io/<repo>` en ~30 segundos. Sin Actions, sin build, sin dependencias locales.

---

## Verificación: checklist para agentes IA

Un agente puede verificar si el repo está correctamente configurado comprobando:

- [ ] Existe `docs/index.html` con `window.$docsify` definido
- [ ] Existe `docs/_sidebar.md` con al menos una entrada
- [ ] `docs/index.html` carga Docsify desde CDN (no dependencias locales)
- [ ] Los archivos `.md` referenciados en `_sidebar.md` existen en las rutas indicadas
- [ ] GitHub Pages está configurado en branch `main`, carpeta `/docs`

Si falta alguno de estos puntos, el sitio no publicará correctamente.

---

## Archivo 1: `docs/index.html`

Este es el único archivo que no es Markdown. Contiene el motor Docsify y el CSS personalizado.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>MaC — Management as Code</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- FUENTES: cambiar aquí para personalizar tipografía -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

  <style>
    /* ============================================================
       VARIABLES DE TEMA — editar esta sección para personalizar
       Docsify-themeable expone estas variables CSS.
       Referencia completa: https://jhildenbiddle.github.io/docsify-themeable
    ============================================================ */
    :root {
      /* Tipografía */
      --base-font-family: 'Inter', -apple-system, sans-serif;
      --base-font-size: 16px;
      --base-line-height: 1.75;

      /* Colores base */
      --base-color: #d4d4d4;               /* texto principal */
      --base-background-color: #0f0f0f;    /* fondo de contenido */
      --heading-color: #f0f0f0;            /* títulos */
      --heading-font-weight: 500;

      /* Links */
      --link-color: #a78bfa;               /* color de acento — cambiar aquí */
      --link-color--hover: #c4b5fd;
      --link-text-decoration: none;

      /* Sidebar */
      --sidebar-background: #141414;
      --sidebar-border-color: #262626;
      --sidebar-width: 260px;
      --sidebar-color: #a3a3a3;
      --sidebar-name-color: #f0f0f0;
      --sidebar-nav-link-color: #a3a3a3;
      --sidebar-nav-link-color--active: #f0f0f0;
      --sidebar-nav-link-font-weight--active: 500;
      --sidebar-nav-link-border-color--active: #a78bfa; /* acento activo */

      /* Código */
      --code-font-family: 'JetBrains Mono', 'Fira Code', monospace;
      --code-background: #1a1a1a;
      --code-color: #c4b5fd;
      --code-block-border-radius: 6px;

      /* Blockquotes */
      --blockquote-border-color: #a78bfa;
      --blockquote-color: #a3a3a3;

      /* Tablas */
      --table-row-odd-background: #1a1a1a;
      --table-row-even-background: #141414;

      /* Búsqueda */
      --search-input-background-color: #1a1a1a;
      --search-input-border-color: #333;
      --search-input-color: #d4d4d4;

      /* Separadores */
      --hr-border: 1px solid #262626;
    }

    /* ============================================================
       CSS ADICIONAL — ajustes fuera del sistema de variables
    ============================================================ */
    body {
      font-feature-settings: 'kern', 'liga';
    }

    .app-name-link {
      font-weight: 600;
      letter-spacing: 0.02em;
    }

    h1, h2, h3 {
      letter-spacing: -0.01em;
    }

    /* Responsive */
    @media (max-width: 768px) {
      :root {
        --base-font-size: 15px;
        --sidebar-width: 240px;
      }
    }
  </style>
</head>
<body>
  <div id="app"></div>

  <script>
    /* ============================================================
       CONFIGURACIÓN DOCSIFY — opciones principales
       Referencia: https://docsify.js.org/#/configuration
    ============================================================ */
    window.$docsify = {
      name: 'MaC',                              // nombre en sidebar
      nameLink: '/',                             // link del nombre
      repo: 'https://github.com/pewma-ai/mac',  // ícono GitHub arriba derecha
      loadSidebar: true,                         // usa _sidebar.md
      subMaxLevel: 2,                            // niveles de TOC en sidebar
      homepage: 'mac-para-impacientes.md',       // página de entrada
      themeColor: '#a78bfa',                     // color de acento (progress bar)
      notFoundPage: true,                        // página 404 automática
      search: {
        placeholder: 'Buscar...',
        noData: 'Sin resultados.',
      },
    }
  </script>

  <!-- Motor de temas (debe ir ANTES de docsify.min.js) -->
  <script src="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/js/docsify-themeable.min.js"></script>
  <!-- Motor Docsify -->
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/docsify.min.js"></script>
  <!-- Plugin de búsqueda -->
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
</body>
</html>
```

---

## Archivo 2: `docs/_sidebar.md`

Este archivo define la navegación lateral. Se edita como cualquier Markdown desde Obsidian u otro editor.

```markdown
* **Documentos**
  * [Para impacientes](mac-para-impacientes.md)
  * [Implementación](implementacion-mac.md)
  * [Método MaC](metodo-mac.md)
  * [Procesos](procesos-mac.md)
  * [Preguntas](preguntas-mac.md)

* **Historias**
  * [Javiera](../historias/javiera%20-%20relato%20de%20un%20independiente.md)
  * [Nexo](../historias/nexo%20-%20relato%20de%202%20a%2010%20personas.md)
  * [NovaTech](../historias/novatech%20-%20relato%20empresa%20mediana.md)
```

> **Nota sobre espacios en nombres de archivo:** Docsify puede fallar con espacios en rutas. Usar `%20` en el `_sidebar.md` es más seguro, aunque los archivos físicos mantengan sus nombres originales.

---

## Configurar GitHub Pages (una sola vez)

1. Ir a **Settings** del repositorio
2. Sección **Pages** en el menú lateral
3. En **Source** seleccionar: `Deploy from a branch`
4. **Branch**: `main` / **Folder**: `/docs`
5. Click en **Save**

Desde ese momento, cada `git push` a `main` publica automáticamente. No se requiere ningún workflow de GitHub Actions.

La URL resultante será: `https://pewma-ai.github.io/mac`

---

## Flujo completo

```
Obsidian
   ↓ edita *.md en /docs/ o /historias/
git push origin main
   ↓ ~30 segundos
GitHub Pages sirve /docs/ como sitio Docsify
   ↓ disponible en
pewma-ai.github.io/mac

Los archivos MD siguen accesibles directamente:
raw.githubusercontent.com/pewma-ai/mac/main/docs/metodo-mac.md
```

Docsify es una capa de lectura sobre los archivos originales. No los modifica ni compila. El repositorio sigue siendo la fuente de verdad.

---

## Personalización CSS: guía de referencia

### Cambiar color de acento

Buscar y reemplazar las tres ocurrencias de `#a78bfa` en `index.html`:

```css
--link-color: #TU_COLOR;
--sidebar-nav-link-border-color--active: #TU_COLOR;
--blockquote-border-color: #TU_COLOR;
```

Y en la configuración JS:

```js
themeColor: '#TU_COLOR',
```

### Cambiar a tema claro

Reemplazar las variables de color base:

```css
:root {
  --base-color: #1a1a1a;
  --base-background-color: #ffffff;
  --heading-color: #111111;
  --sidebar-background: #f5f5f5;
  --sidebar-border-color: #e5e5e5;
  --sidebar-color: #555555;
  --code-background: #f0f0f0;
  --table-row-odd-background: #f9f9f9;
  --table-row-even-background: #ffffff;
}
```

### Cambiar tipografía

Reemplazar el `<link>` de Google Fonts y la variable:

```html
<!-- Ejemplo con otra fuente -->
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
```

```css
--base-font-family: 'DM Sans', sans-serif;
```

### Variables completas disponibles

Referencia oficial de todas las variables del sistema de temas:  
`https://jhildenbiddle.github.io/docsify-themeable/#/customization`

---

## Plugins adicionales disponibles

Agregar después de `search.min.js` según necesidad:

```html
<!-- Zoom en imágenes al hacer click -->
<script src="https://cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>

<!-- Copiar código con un click -->
<script src="https://cdn.jsdelivr.net/npm/docsify-copy-code@2/dist/docsify-copy-code.min.js"></script>

<!-- Paginación anterior/siguiente -->
<script src="https://cdn.jsdelivr.net/npm/docsify-pagination/dist/docsify-pagination.min.js"></script>

<!-- Tabs dentro de documentos -->
<script src="https://cdn.jsdelivr.net/npm/docsify-tabs@1/dist/docsify-tabs.min.js"></script>
```

---

## Limitaciones conocidas

- **SEO**: Docsify renderiza en el browser (JS requerido). Google indexa eventualmente, pero de forma lenta. No usar si el posicionamiento en buscadores es prioritario.
- **Sin JS**: el sitio no funciona sin JavaScript habilitado.
- **Espacios en rutas**: los nombres de archivo con espacios requieren `%20` en los links del `_sidebar.md`.
- **Archivos fuera de `/docs/`**: Docsify puede referenciarlos con rutas relativas (`../historias/`), pero GitHub Pages solo sirve desde `/docs/`. Los archivos sí son accesibles, pero Docsify los carga vía fetch relativo — funciona si están en el mismo repositorio.
