#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const SRC_DIR = path.join(process.cwd(), 'src');
const BASE = process.env.BASEURL || (process.env.GITHUB_REPOSITORY ? `/${process.env.GITHUB_REPOSITORY.split('/')[1]}` : '');

function readFileSafe(p) { try { return fs.readFileSync(p, 'utf8'); } catch { return ''; } }
function stripFrontMatter(md) {
  if (md.startsWith('---')) {
    const end = md.indexOf('\n---', 3);
    if (end !== -1) return md.slice(end + 4);
  }
  return md;
}
function mdToText(md) {
  return md
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/`[^`]*`/g, ' ')
    .replace(/^>\s?/gm, '')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[[^\]]*\]\([^)]*\)/g, (m)=>m.replace(/\[[^\]]*\]|\([^)]*\)/g,''))
    .replace(/[#*_>-]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}
function titleFromMd(md) {
  const m = md.match(/^#\s+(.+)$/m);
  return m ? m[1].trim() : '';
}

function build() {
  const items = [];
  if (!fs.existsSync(SRC_DIR)) return;
  const entries = fs.readdirSync(SRC_DIR, { withFileTypes: true });
  for (const e of entries) {
    if (!e.isDirectory()) continue;
    const indexPath = path.join(SRC_DIR, e.name, 'index.md');
    if (!fs.existsSync(indexPath)) continue;
    const mdRaw = readFileSafe(indexPath);
    const md = stripFrontMatter(mdRaw);
    const title = titleFromMd(md) || e.name;
    const content = mdToText(md).slice(0, 6000);
    const url = `${BASE}/src/${e.name}/`;
    items.push({ url, title, content });
  }
  const outDir = path.join(process.cwd(), 'assets');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);
  const out = path.join(outDir, 'search-index.json');
  fs.writeFileSync(out, JSON.stringify(items, null, 2), 'utf8');
  console.log(`Wrote ${items.length} items to ${out}`);
}

build();

