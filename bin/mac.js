#!/usr/bin/env node
/**
 * MaC CLI — Management as Code Engine
 * 
 * Uso:
 *   npx @pewma-ai/mac init [directorio] [--name nombre]
 *   npx @pewma-ai/mac update [directorio]
 *   npx @pewma-ai/mac version
 */

const fs = require('fs');
const path = require('path');

// ─── Helpers ─────────────────────────────────────────────────────────────────

const ENGINE_DIR = path.resolve(__dirname, '..', 'engine');
const VERSION = JSON.parse(fs.readFileSync(path.join(ENGINE_DIR, 'version.json'), 'utf-8'));

const COLORS = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  dim: '\x1b[2m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  cyan: '\x1b[36m',
  red: '\x1b[31m',
};

function log(msg) { console.log(msg); }
function success(msg) { log(`${COLORS.green}✓${COLORS.reset} ${msg}`); }
function warn(msg) { log(`${COLORS.yellow}⚠${COLORS.reset} ${msg}`); }
function info(msg) { log(`${COLORS.cyan}ℹ${COLORS.reset} ${msg}`); }
function error(msg) { log(`${COLORS.red}✗${COLORS.reset} ${msg}`); }

function today() {
  return new Date().toISOString().split('T')[0];
}

/**
 * Copia un directorio recursivamente.
 */
function copyDirSync(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirSync(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

/**
 * Reemplaza placeholders en un string.
 */
function replacePlaceholders(content, vars) {
  let result = content;
  for (const [key, value] of Object.entries(vars)) {
    result = result.replace(new RegExp(`\\{\\{${key}\\}\\}`, 'g'), value);
  }
  return result;
}

/**
 * Copia un template a destino, reemplazando placeholders.
 */
function copyTemplate(templateName, destPath, vars) {
  const templatePath = path.join(ENGINE_DIR, 'templates', templateName);
  if (!fs.existsSync(templatePath)) {
    warn(`Template no encontrado: ${templateName}`);
    return false;
  }
  const content = fs.readFileSync(templatePath, 'utf-8');
  const processed = replacePlaceholders(content, vars);
  
  const destDir = path.dirname(destPath);
  fs.mkdirSync(destDir, { recursive: true });
  fs.writeFileSync(destPath, processed, 'utf-8');
  return true;
}

/**
 * Copia un archivo del engine (agente/script) a destino sin transformación.
 */
function copyEngineFile(engineRelPath, destPath) {
  const srcPath = path.join(ENGINE_DIR, engineRelPath);
  if (!fs.existsSync(srcPath)) {
    warn(`Archivo del engine no encontrado: ${engineRelPath}`);
    return false;
  }
  const destDir = path.dirname(destPath);
  fs.mkdirSync(destDir, { recursive: true });
  fs.copyFileSync(srcPath, destPath);
  return true;
}

// ─── Comandos ────────────────────────────────────────────────────────────────

function printUsage() {
  log(`
${COLORS.bold}MaC — Management as Code Engine v${VERSION.version}${COLORS.reset}
${COLORS.dim}https://pewma-ai.github.io/mac/${COLORS.reset}

${COLORS.bold}Uso:${COLORS.reset}
  npx @pewma-ai/mac init [directorio] [--name nombre]   Crear un nuevo MaC
  npx @pewma-ai/mac update [directorio]                  Actualizar .mac/
  npx @pewma-ai/mac version                              Mostrar versión

${COLORS.bold}Ejemplos:${COLORS.reset}
  npx @pewma-ai/mac init .
  npx @pewma-ai/mac init ./mac-jpgil --name "JP Gil"
  npx @pewma-ai/mac update .
`);
}

function cmdVersion() {
  log(`MaC Engine v${VERSION.version} (${VERSION.date})`);
  log(VERSION.description);
}

function cmdInit(targetDir, projectName) {
  const absTarget = path.resolve(targetDir);
  
  log('');
  log(`${COLORS.bold}MaC — Inicializando nuevo proyecto${COLORS.reset}`);
  log(`${COLORS.dim}─────────────────────────────────────${COLORS.reset}`);
  info(`Directorio: ${absTarget}`);
  info(`Proyecto: ${projectName}`);
  info(`Engine: v${VERSION.version}`);
  log('');

  // Verificar si ya existe un .mac/
  const macDir = path.join(absTarget, '.mac');
  if (fs.existsSync(macDir)) {
    error(`.mac/ ya existe en ${absTarget}. Usa 'update' para actualizar.`);
    process.exit(1);
  }

  // Variables para templates
  const vars = {
    PROJECT_NAME: projectName,
    DATE: today(),
    ENGINE_VERSION: VERSION.version,
  };

  // 1. Copiar engine → .mac/
  info('Instalando engine en .mac/ ...');
  copyDirSync(ENGINE_DIR, macDir);
  success('.mac/ instalado');

  // 2. Generar estructura del usuario desde templates
  const created = [];

  // Archivos raíz
  const rootFiles = [
    { template: 'AGENTS.md', dest: 'AGENTS.md' },
    { template: 'README.md', dest: 'README.md' },
    { template: 'Indice.md', dest: 'Indice.md' },
  ];

  for (const { template, dest } of rootFiles) {
    const destPath = path.join(absTarget, dest);
    if (!fs.existsSync(destPath)) {
      copyTemplate(template, destPath, vars);
      created.push(dest);
    } else {
      warn(`${dest} ya existe, no se sobreescribe`);
    }
  }

  // Estrategia
  const estrategia = ['Identidad.md', 'Direccion.md', 'Capacidad.md', 'Cadencias.md'];
  for (const file of estrategia) {
    const destPath = path.join(absTarget, 'estrategia', file);
    if (!fs.existsSync(destPath)) {
      copyTemplate(file, destPath, vars);
      created.push(`estrategia/${file}`);
    }
  }

  // Actividad
  const actividadDir = path.join(absTarget, 'actividad');
  fs.mkdirSync(actividadDir, { recursive: true });

  const actAgents = path.join(actividadDir, 'AGENTS.md');
  if (!fs.existsSync(actAgents)) {
    copyTemplate('actividad-AGENTS.md', actAgents, vars);
    created.push('actividad/AGENTS.md');
  }

  const actTemplate = path.join(actividadDir, '_template.md');
  if (!fs.existsSync(actTemplate)) {
    copyTemplate('semana.md', actTemplate, vars);
    created.push('actividad/_template.md');
  }

  const actLog = path.join(actividadDir, 'actividad.md');
  if (!fs.existsSync(actLog)) {
    copyTemplate('actividad.md', actLog, vars);
    created.push('actividad/actividad.md');
  }

  // Proyectos
  const proyectosDir = path.join(absTarget, 'proyectos');
  fs.mkdirSync(proyectosDir, { recursive: true });

  const proyAgents = path.join(proyectosDir, 'AGENTS.md');
  if (!fs.existsSync(proyAgents)) {
    copyTemplate('proyectos-AGENTS.md', proyAgents, vars);
    created.push('proyectos/AGENTS.md');
  }

  const proyIndex = path.join(proyectosDir, 'proyectos.md');
  if (!fs.existsSync(proyIndex)) {
    copyTemplate('proyectos.md', proyIndex, vars);
    created.push('proyectos/proyectos.md');
  }

  // Procesos — copiar agentes del engine como archivos de usuario
  const procesosDir = path.join(absTarget, 'procesos');
  fs.mkdirSync(procesosDir, { recursive: true });

  const agentFiles = [
    { src: 'agentes/amigo.MaC.md', dest: 'procesos/amigo.MaC.md' },
    { src: 'agentes/readme.MaC.md', dest: 'procesos/readme.MaC.md' },
    { src: 'agentes/propagate-logs.MaC.md', dest: 'procesos/propagate-logs.MaC.md' },
    { src: 'agentes/jntr.obsidian.links.md', dest: 'procesos/jntr.obsidian.links.md' },
  ];
  for (const { src, dest } of agentFiles) {
    const destPath = path.join(absTarget, dest);
    if (!fs.existsSync(destPath)) {
      copyEngineFile(src, destPath);
      created.push(dest);
    }
  }

  const procIndex = path.join(procesosDir, 'procesos.md');
  if (!fs.existsSync(procIndex)) {
    copyTemplate('procesos.md', procIndex, vars);
    created.push('procesos/procesos.md');
  }

  // Scripts — copiar janitors
  const scriptsDir = path.join(absTarget, 'scripts');
  fs.mkdirSync(scriptsDir, { recursive: true });

  const scriptFiles = [
    'scripts/jntr.obsidian-links.py',
    'scripts/jntr.find-tags.py',
    'scripts/jntr.check-md-broken-links.py',
    'scripts/README.md',
  ];
  for (const src of scriptFiles) {
    const filename = path.basename(src);
    const destPath = path.join(scriptsDir, filename);
    if (!fs.existsSync(destPath)) {
      copyEngineFile(src, destPath);
      created.push(`scripts/${filename}`);
    }
  }

  // Playbook
  const playbookDir = path.join(absTarget, 'playbook');
  const playbookReadme = path.join(playbookDir, 'README.md');
  if (!fs.existsSync(playbookReadme)) {
    copyTemplate('playbook-README.md', playbookReadme, vars);
    created.push('playbook/README.md');
  }

  // Notas
  const notasDir = path.join(absTarget, 'notas');
  const notasIndex = path.join(notasDir, 'notas.md');
  if (!fs.existsSync(notasIndex)) {
    copyTemplate('notas.md', notasIndex, vars);
    created.push('notas/notas.md');
  }

  // 3. Crear/actualizar .gitignore
  const gitignorePath = path.join(absTarget, '.gitignore');
  let gitignoreContent = '';
  if (fs.existsSync(gitignorePath)) {
    gitignoreContent = fs.readFileSync(gitignorePath, 'utf-8');
  }
  if (!gitignoreContent.includes('.mac/')) {
    const separator = gitignoreContent.endsWith('\n') || gitignoreContent === '' ? '' : '\n';
    gitignoreContent += `${separator}# MaC Engine (distribuido, no versionado)\n.mac/\n`;
    fs.writeFileSync(gitignorePath, gitignoreContent, 'utf-8');
    created.push('.gitignore (actualizado)');
  }

  // 4. Resumen
  log('');
  log(`${COLORS.bold}${COLORS.green}¡MaC inicializado!${COLORS.reset}`);
  log(`${COLORS.dim}─────────────────────────────────────${COLORS.reset}`);
  log('');
  log(`${COLORS.bold}Archivos creados:${COLORS.reset}`);
  for (const f of created) {
    log(`  ${COLORS.green}+${COLORS.reset} ${f}`);
  }
  log('');
  log(`${COLORS.bold}Estructura generada:${COLORS.reset}`);
  log(`  ${absTarget}/`);
  log(`  ├── .mac/              ${COLORS.dim}← engine (en .gitignore)${COLORS.reset}`);
  log(`  ├── AGENTS.md          ${COLORS.dim}← reglas del agente${COLORS.reset}`);
  log(`  ├── README.md          ${COLORS.dim}← panel de control${COLORS.reset}`);
  log(`  ├── Indice.md          ${COLORS.dim}← mapeo de capas MaC${COLORS.reset}`);
  log(`  ├── estrategia/        ${COLORS.dim}← identidad, dirección, capacidad, cadencias${COLORS.reset}`);
  log(`  ├── actividad/         ${COLORS.dim}← bitácoras semanales${COLORS.reset}`);
  log(`  ├── proyectos/         ${COLORS.dim}← gestión de proyectos${COLORS.reset}`);
  log(`  ├── procesos/          ${COLORS.dim}← agentes y procesos MaC${COLORS.reset}`);
  log(`  ├── scripts/           ${COLORS.dim}← janitors de mantenimiento${COLORS.reset}`);
  log(`  ├── playbook/          ${COLORS.dim}← buenas prácticas${COLORS.reset}`);
  log(`  └── notas/             ${COLORS.dim}← second brain${COLORS.reset}`);
  log('');
  log(`${COLORS.bold}Siguiente paso:${COLORS.reset} Abre ${COLORS.cyan}estrategia/Identidad.md${COLORS.reset} y escribe quién eres.`);
  log('');
}

function cmdUpdate(targetDir) {
  const absTarget = path.resolve(targetDir);
  const macDir = path.join(absTarget, '.mac');

  log('');
  log(`${COLORS.bold}MaC — Actualizando engine${COLORS.reset}`);
  log(`${COLORS.dim}─────────────────────────────────────${COLORS.reset}`);

  if (!fs.existsSync(macDir)) {
    error(`No se encontró .mac/ en ${absTarget}. Usa 'init' primero.`);
    process.exit(1);
  }

  // Leer versión actual
  const currentVersionPath = path.join(macDir, 'version.json');
  let currentVersion = { version: 'desconocida' };
  if (fs.existsSync(currentVersionPath)) {
    currentVersion = JSON.parse(fs.readFileSync(currentVersionPath, 'utf-8'));
  }

  info(`Versión actual: ${currentVersion.version}`);
  info(`Versión nueva:  ${VERSION.version}`);

  if (currentVersion.version === VERSION.version) {
    success('Ya tienes la versión más reciente.');
    return;
  }

  // Borrar .mac/ viejo y copiar el nuevo
  fs.rmSync(macDir, { recursive: true, force: true });
  copyDirSync(ENGINE_DIR, macDir);

  success(`Engine actualizado de ${currentVersion.version} a ${VERSION.version}`);
  log('');
  info('Los archivos del usuario no fueron modificados.');
  info('Revisa el changelog para ver si hay templates nuevos que quieras adoptar.');
  log('');
}

// ─── Main ────────────────────────────────────────────────────────────────────

function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args[0] === '--help' || args[0] === '-h') {
    printUsage();
    process.exit(0);
  }

  const command = args[0];

  switch (command) {
    case 'version':
    case '--version':
    case '-v':
      cmdVersion();
      break;

    case 'init': {
      let targetDir = '.';
      let projectName = null;

      for (let i = 1; i < args.length; i++) {
        if (args[i] === '--name' && args[i + 1]) {
          projectName = args[i + 1];
          i++;
        } else if (!args[i].startsWith('-')) {
          targetDir = args[i];
        }
      }

      // Si no se dio nombre, inferir del directorio
      if (!projectName) {
        const dirName = path.basename(path.resolve(targetDir));
        projectName = dirName;
      }

      cmdInit(targetDir, projectName);
      break;
    }

    case 'update': {
      const targetDir = args[1] || '.';
      cmdUpdate(targetDir);
      break;
    }

    default:
      error(`Comando desconocido: ${command}`);
      printUsage();
      process.exit(1);
  }
}

main();
