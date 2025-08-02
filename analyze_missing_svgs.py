#!/usr/bin/env python3
"""
Script to identify missing SVG diagram files by comparing markdown references 
with actual files in the assets/diagrams directory.
"""

import os
import re
import glob
from pathlib import Path

def extract_svg_references_from_markdown(file_path):
    """Extract SVG references from a markdown file."""
    references = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Pattern to match SVG references
        pattern = r'!\[([^\]]*)\]\(\{\{ site\.baseurl \}\}/assets/diagrams/([^)]+\.svg)\)'
        matches = re.findall(pattern, content)
        
        for description, svg_path in matches:
            references.append({
                'description': description,
                'svg_path': svg_path,
                'full_path': f"assets/diagrams/{svg_path}",
                'file': file_path
            })
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

def categorize_by_educational_importance(missing_diagrams):
    """Categorize missing diagrams by educational importance."""
    
    # High priority keywords (fundamental concepts)
    high_priority = [
        'algorithm', 'brute-force', 'problem-solving', 'implementation', 'debug',
        'input-output', 'data-structure', 'solution-design', 'testing',
        'reading-process', 'constraint', 'complexity'
    ]
    
    # Medium priority keywords
    medium_priority = [
        'contest', 'strategy', 'time-allocation', 'preparation', 'workflow',
        'step', 'pattern', 'guide', 'approach', 'technique'
    ]
    
    categorized = {
        'high': [],
        'medium': [],
        'low': []
    }
    
    for ref in missing_diagrams:
        svg_path_lower = ref['svg_path'].lower()
        description_lower = ref['description'].lower()
        
        combined_text = f"{svg_path_lower} {description_lower}"
        
        if any(keyword in combined_text for keyword in high_priority):
            categorized['high'].append(ref)
        elif any(keyword in combined_text for keyword in medium_priority):
            categorized['medium'].append(ref)
        else:
            categorized['low'].append(ref)
    
    return categorized

def main():
    root_dir = '/mnt/c/work/ClaudeCode/books/competitive_programming_book'
    assets_dir = os.path.join(root_dir, 'assets')
    
    print("=== SVG Diagram Analysis ===\n")
    
    # Find all markdown files
    markdown_files = find_all_markdown_files(root_dir)
    print(f"Found {len(markdown_files)} markdown files")
    
    # Extract all SVG references
    all_references = []
    for md_file in markdown_files:
        refs = extract_svg_references_from_markdown(md_file)
        all_references.extend(refs)
    
    print(f"Found {len(all_references)} SVG references in markdown files")
    
    # Find existing SVG files
    existing_svgs = find_existing_svg_files(assets_dir)
    print(f"Found {len(existing_svgs)} existing SVG files")
    
    # Identify missing diagrams
    missing_diagrams = []
    existing_diagrams = []
    
    for ref in all_references:
        # Normalize the path for comparison
        expected_path = f"diagrams/{ref['svg_path']}"
        if expected_path in existing_svgs:
            existing_diagrams.append(ref)
        else:
            missing_diagrams.append(ref)
    
    print(f"\n=== RESULTS ===")
    print(f"Total SVG references: {len(all_references)}")
    print(f"Existing diagrams: {len(existing_diagrams)}")
    print(f"Missing diagrams: {len(missing_diagrams)}")
    
    if missing_diagrams:
        print(f"\n=== MISSING DIAGRAMS BY PRIORITY ===")
        
        categorized = categorize_by_educational_importance(missing_diagrams)
        
        for priority in ['high', 'medium', 'low']:
            diagrams = categorized[priority]
            if diagrams:
                print(f"\n--- {priority.upper()} PRIORITY ({len(diagrams)} diagrams) ---")
                for i, ref in enumerate(diagrams, 1):
                    chapter = ref['svg_path'].split('/')[0] if '/' in ref['svg_path'] else 'unknown'
                    print(f"{i:2d}. {ref['svg_path']}")
                    print(f"    Description: {ref['description']}")
                    print(f"    Chapter: {chapter}")
                    print(f"    Referenced in: {os.path.basename(ref['file'])}")
                    print()
    
    # Show sample of existing and referenced files for verification
    print(f"\n=== VERIFICATION SAMPLES ===")
    print("Sample existing SVG files:")
    for svg in sorted(list(existing_svgs))[:5]:
        print(f"  {svg}")
    
    print("\nSample referenced files:")
    for ref in all_references[:5]:
        expected_path = f"diagrams/{ref['svg_path']}"
        exists = "✓" if expected_path in existing_svgs else "✗"
        print(f"  {exists} {expected_path}")
    
    print(f"\n=== SUMMARY ===")
    if missing_diagrams:
        categorized = categorize_by_educational_importance(missing_diagrams)
        high_count = len(categorized.get('high', []))
        medium_count = len(categorized.get('medium', []))
        low_count = len(categorized.get('low', []))
        
        print(f"High priority (algorithm/data structure concepts): {high_count}")
        print(f"Medium priority (strategy/workflow concepts): {medium_count}")
        print(f"Low priority (general/supplementary): {low_count}")
    else:
        print("All SVG diagrams referenced in markdown files already exist!")
    
    print(f"Total missing: {len(missing_diagrams)}")
    print(f"Total existing: {len(existing_diagrams)}")

if __name__ == "__main__":
    main()