---
title: "第6章：データ構造を理解して活用しよう"
layout: book
order: 6
---

<!-- 
本章は「中学生向け競技プログラミング入門書」の一部であり、
CC BY-NC-SA 4.0ライセンスの下で提供されます。
商用利用は事前許諾が必要です。
詳細：../../LICENSE.md
-->

# 第6章：データ構造を理解して活用しよう

## 6.1 リスト（配列）を使いこなそう

第5章では基本的なアルゴリズムを学んだね。今度は、それらのアルゴリズムを効率的に実行するための「データ構造」について学ぼう。データ構造とは、プログラムの中でデータを整理して保存する「入れ物」のようなものだ。

まずは、Pythonで最もよく使われるリスト（配列）から始めよう。

【図6-1：リストの基本概念とメモリ構造】

{% include panel.html type="info" title="リストとは" content="複数のデータを順番に並べて保存できる入れ物（順序・重複・異種型OK／追加・削除・変更が可能）" %}

```python
numbers = [10, 25, 7, 33, 2]
# メモリ図は将来のSVG図に統一（本文では省略）
 

### リストの基本操作をマスターしよう

【図6-2：リスト操作の完全ガイド】

{% include panel.html type="steps" title="作成と初期化" content="空: []/list()／リテラル: [1,2,3]／同値初期化: [0]*n／二次元は内包で [[0]*c for _ in range(r)]" %}

```python
# 作成と初期化の例
empty_list = []
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
zeros = [0] * 5
matrix = [[0] * 3 for _ in range(2)]
```

{% include panel.html type="steps" title="アクセス" content="正のインデックス／負のインデックス／スライス（start:end）" %}

```python
numbers = [10, 25, 7, 33, 2]
print(numbers[0])   # 10
print(numbers[-1])  # 2
print(numbers[1:4]) # [25, 7, 33]
```

{% include panel.html type="steps" title="追加・挿入" content="append／insert／extend" %}

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.insert(1, "orange")
fruits.extend(["grape", "melon"])
```

❌ 要素の削除・変更
<figure class="pseudocode">
<figcaption>削除・変更の基本操作</figcaption>

```python
numbers = [10, 25, 7, 33, 2, 25]

# 値を指定して削除（最初の1件）
numbers.remove(25)
print(numbers)  # [10, 7, 33, 2, 25]

# インデックスを指定して削除
del numbers[0]
print(numbers)  # [7, 33, 2, 25]

# 末尾要素を削除して取得
last = numbers.pop()
print(last)     # 25
print(numbers)  # [7, 33, 2]

# 要素の変更
numbers[0] = 100
print(numbers)  # [100, 33, 2]
```
</figure>
```

### 二次元リスト（表形式データ）の活用

【図6-3：二次元リストの構造と活用法】

📊 二次元リストの基本概念

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

<div class="table-scroll">
<table class="table-compact table-striped">
  <thead>
    <tr><th></th><th>列0</th><th>列1</th><th>列2</th></tr>
  </thead>
  <tbody>
    <tr><th>行0</th><td>1</td><td>2</td><td>3</td></tr>
    <tr><th>行1</th><td>4</td><td>5</td><td>6</td></tr>
    <tr><th>行2</th><td>7</td><td>8</td><td>9</td></tr>
  </tbody>
</table>
</div>

アクセス方法:

```python
print(grid[0][0])  # 1
print(grid[1][2])  # 6
print(grid[2][1])  # 8
```

🏗️ 二次元リストの作成方法
<figure class="pseudocode">
<figcaption>作成パターン</figcaption>

```python
# 方法1: 直接作成
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 方法2: 内包表記（推奨）
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
# [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# 方法3: 値を入力しながら作成
matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

# ❌ 危険: 参照共有で意図せず同時更新
wrong = [[0] * 3] * 3
```
</figure>

🔄 二次元リストの操作パターン
<figure class="pseudocode">
<figcaption>走査・集計の基本</figcaption>

```python
# 全要素への処理
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"({i},{j}): {matrix[i][j]}")

# より Pythonic な書き方
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        print(f"({i},{j}): {value}")

# 行ごとの処理
for row in matrix:
    print(sum(row))  # 各行の合計

# 列ごとの処理
for j in range(len(matrix[0])):
    col_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(col_sum)  # 各列の合計
```
</figure>
```

### 競技プログラミングでのリスト活用例

【図6-4：実際の問題でのリスト活用パターン】

{% include panel.html type="info" title="問題例1: 配列の最大値・最小値（概要）" content="N個の整数が与えられる。最大値と最小値を出力せよ。入力例: 5 / 3 1 4 1 5" %}
<figure class="pseudocode">
<figcaption>実装（max/min の活用）</figcaption>

```python
n = int(input())
numbers = list(map(int, input().split()))
print(max(numbers), min(numbers))
```
</figure>
{% include panel.html type="steps" title="ポイント" content="リストに格納してから処理／組み込み関数 max(), min() を活用" %}

{% include panel.html type="info" title="問題例2: 累積和の計算（概要）" content="配列の各要素について、その位置までの累積和を求める。例: [1,2,3,4,5] → [1,3,6,10,15]" %}
<figure class="pseudocode">
<figcaption>実装（累積和）</figcaption>

```python
numbers = [1, 2, 3, 4, 5]
cumsum = []
total = 0
for num in numbers:
    total += num
    cumsum.append(total)
print(cumsum)  # [1, 3, 6, 10, 15]
```
</figure>
{% include panel.html type="steps" title="応用" content="累積和配列を作れば区間和を O(1) で計算可能" %}

{% include panel.html type="info" title="問題例3: 二次元グリッドの探索（概要）" content="H×W のグリッドで、'#' の隣接する '.' の個数を数える。上下左右の4方向を探索" %}
<figure class="pseudocode">
<figcaption>実装（グリッド探索）</figcaption>

```python
h, w = map(int, input().split())
grid = [input() for _ in range(h)]

count = 0
directions = [(0,1), (0,-1), (1,0), (-1,0)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    if grid[ni][nj] == '.':
                        count += 1
print(count)
```
</figure>

## 6.2 辞書（ディクショナリ）で高速検索

リストは順番にデータを管理するのに適しているが、「特定の値を高速で検索したい」「データに名前を付けて管理したい」という場合には、辞書（ディクショナリ）が威力を発揮する。

![図6-2：リストvs辞書vs集合比較]({{ site.baseurl }}/images/figure6-2-list-dict-set-comparison.svg)

### 辞書の基本操作をマスターしよう

【図6-6：辞書操作の完全ガイド】

{% include panel.html type="steps" title="辞書の作成方法" content="空の作成: {} / dict()／リテラルで作成／dict()のキーワード引数／ペアのリストから作成" %}

```python
# 空の辞書
empty_dict = {}
empty_dict = dict()

# 値を入れて作成
student = {"name": "Alice", "age": 14, "grade": "8th"}
scores = {"math": 85, "english": 92, "science": 78}

# dict() のキーワード引数
colors = dict(red="赤", blue="青", green="緑")

# ペアのリストから作成
items = [("apple", 100), ("banana", 80), ("cherry", 120)]
prices = dict(items)
print(prices)  # {"apple": 100, "banana": 80, "cherry": 120}
```

{% include panel.html type="steps" title="要素へのアクセスと操作" content="[] と get()／存在しないキー時の既定値／値の変更・追加／削除(pop/del)" %}

```python
student = {"name": "Alice", "age": 14, "grade": "8th"}

# 値の取得
print(student["name"])            # Alice
print(student.get("age"))         # 14
print(student.get("height", "不明"))  # 不明

# 値の変更・追加
student["age"] = 15               # 変更
student["height"] = 160           # 追加
print(student)                     # {"name": "Alice", "age": 15, "grade": "8th", "height": 160}

# 要素の削除
del student["height"]             # キー指定削除
grade = student.pop("grade")      # 削除して値取得
print(grade)                       # 8th
print(student)                     # {"name": "Alice", "age": 15}
```

{% include panel.html type="steps" title="辞書の反復処理" content="keys/values/items の使い分け／for での標準反復はキー列挙" %}

```python
scores = {"math": 85, "english": 92, "science": 78}

# キーのみ取得
for subject in scores:
    print(subject)  # math, english, science

# 値のみ取得
for score in scores.values():
    print(score)  # 85, 92, 78

# キーと値のペア取得
for subject, score in scores.items():
    print(f"{subject}: {score}")  # math: 85, english: 92, science: 78

# 条件付き処理
high_scores = {k: v for k, v in scores.items() if v >= 80}
print(high_scores)  # {"math": 85, "english": 92}
```

### 競技プログラミングでの辞書活用パターン

【図6-7：辞書を使った典型的な解法パターン】

{% include panel.html type="info" title="パターン1: カウント処理（文字出現回数）" content="入力: programming → 出力: p:1, r:2, o:1, g:2, a:1, m:2, i:1, n:1" %}
```python
text = "programming"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    print(f"{char}:{count}")

# 簡潔版（標準ライブラリ）
from collections import Counter
print(dict(Counter(text)))
```

{% include panel.html type="steps" title="パターン2: グループ分け（学年で分類）" content="辞書のキーにグループ名、値にリスト／defaultdict(list) で初期化不要化" %}
```python
students = [("Alice", "8th"), ("Bob", "7th"), ("Charlie", "8th")]

# 通常の辞書版
groups = {}
for name, grade in students:
    if grade not in groups:
        groups[grade] = []
    groups[grade].append(name)
print(groups)  # {"8th": ["Alice", "Charlie"], "7th": ["Bob"]}

# defaultdict 版
from collections import defaultdict
groups = defaultdict(list)
for name, grade in students:
    groups[grade].append(name)
```

{% include panel.html type="steps" title="パターン3: 高速な存在確認・検索" content="集合/辞書による O(1) 確認。リストは O(N) で非効率" %}
```python
allowed_users = {"alice", "bob", "charlie", "david"}

def is_allowed(user_id):
    return user_id in allowed_users  # True/False を高速判定

print(is_allowed("alice"))  # True
print(is_allowed("eve"))    # False

# リスト比較（遅い: O(N)）
allowed_list = ["alice", "bob", "charlie", "david"]
def is_allowed_slow(user_id):
    return user_id in allowed_list
```

{% include panel.html type="steps" title="パターン4: メモ化（動的計画法の基礎）" content="計算済み結果を辞書に保存して再利用。大幅な高速化" %}
```python
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

memo = {}
def fibonacci_fast(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_fast(n-1) + fibonacci_fast(n-2)
    return memo[n]

# 効果の例
# fibonacci_slow(30) は数秒、fibonacci_fast(30) は瞬時
 

 

## 6.3 集合（セット）で重複を管理

データを扱っていると、「重複する要素を除去したい」「2つのグループの共通部分を知りたい」といった場面に遭遇する。そんなときに威力を発揮するのが、集合（セット）だ。

【図6-8：集合の基本概念と数学的背景】

{% include panel.html type="info" title="集合の特徴" content="重複なし／順序なし（インデックス不可）／存在確認が高速（O(1)）／集合演算が可能（和・積・差・対称差）" %}

```python
# 重複除去の自動化
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
unique = set(numbers)
print(unique)  # {1, 2, 3, 4, 5}
```

### 集合の基本操作

【図6-9：集合操作の完全ガイド】

{% include panel.html type="steps" title="作成パターン" content="空は set()（{} は辞書）／リテラル {…}／リストや文字列から set(…) で作成" %}

```python
# 空の集合作成
empty_set = set()
# empty_set = {}  # これは辞書になる

# 値を入れて集合作成
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# リストから（重複除去）
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)  # {1, 2, 3, 4, 5}

# 文字列から
chars = set("programming")
print(chars)  # {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'}
```

{% include panel.html type="steps" title="追加・削除の基本" content="add／update（複数）／remove（無いと例外）／discard（無視）／pop（任意の1要素）／clear" %}

```python
fruits = {"apple", "banana"}

# 追加
fruits.add("cherry")
print(fruits)  # {"apple", "banana", "cherry"}

# 複数追加
fruits.update(["grape", "melon"])
fruits.update({"orange", "kiwi"})
print(fruits)  # {"apple", "banana", "cherry", "grape", "melon", "orange", "kiwi"}

# 削除
fruits.remove("banana")      # 無いと例外
fruits.discard("pineapple")  # 無い場合は何もしない
popped = fruits.pop()         # 任意の1要素
print(popped)

# 全削除
fruits.clear()
print(fruits)  # set()
```

{% include panel.html type="steps" title="存在確認・サイズ・反復" content="in で高速存在確認／len で要素数／for で列挙／内包表記でフィルタ" %}

```python
languages = {"Python", "Java", "C++", "JavaScript"}

# 存在確認（高速：O(1)）
print("Python" in languages)   # True
print("Ruby" in languages)     # False

# 要素数
print(len(languages))          # 4

# 反復処理
for lang in languages:
    print(f"I can use {lang}")

# 条件付きフィルタ
short_names = {lang for lang in languages if len(lang) <= 4}
print(short_names)  # {"Java", "C++"}
```

### 集合演算の活用

【図6-10：集合演算による高度なデータ処理】

{% include panel.html type="steps" title="基本的な集合演算" content="和集合 A|B／積集合 A&B／差集合 A-B／対称差 A^B（いずれもメソッド有）" %}

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 和集合（union）：AまたはBに含まれる要素
union = A | B
# または A.union(B)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 積集合（intersection）：AとBの両方に含まれる要素
intersection = A & B
# または A.intersection(B)
print(intersection)  # {4, 5}

# 差集合（difference）：Aに含まれBに含まれない要素
difference = A - B
# または A.difference(B)
print(difference)  # {1, 2, 3}

# 対称差集合（symmetric_difference）：どちらか一方のみに含まれる
sym_diff = A ^ B
# または A.symmetric_difference(B)
print(sym_diff)  # {1, 2, 3, 6, 7, 8}
```

{% include panel.html type="steps" title="集合関係の判定" content="部分集合 issubset／上位集合 issuperset／素集合 isdisjoint（共通要素なし）" %}

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

# 部分集合の判定
print(A.issubset(B))   # True（AはBの部分集合）
print(B.issubset(A))   # False

# 上位集合の判定
print(B.issuperset(A)) # True（BはAの上位集合）

# 素集合の判定（共通要素なし）
print(A.isdisjoint(C)) # True
print(A.isdisjoint(B)) # False

# 応用例：権限管理
admin_permissions = {"read", "write", "delete", "admin"}
user_permissions = {"read", "write"}
if user_permissions.issubset(admin_permissions):
    print("ユーザー権限は管理者権限の範囲内")
```
### 競技プログラミングでの集合活用例

【図6-11：集合を使った効率的な解法例】

{% include panel.html type="info" title="問題例1: 共通要素の発見（概要）" content="2つのリストの共通要素を出力。集合の積集合で O(N+M) に高速化" %}
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1, set2 = set(list1), set(list2)
common = set1 & set2
print(sorted(common))  # [4, 5]
```

{% include panel.html type="steps" title="問題例2: 重複除去と順序保持" content="集合で既出判定しながら結果リストに追加" %}
```python
def remove_duplicates_keep_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique = remove_duplicates_keep_order(numbers)
print(unique)  # [3, 1, 4, 5, 9, 2, 6]
```

{% include panel.html type="steps" title="問題例3: グループの分類" content="和・積・差で4群に分解（両方／数学のみ／英語のみ／どちらも普通）" %}
```python
math_good = {"Alice", "Bob", "Charlie", "David"}
english_good = {"Bob", "Charlie", "Eve", "Frank"}
all_students = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"}

both_good = math_good & english_good
print("両方得意:", both_good)          # {"Bob", "Charlie"}

math_only = math_good - english_good
print("数学のみ:", math_only)            # {"Alice", "David"}

english_only = english_good - math_good
print("英語のみ:", english_only)         # {"Eve", "Frank"}

normal = all_students - (math_good | english_good)
print("どちらも普通:", normal)          # {"Grace"}
```
## 6.4 スタックとキューの考え方

データ構造の中でも、特に「データの取り出し順序」が重要な役割を果たすのが、スタックとキューだ。これらは、プログラムでよく使われる「後入れ先出し」と「先入れ先出し」という概念を具現化したものだ。

![図6-3：スタックとキューの活用]({{ site.baseurl }}/images/figure6-3-stack-queue-utilization.svg)

### Pythonでのスタック実装

【図6-13：Pythonでのスタック実装と活用】

{% include panel.html type="steps" title="基本操作（push/pop/peek）" content="リストの append/pop を用いる（末尾がトップ）／空チェックは if stack" %}
```python
# スタックの作成
stack = []

# 要素の追加（push）
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# 要素の取り出し（pop）
top = stack.pop()
print(top)    # 3（最後に追加した要素）
print(stack)  # [1, 2]

# 先頭要素の確認（取り出さない）
if stack:
    print(stack[-1])  # 2

# 空チェック
print(len(stack) == 0)  # False
```

{% include panel.html type="steps" title="使用例1: 括弧の対応チェック" content="開き括弧で push、閉じ括弧で pop／空や不一致で不正" %}
```python
def is_balanced_parentheses(s: str) -> bool:
    stack = []
    for ch in s:
        if ch == '(': stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced_parentheses("((()))"))  # True
print(is_balanced_parentheses("(()))"))   # False
```

{% include panel.html type="steps" title="使用例2: 逆ポーランド記法（RPN）" content="オペランドは push、演算子で2つ pop→結果を push" %}
```python
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop(); a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a // b)
        else:
            stack.append(int(token))
    return stack[0]

print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
```

🎯 スタックの典型的な使用例
```

### Pythonでのキュー実装

【図6-14：Pythonでのキュー実装と活用】

{% include panel.html type="steps" title="基本操作（enqueue/dequeue/peek）" content="deque の append/popleft を用いる（先頭がフロント）" %}
```python
from collections import deque

# キューの作成
queue = deque()

# 追加（enqueue）
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

# 取り出し（dequeue）
front = queue.popleft()
print(front)  # 1（最初に追加した要素）
print(queue)  # deque([2, 3])

# 先頭の確認（取り出さない）
if queue:
    print(queue[0])  # 2

# 空チェック
print(len(queue) == 0)  # False
```

{% include panel.html type="warn" title="リストをキューに使わない理由" content="pop(0) は全体シフトで O(N)。deque の popleft() は O(1) で高速" %}
```python
# 悪い例（遅い）
queue = []
queue.append(1); queue.append(2)
front = queue.pop(0)   # O(N)

# 良い例（速い）
from collections import deque
queue = deque()
queue.append(1); queue.append(2)
front = queue.popleft()  # O(1)
```

{% include panel.html type="steps" title="使用例: BFS とタスク処理" content="BFS で探索順を管理／先入れ先出しの処理待ち行列に最適" %}
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                queue.append(nb)
    return order

def process_tasks():
    q = deque()
    q.append("メール送信"); q.append("データ処理"); q.append("レポート作成")
    while q:
        current = q.popleft()
        print(f"実行中: {current}")
```

 
```

## 6.5 どのデータ構造を選ぶべき？

これまで様々なデータ構造を学んできたが、実際の問題を解くときに「どれを使えばいいの？」と迷うことがあるだろう。データ構造の選択は、プログラムの効率性と可読性に大きな影響を与える重要な判断だ。

![図6-1：データ構造選択ガイド]({{ site.baseurl }}/images/figure6-1-data-structure-selection-guide.svg)

```

### データ構造比較表

![図6-16：主要データ構造の性能・特徴比較]({{ site.baseurl }}/assets/diagrams/chapter6/figure6-16-data-structure-performance-comparison.svg)

### 問題別データ構造選択ガイド

![図6-17：典型的な問題パターンとデータ構造選択]({{ site.baseurl }}/assets/diagrams/chapter6/figure6-17-problem-patterns-data-structure-selection.svg)

## 次のステップへ

第7章では、いよいよ実際のAtCoderのABC問題に挑戦し、これまで学んだアルゴリズムとデータ構造を組み合わせた実戦的な問題解決を学ぶ。君が身につけた技術を、本物の競技で活用する時が来た！

君はもう、競技プログラミングで必要な基本的な道具を全て手に入れた。次の章では、その道具を使って実際の問題を解く楽しさと、競技での勝利の喜びを体験しよう！
