#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const os = require("os");

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

const SKILLS_SRC   = path.join(__dirname, "..", ".claude", "skills");
const COMMANDS_SRC = path.join(__dirname, "..", ".claude", "commands");

const YELLOW = "\x1b[33m";
const GREEN  = "\x1b[32m";
const RESET  = "\x1b[0m";
const BOLD   = "\x1b[1m";

const HELP = `
claude-code-starter-skills — install PM skills into Claude Code

Usage:
  npx github:hamzafarooq/claude-code-starter@main [options] [skill...]

Options:
  --global            Install into ~/.claude/skills/  (default)
  --local             Install into ./.claude/skills/  (current directory)
  --config-dir <dir>  Override the Claude config root (e.g. /path/to/.claude)
  --prefix <name>     Namespace installed skills as <name>-<skill>
  --list              Print available skills and exit
  --uninstall         Remove selected skills from the target directory
  --force             Overwrite existing skills without prompting
  --help              Show this message

Examples:
  npx github:hamzafarooq/claude-code-starter@main --global
  npx github:hamzafarooq/claude-code-starter@main --global okr-writer sprint-planner
  npx github:hamzafarooq/claude-code-starter@main --local --prefix pm
  npx github:hamzafarooq/claude-code-starter@main --list
  npx github:hamzafarooq/claude-code-starter@main --uninstall okr-writer

After install: restart Claude Code and run /help to see the new skills.
`.trim();

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function die(msg) {
  console.error(`\nError: ${msg}\n`);
  process.exit(1);
}

function readDescription(skillDir) {
  const skillFile = path.join(skillDir, "SKILL.md");
  try {
    const text = fs.readFileSync(skillFile, "utf8");
    const m = text.match(/^description:\s*(.+)$/m);
    return m ? m[1].trim() : "(no description)";
  } catch {
    return "(no description)";
  }
}

function availableSkills() {
  try {
    return fs
      .readdirSync(SKILLS_SRC, { withFileTypes: true })
      .filter((d) => d.isDirectory())
      .map((d) => d.name)
      .sort();
  } catch {
    die(`Skills directory not found: ${SKILLS_SRC}`);
  }
}

function copyRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyRecursive(s, d);
    } else {
      fs.copyFileSync(s, d);
    }
  }
}

function removeRecursive(dir) {
  if (fs.existsSync(dir)) {
    fs.rmSync(dir, { recursive: true, force: true });
  }
}

// ---------------------------------------------------------------------------
// Parse args
// ---------------------------------------------------------------------------

const args = process.argv.slice(2);

let isGlobal = false;
let isLocal = false;
let configDirOverride = null;
let prefix = null;
let doList = false;
let doUninstall = false;
let force = false;
let selectedSkills = [];

for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === "--global") {
    isGlobal = true;
  } else if (a === "--local") {
    isLocal = true;
  } else if (a === "--config-dir") {
    configDirOverride = args[++i];
    if (!configDirOverride) die("--config-dir requires a path argument");
  } else if (a === "--prefix") {
    prefix = args[++i];
    if (!prefix) die("--prefix requires a name argument");
  } else if (a === "--list") {
    doList = true;
  } else if (a === "--uninstall") {
    doUninstall = true;
  } else if (a === "--force") {
    force = true;
  } else if (a === "--help" || a === "-h") {
    console.log(HELP);
    process.exit(0);
  } else if (a.startsWith("--")) {
    die(`Unknown flag: ${a}\nRun with --help for usage.`);
  } else {
    selectedSkills.push(a);
  }
}

if (isGlobal && isLocal) die("Cannot use --global and --local together.");

// --list doesn't need a target dir
if (doList) {
  const skills = availableSkills();
  console.log(`\nAvailable skills (${skills.length}):\n`);
  for (const name of skills) {
    const desc = readDescription(path.join(SKILLS_SRC, name));
    console.log(`  ${name.padEnd(24)} ${desc}`);
  }
  console.log();
  process.exit(0);
}

// ---------------------------------------------------------------------------
// Resolve target directory
// ---------------------------------------------------------------------------

let claudeRoot;
if (configDirOverride) {
  claudeRoot = path.resolve(configDirOverride);
} else if (isLocal) {
  claudeRoot = path.join(process.cwd(), ".claude");
} else {
  // default: global
  claudeRoot = path.join(os.homedir(), ".claude");
}

const skillsTarget   = path.join(claudeRoot, "skills");
const commandsTarget = path.join(claudeRoot, "commands");

// ---------------------------------------------------------------------------
// Validate requested skills
// ---------------------------------------------------------------------------

const all = availableSkills();

if (selectedSkills.length === 0) {
  selectedSkills = all;
} else {
  const unknown = selectedSkills.filter((s) => !all.includes(s));
  if (unknown.length > 0) {
    die(
      `Unknown skill(s): ${unknown.join(", ")}\nRun with --list to see available skills.`
    );
  }
}

// ---------------------------------------------------------------------------
// Uninstall
// ---------------------------------------------------------------------------

if (doUninstall) {
  console.log(`\nUninstalling from: ${skillsTarget}\n`);
  let removed = 0;
  for (const name of selectedSkills) {
    const destName = prefix ? `${prefix}-${name}` : name;
    const dest = path.join(skillsTarget, destName);
    if (fs.existsSync(dest)) {
      removeRecursive(dest);
      console.log(`  removed  ${destName}`);
      removed++;
    } else {
      console.log(`  skipped  ${destName} (not found)`);
    }
    // Also remove the matching command file if present
    const commandDest = path.join(commandsTarget, `${destName}.md`);
    if (fs.existsSync(commandDest)) {
      fs.rmSync(commandDest);
    }
  }
  console.log(`\nDone. Removed ${removed} skill(s).\n`);
  process.exit(0);
}

// ---------------------------------------------------------------------------
// Install
// ---------------------------------------------------------------------------

fs.mkdirSync(skillsTarget, { recursive: true });

console.log(`\nInstalling ${selectedSkills.length} skill(s) into: ${skillsTarget}\n`);

let installed = 0;
let skipped = 0;

for (const name of selectedSkills) {
  const src = path.join(SKILLS_SRC, name);
  const destName = prefix ? `${prefix}-${name}` : name;
  const dest = path.join(skillsTarget, destName);

  if (fs.existsSync(dest) && !force) {
    console.log(`  ${YELLOW}${BOLD}⚠ SKIPPED${RESET}  ${BOLD}${destName}${RESET} ${YELLOW}already exists — run with --force to overwrite${RESET}`);
    skipped++;
    continue;
  }

  copyRecursive(src, dest);

  // Copy the matching command file if one exists
  const commandSrc  = path.join(COMMANDS_SRC, `${name}.md`);
  const commandDest = path.join(commandsTarget, `${destName}.md`);
  if (fs.existsSync(commandSrc) && (!fs.existsSync(commandDest) || force)) {
    fs.mkdirSync(commandsTarget, { recursive: true });
    fs.copyFileSync(commandSrc, commandDest);
  }

  console.log(`  ${GREEN}✔ installed${RESET}  ${destName}`);
  installed++;
}

const skipNote = skipped > 0
  ? `\n${YELLOW}${BOLD}⚠ ${skipped} skill(s) skipped (already exist). Re-run with --force to overwrite.${RESET}`
  : "";
console.log(`\n${GREEN}${BOLD}Done.${RESET} Installed ${installed} skill(s).${skipNote}\nRestart Claude Code and run /help to see your new skills.\n`);
