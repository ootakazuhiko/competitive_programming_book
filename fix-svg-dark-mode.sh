#!/bin/bash

# SVGファイルのダークモード表示問題を修正するスクリプト
# CSS変数にフォールバック色を追加

echo "🎨 SVG dark mode fix script starting..."

# CSS変数を使用しているSVGファイルを検索
files_with_css_vars=$(grep -r "var(--" assets/diagrams/ --include="*.svg" | cut -d: -f1 | sort -u)

echo "Found $(echo "$files_with_css_vars" | wc -l) files with CSS variables"

for file in $files_with_css_vars; do
    echo "Processing: $file"
    
    # バックアップ作成
    cp "$file" "$file.bak"
    
    # CSS変数にフォールバック色を追加
    sed -i 's/var(--svg-bg)/var(--svg-bg, #ffffff)/g' "$file"
    sed -i 's/var(--svg-bg-alt)/var(--svg-bg-alt, #f8fafc)/g' "$file"
    sed -i 's/var(--svg-text)/var(--svg-text, #1a1a1a)/g' "$file"
    sed -i 's/var(--svg-border)/var(--svg-border, #d1d5db)/g' "$file"
    sed -i 's/var(--svg-primary)/var(--svg-primary, #3b82f6)/g' "$file"
    sed -i 's/var(--svg-success)/var(--svg-success, #10b981)/g' "$file"
    sed -i 's/var(--svg-warning)/var(--svg-warning, #f59e0b)/g' "$file"
    sed -i 's/var(--svg-error)/var(--svg-error, #ef4444)/g' "$file"
    sed -i 's/var(--svg-info)/var(--svg-info, #06b6d4)/g' "$file"
    sed -i 's/var(--svg-secondary)/var(--svg-secondary, #64748b)/g' "$file"
    
    echo "✅ Fixed: $file"
done

echo "🎉 All SVG files have been updated with fallback colors for dark mode compatibility"
echo "Files processed: $(echo "$files_with_css_vars" | wc -l)"
echo ""
echo "To test the changes:"
echo "1. Open any SVG file in a browser"
echo "2. Check that content is visible in both light and dark modes"
echo "3. Verify that emojis and text are properly displayed"