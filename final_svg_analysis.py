#!/usr/bin/env python3
"""
Comprehensive analysis to identify missing SVG diagrams across all locations.
"""

import os
import re
import glob
from pathlib import Path

def extract_all_svg_references_from_markdown(file_path):
    """Extract all SVG references from a markdown file."""
    references = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Pattern 1: Jekyll style with site.baseurl and assets/diagrams
        pattern1 = r'!\[([^\]]*)\]\(\{\{ site\.baseurl \}\}/assets/diagrams/([^)]+\.svg)\)'
        matches1 = re.findall(pattern1, content)
        for description, svg_path in matches1:
            references.append({
                'description': description,
                'svg_path': svg_path,
                'expected_location': f"assets/diagrams/{svg_path}",
                'file': file_path,
                'type': 'assets_diagrams'
            })
        
        # Pattern 2: Jekyll style with site.baseurl and images
        pattern2 = r'!\[([^\]]*)\]\(\{\{ site\.baseurl \}\}/images/([^)]+\.svg)\)'
        matches2 = re.findall(pattern2, content)
        for description, svg_path in matches2:
            references.append({
                'description': description,
                'svg_path': svg_path,
                'expected_location': f"images/{svg_path}",
                'file': file_path,
                'type': 'images'
            })
            
        # Pattern 3: Relative path to assets/diagrams
        pattern3 = r'!\[([^\]]*)\]\(assets/diagrams/([^)]+\.svg)\)'
        matches3 = re.findall(pattern3, content)
        for description, svg_path in matches3:
            references.append({
                'description': description,
                'svg_path': svg_path,
                'expected_location': f"assets/diagrams/{svg_path}",
                'file': file_path,
                'type': 'assets_diagrams_relative'
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

def find_existing_files(root_dir):
    """Find all existing SVG files in both assets/diagrams and images directories."""
    files = set()
    
    # Check assets/diagrams
    diagrams_dir = os.path.join(root_dir, 'assets', 'diagrams')
    if os.path.exists(diagrams_dir):
        for root, dirs, filenames in os.walk(diagrams_dir):
            for filename in filenames:
                if filename.endswith('.svg'):
                    rel_path = os.path.relpath(os.path.join(root, filename), root_dir)
                    files.add(rel_path.replace('\\', '/'))
    
    # Check images directory
    images_dir = os.path.join(root_dir, 'images')
    if os.path.exists(images_dir):
        for filename in os.listdir(images_dir):
            if filename.endswith('.svg'):
                rel_path = f"images/{filename}"
                files.add(rel_path)
    
    return files

def categorize_by_educational_importance(missing_diagrams):
    """Categorize missing diagrams by educational importance."""
    
    # High priority keywords (fundamental concepts)
    high_priority = [
        'algorithm', 'brute-force', 'problem-solving', 'implementation', 'debug',
        'input-output', 'data-structure', 'solution-design', 'testing',
        'reading-process', 'constraint', 'complexity', 'mathematical-properties'
    ]
    
    # Medium priority keywords
    medium_priority = [
        'contest', 'strategy', 'time-allocation', 'preparation', 'workflow',
        'step', 'pattern', 'guide', 'approach', 'technique', 'toolbox'
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
    
    print("=== Comprehensive SVG Diagram Analysis ===\n")
    
    # Find all markdown files
    markdown_files = find_all_markdown_files(root_dir)
    print(f"Found {len(markdown_files)} markdown files")
    
    # Extract all SVG references
    all_references = []
    for md_file in markdown_files:
        refs = extract_all_svg_references_from_markdown(md_file)
        all_references.extend(refs)
    
    print(f"Found {len(all_references)} total SVG references in markdown files")
    
    # Find existing SVG files
    existing_files = find_existing_files(root_dir)
    print(f"Found {len(existing_files)} existing SVG files")
    
    # Identify missing diagrams
    missing_diagrams = []
    existing_diagrams = []
    
    for ref in all_references:
        if ref['expected_location'] in existing_files:
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
                    chapter = ref['svg_path'].split('/')[0] if '/' in ref['svg_path'] else 'root'
                    print(f"{i:2d}. {ref['expected_location']}")
                    print(f"    Description: {ref['description']}")
                    print(f"    Chapter/Context: {chapter}")
                    print(f"    Referenced in: {os.path.basename(ref['file'])}")
                    print(f"    Path type: {ref['type']}")
                    print()
    
    # Summary by type
    print(f"\n=== MISSING DIAGRAMS BY TYPE ===")
    by_type = {}
    for ref in missing_diagrams:
        ref_type = ref['type']
        if ref_type not in by_type:
            by_type[ref_type] = []
        by_type[ref_type].append(ref)
    
    for ref_type, refs in by_type.items():
        print(f"{ref_type}: {len(refs)} missing")
    
    print(f"\n=== SUMMARY ===")
    if missing_diagrams:
        categorized = categorize_by_educational_importance(missing_diagrams)
        high_count = len(categorized.get('high', []))
        medium_count = len(categorized.get('medium', []))
        low_count = len(categorized.get('low', []))
        
        print(f"High priority (algorithm/data structure concepts): {high_count}")
        print(f"Medium priority (strategy/workflow concepts): {medium_count}")
        print(f"Low priority (general/supplementary): {low_count}")
        print(f"\nRECOMMENDATION: Focus on creating the {high_count} high-priority diagrams first.")
        print("These are fundamental algorithmic and data structure concepts crucial for learning.")
    else:
        print("All SVG diagrams referenced in markdown files already exist!")
    
    print(f"\nTotal missing: {len(missing_diagrams)}")
    print(f"Total existing: {len(existing_diagrams)}")

if __name__ == "__main__":
    main()