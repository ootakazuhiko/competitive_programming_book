---
title: "第4章：入出力処理を完全マスター"
layout: book
order: 4
checklist:
  - 標準入力/出力の基本を説明できる
  - 数値/文字列/配列など入力形式の扱いに慣れる
  - 出力フォーマット（小数/空白/改行）を制御できる
pitfalls:
  - 入力末尾の改行・空白の扱いミス
  - 出力の余計な空白/改行
  - 半角/全角や大小文字の取り違え
exercises:
  - { level: A, text: "四則演算の基礎", link: "https://atcoder.jp/contests/abc086/tasks/abc086_a" }
  - { level: A, text: "桁の和の判定", link: "https://atcoder.jp/contests/abc080/tasks/abc080_a" }
  - { level: B, text: "ユニーク要素数", link: "https://atcoder.jp/contests/abc085/tasks/abc085_b" }
---

<!-- 
本章は「中学生向け競技プログラミング入門書」の一部であり、
CC BY-NC-SA 4.0ライセンスの下で提供されます。
商用利用は事前許諾が必要です。
詳細：../../LICENSE.md
-->

# 第4章：入出力処理を完全マスター

## 章の学習目標

この章を読み終わることで、以下ができるようになります：
- 競技プログラミングでの入出力の特殊性を理解できる
- 様々な形式のデータを正確に読み込めるようになる
- 問題の要求に応じた適切な出力ができるようになる
- 入出力処理でよくあるエラーを回避できるようになる

競技プログラミングにおいて、入出力処理は最も基本的でありながら、最も重要な技術だ。どんなに素晴らしいアルゴリズムを思いついても、データを正しく読み込めなければ、正解にはたどり着けない。この章で、確実で効率的な入出力処理をマスターしよう。

## 4.1 入力って何？出力って何？

### Scratchとの対比による理解

![図4-1：ScratchとPythonの入出力対比]({{ site.baseurl }}/assets/diagrams/chapter4/figure4-1-scratch-python-io-comparison.svg)

### 競技プログラミングでの入出力の特殊性

一般的なプログラムと競技プログラミングでは、入出力の方式が大きく異なる：

![図4-2：一般プログラムと競技プログラムの入出力の違い]({{ site.baseurl }}/assets/diagrams/chapter4/figure4-2-general-vs-competitive-programming.svg)

### 標準入力・標準出力の概念

![図4-3：標準入力・標準出力のデータフロー]({{ site.baseurl }}/assets/diagrams/chapter4/figure4-3-standard-io-dataflow.svg)

AtCoderでは、この標準入力・標準出力を使って、自動的にプログラムをテストしている。君のプログラムに問題文の入力例を与えて、期待される出力例と一致するかをチェックしているんだ。

## 4.2 1つの数字を読み込もう

### 基本パターンの完全理解

最もシンプルな入力処理から始めよう。1つの整数を読み込む処理だ。

【図4-4：単一数値入力の内部処理フロー】

標準入力: "42\n"  ← \nは改行文字（見えない）
    ↓
input()関数: "42"  ← 文字列として取得（改行は除去）
    ↓
int()関数: 42  ← 整数として変換
    ↓
変数に格納: n = 42

コード例：
<figure class="pseudocode">
<figcaption>整数入力と内部での変換</figcaption>

```python
# 入力例: 42
n = int(input())

# 内部で起こっていること:
# 1) input() → "42"（文字列）
# 2) int("42") → 42（整数）
# 3) n = 42 が確定

print(n)       # 42
print(n * 2)   # 84
print(type(n)) # <class 'int'>
</figure>

### なぜint()が必要なのか

この点は初心者がよく混乱するところだ。詳しく説明しよう：

【図4-5：文字列と数値の違いによる動作の差】

<figure class="pseudocode">
  <figcaption>int()変換なしの場合</figcaption>
  <pre><code class="language-python">n = input()  # nは"42"（文字列）
print(n + n)   # "42" + "42" = "4242"（結合）
print(n * 2)   # "42" * 2 = "4242"（繰り返し）
print(n &gt; 5)   # エラー：文字列と数値は比較不可</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>int()変換ありの場合</figcaption>
  <pre><code class="language-python">n = int(input())  # nは42（整数）
print(n + n)   # 84（数値加算）
print(n * 2)   # 84（数値乗算）
print(n &gt; 5)   # True（数値比較）</code></pre>
</figure>

{% capture remember_int %}
• input() は必ず文字列を返す  
• 数値として計算したい場合は `int()` で変換  
• 文字列のままだと予期しない動作になる
{% endcapture %}
{% include panel.html type="info" title="🎯 覚えるポイント" content=remember_int %}

### 小数を読み込む場合

整数だけでなく、小数（浮動小数点数）を読み込む場合もある：

【図4-6：浮動小数点数の入力処理】

<figure class="pseudocode">
  <figcaption>基本的な浮動小数点数の読み込み</figcaption>
  <pre><code class="language-python"># 入力例: 3.14
pi = float(input())
print(pi)        # 3.14
print(pi * 2)    # 6.28
print(type(pi))  # &lt;class 'float'&gt;</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>整数か小数か分からない場合（実数）</figcaption>
  <pre><code class="language-python"># 問題文で「実数」と書かれている場合
x = float(input())

# 入力が"5"でも"5.0"でも正しく処理される
# float("5") → 5.0
# float("5.0") → 5.0
# float("3.14") → 3.14</code></pre>
</figure>

{% capture float_tips %}
• 「整数」→ `int()`、 「実数/小数」→ `float()`  
• 迷ったらサンプル入力を確認
{% endcapture %}
{% include panel.html type="steps" title="💡 使い分けの指針" content=float_tips %}

## 4.3 複数の数字を読み込もう

### split()とmap()の組み合わせの理解

複数の数値が1行に書かれている場合の処理は、競技プログラミングで最もよく使うパターンだ。

【図4-7：複数数値入力の段階的処理】

<figure class="pseudocode">
  <figcaption>1行の複数数値を処理する流れ</figcaption>
  <pre><code class="language-text">入力: "3 5 2\n"
    ↓
input(): "3 5 2"   ← 改行は自動で除去
    ↓
.split(): ["3", "5", "2"]   ← 空白で分割（文字列のリスト）
    ↓
map(int, ...): &lt;map object&gt;   ← 各要素を int() で変換するイテレータ
    ↓
用途に応じて受け取り方を選ぶ
  - 個別変数に展開（要素数が決まっている場合）
  - リスト化して扱う（可変長の場合）</code></pre>
  <figcaption>パターン1：個別変数に代入</figcaption>
  <pre><code class="language-python">a, b, c = map(int, input().split())
# a=3, b=5, c=2</code></pre>
  <figcaption>パターン2：リストとして取得</figcaption>
  <pre><code class="language-python">numbers = list(map(int, input().split()))
# numbers = [3, 5, 2]</code></pre>
  
</figure>

### split()関数の詳細

【図4-8：split()関数の動作パターン】

<figure class="pseudocode">
  <figcaption>基本的な使い方</figcaption>
  <pre><code class="language-python">text = "apple banana cherry"
words = text.split()  # 空白で分割
print(words)  # ['apple', 'banana', 'cherry']</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>区切り文字を指定</figcaption>
  <pre><code class="language-python">text = "1,2,3,4,5"
numbers = text.split(',')  # カンマで分割
print(numbers)  # ['1', '2', '3', '4', '5']</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>空白の処理</figcaption>
  <pre><code class="language-python">text = "  1   2    3  "  # 不規則な空白
parts = text.split()    # 連続空白も1つとして扱う
print(parts)  # ['1', '2', '3']</code></pre>
</figure>

{% capture split_points %}
• split() は必ず「文字列のリスト」を返す  
• 引数なしの場合、任意の空白で分割  
• 連続する空白は1つとして扱う  
• 先頭/末尾の空白は自動で無視
{% endcapture %}
{% include panel.html type="info" title="💡 重要な特徴" content=split_points %}

### map()関数の理解

![図4-9：map()関数による一括変換]({{ site.baseurl }}/assets/diagrams/chapter4/figure4-9-map-function-conversion.svg)

### 実践的な使い分け

【図4-10：複数入力の使い分けガイド】

<figure class="pseudocode">
  <figcaption>2–3個の値 → 個別変数（推奨）</figcaption>
  <pre><code class="language-python"># 座標を読み込む
x, y = map(int, input().split())
print(f"点({x}, {y})")

# 範囲を読み込む
start, end = map(int, input().split())
for i in range(start, end + 1):
    print(i)

# 3つの値
a, b, c = map(int, input().split())
print(max(a, b, c))</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>4個以上の値 → リスト（推奨）</figcaption>
  <pre><code class="language-python"># N個の点数を読み込む
n = int(input())
scores = list(map(int, input().split()))
print(f"平均: {sum(scores) / len(scores)}")
print(f"最高: {max(scores)}")
print(f"最低: {min(scores)}")

# 可変個数
data = list(map(int, input().split()))
print(f"合計: {sum(data)}")
print(f"要素数: {len(data)}")</code></pre>
</figure>

{% capture split_warn %}
⚠️ 避けるべきパターン  
• 個数が分からないのに個別変数で受け取る  
  a, b, c, d, e = map(int, input().split()) → 入力が3個だとエラー  
• 2–3個なのにリストで受け取り→添字参照  
  coords = list(map(int, input().split())) より  
  x, y = map(int, input().split()) の方が簡潔
{% endcapture %}
{% include panel.html type="warn" title="避けるべきパターン" content=split_warn %}

## 4.4 繰り返し入力を処理しよう

### N行入力の標準パターン

競技プログラミングでは「N個のデータが1行ずつ与えられる」というパターンが非常に多い。

【図4-11：N行入力処理の基本形】

問題例：「N個の整数が1行ずつ与えられる」

入力例:
3      ← N（データの個数）
10     ← 1行目の数値
25     ← 2行目の数値  
13     ← 3行目の数値

基本コード：
<figure class="pseudocode">
<figcaption>N行入力の基本形</figcaption>

```python
n = int(input())          # データ個数
numbers = []              # 結果格納用
for _ in range(n):        # N回繰り返し
    x = int(input())      # 1行ずつ読み込み
    numbers.append(x)

# この時点で numbers = [10, 25, 13]
print(max(numbers))       # 最大値: 25
print(sum(numbers))       # 合計: 48
print(len(numbers))       # 個数: 3
```
</figure>

### リスト内包表記による効率化

Pythonには、より簡潔に書ける「リスト内包表記」という機能がある：

【図4-12：リスト内包表記の活用】

基本形 → 内包表記への変換

❌ 冗長な書き方：
<figure class="pseudocode">
<figcaption>基本形（冗長）</figcaption>

```python
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
```
</figure>

✅ 内包表記（推奨）：
<figure class="pseudocode">
<figcaption>内包表記（推奨）</figcaption>

```python
n = int(input())
numbers = [int(input()) for _ in range(n)]
```
</figure>

さらなる応用例：
<figure class="pseudocode">
<figcaption>条件付きの読み込み</figcaption>

```python
n = int(input())
positive_nums = []
for _ in range(n):
    v = int(input())
    if v > 0:
        positive_nums.append(v)
```
</figure>

<figure class="pseudocode">
<figcaption>複数行の座標データ</figcaption>

```python
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
# 例: [[1, 2], [3, 4], [5, 6]]
```
</figure>

💡 "_"（アンダースコア）の意味：
• 変数名として"_"を使うのは「値を使わない」という慣習
• range(n)のカウンタは必要だが、実際の値は使わない場合
• "i"でも動作するが、"_"の方がPython的で推奨される

### 複数行・複数列データの処理

【図4-13：2次元データの読み込みパターン】

問題例：「N行M列の数値が与えられる」

入力例:
3 4        ← N=3行, M=4列
1 2 3 4    ← 1行目のデータ
5 6 7 8    ← 2行目のデータ
9 10 11 12 ← 3行目のデータ

処理コード：
<figure class="pseudocode">
<figcaption>N行M列の2次元読み込み</figcaption>

```python
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
# 例: 3行4列 → [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# アクセス例
print(matrix[0][0])  # 1行1列目: 1
print(matrix[1][2])  # 2行3列目: 7
print(matrix[2][3])  # 3行4列目: 12
```
</figure>

内包表記版：
<figure class="pseudocode">
<figcaption>2次元の内包表記版</figcaption>

```python
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
```
</figure>

実用例：
<figure class="pseudocode">
<figcaption>集計パターン</figcaption>

```python
# 各行の合計
for i, row in enumerate(matrix):
    print(f"{i+1}行目の合計: {sum(row)}")

# 全体の最大値
max_val = 0
for row in matrix:
    for val in row:
        max_val = max(max_val, val)
print(f"最大値: {max_val}")
```
</figure>

## 4.5 文字列入力を扱おう

### 文字列処理の基本パターン

数値だけでなく、文字列を扱う問題も多い。文字列の場合は`int()`変換は不要だ。

【図4-14：文字列入力の処理方法】

<figure class="pseudocode">
  <figcaption>基本的な文字列入力</figcaption>
  <pre><code class="language-python">s = input()                # 1行を文字列として読む
print(len(s))             # 文字数
print(s.upper())          # 大文字
print(s.lower())          # 小文字
print(s[::-1])            # 逆順</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>複数の文字列を読み込む</figcaption>
  <pre><code class="language-python"># 例: "apple banana cherry"
words = input().split()   # ['apple', 'banana', 'cherry']
for word in words:
    print(f"単語: {word}, 長さ: {len(word)}")</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>1文字ずつの処理</figcaption>
  <pre><code class="language-python">s = input()               # 例: "hello"
for i, char in enumerate(s):
    print(f"{i}番目の文字: {char}")
# 出力:
# 0番目の文字: h
# 1番目の文字: e
# 2番目の文字: l
# 3番目の文字: l
# 4番目の文字: o</code></pre>
</figure>

### 文字列と数値の混在入力

【図4-15：混在データの処理パターン】

<figure class="pseudocode">
  <figcaption>名前と年齢（空白区切り）</figcaption>
  <pre><code class="language-python"># 方法1: 分割してから変換
line = input().split()
name = line[0]
age = int(line[1])
print(f"{name}さんは{age}歳です")

# 方法2: 直接代入（型が確定）
name, age_str = input().split()
age = int(age_str)
print(f"{name}さんは{age}歳です")</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>複雑な混在（先頭が個数）</figcaption>
  <pre><code class="language-python"># 例: "3 Alice Bob Charlie"
data = input().split()
n = int(data[0])     # 最初は個数
names = data[1:]
print(f"人数: {n}")
for i, name in enumerate(names):
    print(f"{i+1}番目: {name}")</code></pre>
</figure>

{% capture mixed_warn %}
注意が必要  
• 文字列に空白が含まれる場合（例: "Hello World" 25）  
• split() だけでは分割できないケースあり  
• 問題文の入力形式を必ず確認
{% endcapture %}
{% include panel.html type="warn" title="注意が必要なパターン" content=mixed_warn %}

### 文字列操作の実践例

【図4-16：競技プログラミングでよく使う文字列操作】

<figure class="pseudocode">
  <figcaption>パターン1：文字の出現回数カウント</figcaption>
  <pre><code class="language-python">s = input()  # 例: "programming"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# より簡潔に
from collections import Counter
char_count = Counter(s)</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン2：回文（palindrome）判定</figcaption>
  <pre><code class="language-python">s = input()  # 例: "racecar"
if s == s[::-1]:
    print("回文です")
else:
    print("回文ではありません")

# 大文字小文字を区別しない場合
s = input().lower()
if s == s[::-1]:
    print("回文です（大小文字無視）")</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン3：文字列の置換・加工</figcaption>
  <pre><code class="language-python">s = input()  # 例: "Hello World"
s = s.replace(" ", "_")      # "Hello_World"
s = s.replace("o", "0")      # "Hell0_W0rld"
s = s.lower()                  # "hell0_w0rld"
words = s.split("_")           # ["hell0", "w0rld"]
print("_".join(words))        # "hell0_w0rld"</code></pre>
</figure>

## 4.6 出力フォーマットをマスターしよう

### print()関数の詳細オプション

出力処理も入力と同じくらい重要だ。AtCoderでは出力形式が厳密に指定されるため、正確な出力が必要だ。

![図4-17：print()関数の完全活用]({{ site.baseurl }}/assets/diagrams/chapter4/figure4-17-print-function-complete-usage.svg)

### 問題別出力パターン

【図4-18：競技プログラミングでよくある出力パターン】

<figure class="pseudocode">
  <figcaption>パターン1: リストの要素を1行で出力</figcaption>
  <pre><code class="language-python">numbers = [1, 2, 3, 4, 5]
# 方法1: * 演算子（推奨）
print(*numbers)                 # 1 2 3 4 5

# 方法2: join()
print(' '.join(map(str, numbers)))

# 方法3: sep（固定個数のみ）
print(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン2: リストの要素を1行ずつ出力</figcaption>
  <pre><code class="language-python">numbers = [10, 20, 30]
# 方法1: for ループ（推奨）
for num in numbers:
    print(num)

# 方法2: join() で改行結合
print('\\n'.join(map(str, numbers)))</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン3: 条件付き出力</figcaption>
  <pre><code class="language-python">n = int(input())
if n % 2 == 0:
    print("Even")   # 大小文字に注意
else:
    print("Odd")    # 問題文と一致

# Yes/No の出力
if condition:
    print("Yes")
else:
    print("No")</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン4: 小数点の制御</figcaption>
  <pre><code class="language-python">import math
pi = math.pi  # 3.141592653589793

# 小数点以下2桁
print(f"{pi:.2f}")    # 3.14

# 小数点以下6桁
print(f"{pi:.6f}")    # 3.141593

# 問題で「小数点以下3桁」指定
result = 7 / 3
print(f"{result:.3f}")  # 2.333</code></pre>
</figure>

### 出力でよくあるミス

【図4-19：出力の典型的な間違いパターン】

{% capture mistake1 %}
❌ 余分な文字・説明の出力  
例：「答えを出力」なのに説明を付ける  
• print("答えは", answer) → 説明は不要  
• 正：print(answer)
{% endcapture %}
{% include panel.html type="warn" title="ミス1" content=mistake1 %}

{% capture mistake2 %}
❌ 改行の制御ミス  
例：「a bを1行で出力」  
• print(a); print(b) → 2行になる  
• 正：print(a, b)
{% endcapture %}
{% include panel.html type="warn" title="ミス2" content=mistake2 %}

{% capture mistake3 %}
❌ 大文字小文字の間違い  
例：「Yes」指定なのに yes/YES と出力  
• 正：print("Yes")（問題文と一致）
{% endcapture %}
{% include panel.html type="warn" title="ミス3" content=mistake3 %}

{% capture mistake4 %}
❌ 区切り文字の間違い  
• カンマ区切り → ','.join(...)  
• 空白区切り → print(*numbers)
{% endcapture %}
{% include panel.html type="warn" title="ミス4" content=mistake4 %}

{% capture checklist %}
🛡️ 出力ミス防止チェック  
1) サンプル出力を文字単位で確認  
2) 余計な説明文字がない  
3) 改行/スペース/区切りが正確  
4) 大小文字が一致  
5) 小数点桁数が指定通り
{% endcapture %}
{% include panel.html type="steps" title="チェックリスト" content=checklist %}

## 典型的な誤りと修正（入出力）

{% capture io_wrong %}
ケース1: `a, b = input().split()` のまま演算してしまう  
→ 文字列のままなので `"2" + "3" == "23"`。修正: `a, b = map(int, input().split())`

ケース2: リストをそのまま `print(numbers)` してしまう  
→ 期待は `1 2 3` だが `['1', '2', '3']` になる。修正: `print(*numbers)`（アンパック）

ケース3: N行入力なのに1行で `split()` しようとする  
→ 入力形式と不一致。修正: `for _ in range(N): x = int(input())`
{% endcapture %}
{% include panel.html type="warn" title="⚠️ よくある誤り" content=io_wrong %}

## まとめ：入出力処理の完全マスター達成！

この章では、競技プログラミングにおける入出力処理のすべてを学んだ。

【図4-20：この章で身につけたスキル】

{% capture ch4_gained %}
✅ 単一/複数数値の読み込み  
✅ 繰り返し入力・2次元データ  
✅ 文字列・混在データの処理  
✅ 多様な出力形式  
✅ 入出力エラーの回避と対処
{% endcapture %}
{% include panel.html type="steps" title="🎯 習得したスキル" content=ch4_gained %}

{% capture ch4_next %}
第5章: 基本アルゴリズムの道具箱  
• 基本手法の学習  
• 全探索/ソート/貪欲法  
• 実問題への適用
{% endcapture %}
{% include panel.html type="info" title="🚀 次のステップ" content=ch4_next %}

入出力処理は、競技プログラミングにおける「基礎の基礎」だ。どんなに高度なアルゴリズムを知っていても、データを正しく読み込み、正確に出力できなければ、正解にはたどり着けない。

この章で学んだ技術は、今後のすべての問題で使うことになる。特に以下のパターンは頻繁に使うので、しっかりと覚えておこう：

- `n = int(input())` - 単一整数の読み込み
- `a, b = map(int, input().split())` - 複数整数の読み込み
- `numbers = [int(input()) for _ in range(n)]` - N行の整数読み込み
- `print(*list)` - リストの要素をスペース区切りで出力

次の章では、いよいよアルゴリズムの世界に足を踏み入れよう。問題を効率的に解くための「道具箱」を手に入れることで、君の競技プログラミングスキルは大きく飛躍するはずだ！

# 章末クイズ（理解度チェック）

{% capture quiz_q %}
Q1. 標準入力から1行の整数を3つ読み、合計を出力したい。最も簡潔な実装は？（Python）  
Q2. `input().split()` が返す型は？  
Q3. `map(int, input().split())` の返り値をそのまま `len()` に渡すと何が起こる？  
Q4. N行入力で、1行ずつ整数を読みたい。forの回数と `input()` の呼び出し関係は？  
Q5. 浮動小数点の出力で小数第2位まで表示するフォーマット指定子は？
{% endcapture %}
{% include panel.html type="steps" title="📘 質問" content=quiz_q %}

{% capture quiz_a %}
A1. `a,b,c = map(int, input().split()); print(a+b+c)`  
A2. 文字列のリスト（例: `["1","2","3"]`）  
A3. `map` オブジェクトであり、そのままでは長さを数えられない（`len()`は不可）。`list(...)` で実体化する  
A4. `for _ in range(N): x = int(input())` のように N 回 `input()` を呼ぶ  
A5. `print(f"{x:.2f}")`（フォーマット指定: `.2f`）
{% endcapture %}
{% include panel.html type="info" title="📝 解答とヒント" content=quiz_a %}

{% capture ch4_map %}
| パターン | 問題 | 難易度 | 制約目安 | 想定テク |
|---|---|---|---|---|
| 1行で複数整数 | [ABC086A Product](https://atcoder.jp/contests/abc086/tasks/abc086_a) | A | 小 | `map(int, input().split())` |
| N個の整数（1行） | [ABC081B Shift only](https://atcoder.jp/contests/abc081/tasks/abc081_b) | B | 中 | 分割→`map`→反復/条件 |
| N行入力（整数） | [ABC155B Papers, Please](https://atcoder.jp/contests/abc155/tasks/abc155_b) | B | 中 | `for _ in range(N): int(input())` |
| 2次元グリッド | [ABC075B Minesweeper](https://atcoder.jp/contests/abc075/tasks/abc075_b) | B | 中 | `H,W`→`grid=[input() for _ in range(H)]` |
| 2次元数値 | [ABC237B Matrix Transposition](https://atcoder.jp/contests/abc237/tasks/abc237_b) | B | 中 | `H,W`＋各行`map(int, ...)` |
| 文字列入力/処理 | [ABC081A Placing Marbles](https://atcoder.jp/contests/abc081/tasks/abc081_a) | A | 小 | `s=input(); s.count('1')` |
| 混在データ | [ABC086C Traveling](https://atcoder.jp/contests/abc086/tasks/abc086_c) | C（発展） | 中 | 複数行/複数値の読解と検証 |
{% endcapture %}
{% include panel.html type="info" title="🔗 パターン→実例マッピング（入出力）" content=ch4_map %}

{% capture ch4_note %}
凡例  
• 難易度: AtCoderのA/B/C目安  
• 制約目安: 小（〜10^2）、中（〜10^5 前後）  
• 想定テク: そのパターンで身につく代表的な手筋
{% endcapture %}
{% include panel.html type="info" title="ℹ️ 注記（凡例）" content=ch4_note %}
