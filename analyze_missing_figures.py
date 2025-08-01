#!/usr/bin/env python3
"""
Script to analyze missing figure references that haven't been converted to SVG format.
Compares figure references in markdown files with existing SVG files.
"""

import os
import re
import glob
from collections import defaultdict

def extract_figure_references(file_path):
    """Extract all figure references from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match 【図X-Y：タイトル】
    pattern = r'【図(\d+)-(\d+)：([^】]+)】'
    matches = re.findall(pattern, content)
    
    return [(int(chapter), int(figure), title) for chapter, figure, title in matches]

def get_existing_svg_files():
    """Get list of existing SVG files."""
    svg_files = set()
    
    # Search in assets/diagrams and images directories
    for pattern in ['assets/diagrams/**/*.svg', 'images/*.svg']:
        for file_path in glob.glob(pattern, recursive=True):
            filename = os.path.basename(file_path)
            # Extract figure number from filename like "figure1-2-something.svg"
            match = re.match(r'figure(\d+)-(\d+)-.*\.svg', filename)
            if match:
                chapter, figure = int(match.group(1)), int(match.group(2))
                svg_files.add((chapter, figure))
    
    return svg_files

def get_context_for_figure(file_path, chapter, figure):
    """Get context around a figure reference for description."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    figure_pattern = f'【図{chapter}-{figure}：'
    context_lines = []
    
    for i, line in enumerate(lines):
        if figure_pattern in line:
            # Get context: 2 lines before and 3 lines after
            start = max(0, i - 2)
            end = min(len(lines), i + 4)
            context_lines = lines[start:end]
            break
    
    return '\n'.join(line.strip() for line in context_lines if line.strip())

def determine_priority(chapter, figure, title, context):
    """Determine priority based on educational importance."""
    # High priority keywords
    high_priority_keywords = [
        '完全ガイド', '基本概念', '5ステップ', '戦略', 'プロセス',
        '全体像', '構造', 'フロー', '完全解法', '段階的'
    ]
    
    # Medium priority keywords  
    medium_priority_keywords = [
        '活用', '応用', '実践', '例', 'パターン', '比較',
        'テクニック', '手順', 'ガイド'
    ]
    
    # Check if it's a summary/skills figure (usually lower priority)
    if 'この章で身につけた' in title or '次章への' in title:
        return 'low'
    
    # Check for high priority keywords
    if any(keyword in title for keyword in high_priority_keywords):
        return 'high'
    
    # Check for medium priority keywords
    if any(keyword in title for keyword in medium_priority_keywords):
        return 'medium'
    
    # Default to medium for most educational content
    return 'medium'

def main():
    # Chapter mapping for better organization
    chapter_mapping = {
        1: 'introduction',
        2: 'environment-setup', 
        3: 'programming-environment',
        4: 'input-output',
        5: 'basic-algorithms',
        6: 'basic-data-structures',
        7: 'abc-problems',
        8: 'problem-solving',
        9: 'debugging',
        10: 'contest-participation',
        11: 'community',
        12: 'future-career'
    }
    
    # Collect all figure references
    all_figures = []
    src_dir = 'src'
    
    for chapter_dir in os.listdir(src_dir):
        if chapter_dir.startswith('chapter-'):
            index_file = os.path.join(src_dir, chapter_dir, 'index.md')
            if os.path.exists(index_file):
                figures = extract_figure_references(index_file)
                for chapter, figure, title in figures:
                    context = get_context_for_figure(index_file, chapter, figure)
                    priority = determine_priority(chapter, figure, title, context)
                    all_figures.append({
                        'chapter': chapter,
                        'figure': figure, 
                        'title': title,
                        'context': context,
                        'priority': priority,
                        'file_path': index_file
                    })
    
    # Get existing SVG files
    existing_svgs = get_existing_svg_files()
    
    # Find missing figures
    missing_figures = []
    for fig in all_figures:
        if (fig['chapter'], fig['figure']) not in existing_svgs:
            missing_figures.append(fig)
    
    # Sort by chapter and figure number
    missing_figures.sort(key=lambda x: (x['chapter'], x['figure']))
    
    # Group by chapter
    by_chapter = defaultdict(list)
    for fig in missing_figures:
        by_chapter[fig['chapter']].append(fig)
    
    # Generate markdown report
    print("# 競技プログラミング本 - 未作成図版リスト")
    print()
    print("## 概要")
    print(f"- 総図版参照数: {len(all_figures)}")
    print(f"- 既存SVGファイル数: {len(existing_svgs)}")
    print(f"- **未作成図版数: {len(missing_figures)}**")
    print()
    
    # Priority summary
    priority_counts = defaultdict(int)
    for fig in missing_figures:
        priority_counts[fig['priority']] += 1
    
    print("## 優先度別内訳")
    for priority in ['high', 'medium', 'low']:
        count = priority_counts[priority]
        priority_ja = {'high': '高', 'medium': '中', 'low': '低'}[priority]
        print(f"- {priority_ja}優先度: {count}個")
    print()
    
    print("## 章別詳細リスト")
    print()
    
    for chapter in sorted(by_chapter.keys()):
        chapter_name = chapter_mapping.get(chapter, f'chapter-{chapter}')
        figures = by_chapter[chapter]
        
        print(f"### 第{chapter}章 ({chapter_name})")
        print(f"未作成図版数: {len(figures)}個")
        print()
        
        for fig in figures:
            priority_icon = {'high': '🔴', 'medium': '🟡', 'low': '⚪'}[fig['priority']]
            print(f"#### {priority_icon} 図{fig['chapter']}-{fig['figure']}: {fig['title']}")
            print()
            
            # Add brief description based on context
            if fig['context']:
                # Take first meaningful sentence from context
                context_lines = fig['context'].split('\n')
                description = ""
                for line in context_lines:
                    if line and not line.startswith('【図') and len(line) > 10:
                        description = line[:100] + "..." if len(line) > 100 else line
                        break
                
                if description:
                    print(f"**内容**: {description}")
                    print()
            
            priority_desc = {
                'high': '基本概念や重要なプロセスを説明する教育的価値の高い図版',
                'medium': '具体的な手法や応用例を示す実用的な図版', 
                'low': '章のまとめや補足的な内容を含む図版'
            }[fig['priority']]
            
            print(f"**優先度**: {fig['priority'].upper()} - {priority_desc}")
            print()
            print("---")
            print()
    
    # Generate GitHub issue format
    print("\n## GitHub Issue用サマリー")
    print()
    print("```markdown")
    print("## 未作成図版の作成タスク")
    print()
    print(f"競技プログラミング本で参照されている図版のうち、{len(missing_figures)}個がまだSVG形式で作成されていません。")
    print()
    print("### 優先度別作業量")
    for priority in ['high', 'medium', 'low']:
        count = priority_counts[priority]
        if count > 0:
            priority_ja = {'high': '高優先度', 'medium': '中優先度', 'low': '低優先度'}[priority]
            print(f"- [ ] {priority_ja}: {count}個")
    print()
    print("### 章別内訳")
    for chapter in sorted(by_chapter.keys()):
        chapter_name = chapter_mapping.get(chapter, f'chapter-{chapter}')
        count = len(by_chapter[chapter])
        print(f"- 第{chapter}章 ({chapter_name}): {count}個")
    print("```")

if __name__ == '__main__':
    main()