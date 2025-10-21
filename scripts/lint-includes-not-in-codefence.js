#!/usr/bin/env node
// Detect Jekyll include tags used inside fenced code blocks in Markdown.
// This helps avoid panels/figures being wrapped in <pre> due to stray ``` fences.
//
// Scope: scans markdown files under src/ and the top-level index.md.
// Exits with non-zero status if any violation is found.

const fs = require('fs');
const path = require('path');

// Precompile regex patterns once
const JEKYLL_INCLUDE_RE = /\{\%\s*include\b[^%]*\%\}/; // Jekyll include tag
const FENCE_START_RE = /^\s*```/; // allow indented fenced code blocks

/**
 * Recursively collect markdown files under dir.
 */
function collectMdFiles(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...collectMdFiles(p));
    else if (entry.isFile() && p.endsWith('.md')) out.push(p);
  }
  return out;
}

function scanFile(file) {
  const text = fs.readFileSync(file, 'utf8');
  const lines = text.split(/\r?\n/);
  let inFence = false;
  let fenceStart = 0;
  const problems = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // Start/end of fenced code block (```)
    if (FENCE_START_RE.test(line)) {
      inFence = !inFence;
      fenceStart = inFence ? (i + 1) : 0;
      continue;
    }
    if (inFence && JEKYLL_INCLUDE_RE.test(line)) {
      problems.push({ line: i + 1, fenceStart, text: line.trim() });
    }
  }
  return problems;
}

function main() {
  const root = process.cwd();
  const targets = [];
  const srcDir = path.join(root, 'src');
  if (fs.existsSync(srcDir)) targets.push(...collectMdFiles(srcDir));
  const indexMd = path.join(root, 'index.md');
  if (fs.existsSync(indexMd)) targets.push(indexMd);

  let total = 0;
  const report = [];
  for (const f of targets) {
    const issues = scanFile(f);
    if (issues.length) {
      report.push({ file: f, issues });
      total += issues.length;
    }
  }

  if (total === 0) {
    console.log('include-guard: OK (no include tags inside code fences)');
    return;
  }

  console.error(`include-guard: found ${total} violation(s):`);
  for (const r of report) {
    for (const p of r.issues) {
      console.error(`- ${r.file}:${p.line} (fence starts at line ${p.fenceStart}) -> ${p.text}`);
    }
  }
  process.exit(1);
}

main();
