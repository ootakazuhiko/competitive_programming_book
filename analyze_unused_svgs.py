#!/usr/bin/env python3
"""
Script to identify unused SVG diagram files by comparing existing files
with references in markdown files.
"""

import os
import re
import glob
from pathlib import Path

def extract_svg_references_from_markdown(file_path):
    """Extract SVG references from a markdown file."""
    references = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Pattern to match SVG references
        pattern = r'!\[([^\]]*)\]\(\{\{ site\.baseurl \}\}/assets/diagrams/([^)]+\.svg)\)'
        matches = re.findall(pattern, content)
        
        for description, svg_path in matches:
            references.add(f"diagrams/{svg_path}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return references

def find_all_markdown_files(root_dir):
    """Find all markdown files in the project."""
    markdown_files = []
    for pattern in ['*.md', 'src/**/*.md']:
        markdown_files.extend(glob.glob(os.path.join(root_dir, pattern), recursive=True))
    return markdown_files

def find_existing_svg_files(assets_dir):
    """Find all existing SVG files in assets/diagrams."""
    svg_files = set()
    diagrams_dir = os.path.join(assets_dir, 'diagrams')
    if os.path.exists(diagrams_dir):
        for root, dirs, files in os.walk(diagrams_dir):
            for file in files:
                if file.endswith('.svg'):
                    rel_path = os.path.relpath(os.path.join(root, file), assets_dir)
                    svg_files.add(rel_path.replace('\\', '/'))  # Normalize path separators
    return svg_files

def categorize_unused_diagrams(unused_diagrams):
    """Categorize unused diagrams by chapter and type."""
    by_chapter = {}
    
    for diagram in unused_diagrams:
        # Extract chapter from path like "diagrams/chapterX/figure..."
        parts = diagram.split('/')
        if len(parts) >= 2:
            chapter = parts[1]
            if chapter not in by_chapter:
                by_chapter[chapter] = []
            by_chapter[chapter].append(diagram)
    
    return by_chapter

def main():
    root_dir = '/mnt/c/work/ClaudeCode/books/competitive_programming_book'
    assets_dir = os.path.join(root_dir, 'assets')
    
    print("=== Unused SVG Diagram Analysis ===\n")
    
    # Find all markdown files
    markdown_files = find_all_markdown_files(root_dir)
    print(f"Found {len(markdown_files)} markdown files")
    
    # Extract all SVG references
    all_referenced = set()
    for md_file in markdown_files:
        refs = extract_svg_references_from_markdown(md_file)
        all_referenced.update(refs)
    
    print(f"Found {len(all_referenced)} unique SVG references in markdown files")
    
    # Find existing SVG files
    existing_svgs = find_existing_svg_files(assets_dir)
    print(f"Found {len(existing_svgs)} existing SVG files")
    
    # Identify unused diagrams
    unused_diagrams = existing_svgs - all_referenced
    used_diagrams = existing_svgs & all_referenced
    
    print(f"\n=== RESULTS ===")
    print(f"Total SVG files: {len(existing_svgs)}")
    print(f"Referenced in markdown: {len(used_diagrams)}")
    print(f"Not referenced (unused): {len(unused_diagrams)}")
    
    if unused_diagrams:
        print(f"\n=== UNUSED DIAGRAMS BY CHAPTER ===")
        
        categorized = categorize_unused_diagrams(unused_diagrams)
        
        for chapter in sorted(categorized.keys()):
            diagrams = categorized[chapter]
            print(f"\n--- {chapter.upper()} ({len(diagrams)} unused diagrams) ---")
            for i, diagram in enumerate(sorted(diagrams), 1):
                filename = diagram.split('/')[-1]
                print(f"{i:2d}. {filename}")
    
    # Show statistics
    print(f"\n=== STATISTICS BY CHAPTER ===")
    chapter_stats = {}
    
    # Count used diagrams by chapter
    for diagram in used_diagrams:
        parts = diagram.split('/')
        if len(parts) >= 2:
            chapter = parts[1]
            if chapter not in chapter_stats:
                chapter_stats[chapter] = {'used': 0, 'unused': 0, 'total': 0}
            chapter_stats[chapter]['used'] += 1
    
    # Count unused diagrams by chapter
    for diagram in unused_diagrams:
        parts = diagram.split('/')
        if len(parts) >= 2:
            chapter = parts[1]
            if chapter not in chapter_stats:
                chapter_stats[chapter] = {'used': 0, 'unused': 0, 'total': 0}
            chapter_stats[chapter]['unused'] += 1
    
    # Calculate totals
    for chapter in chapter_stats:
        chapter_stats[chapter]['total'] = chapter_stats[chapter]['used'] + chapter_stats[chapter]['unused']
    
    print(f"{'Chapter':<10} {'Used':<6} {'Unused':<8} {'Total':<6} {'Usage %'}")
    print("-" * 45)
    
    for chapter in sorted(chapter_stats.keys()):
        stats = chapter_stats[chapter]
        usage_pct = (stats['used'] / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"{chapter:<10} {stats['used']:<6} {stats['unused']:<8} {stats['total']:<6} {usage_pct:.1f}%")

if __name__ == "__main__":
    main()