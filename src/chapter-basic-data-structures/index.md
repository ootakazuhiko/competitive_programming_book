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

```
【図6-1：リストの基本概念とメモリ構造】

📦 リストとは何か？
┌─────────────────────────────────────────────┐
│ 複数のデータを順番に並べて保存できる入れ物        │
│                                           │
│ numbers = [10, 25, 7, 33, 2]               │
│                                           │
│ メモリ上でのイメージ：                       │
│ ┌─────┬─────┬─────┬─────┬─────┐     │
│ │ 10  │ 25  │  7  │ 33  │  2  │     │
│ └─────┴─────┴─────┴─────┴─────┘     │
│   [0]   [1]   [2]   [3]   [4]  ← インデックス│
│                                           │
│ 特徴：                                     │
│ • 順番がある（左から0, 1, 2...）             │
│ • 重複する値でもOK                          │
│ • 異なる型の値も入れられる                   │
│ • 後から追加・削除・変更が可能                │
└─────────────────────────────────────────────┘
```

### リストの基本操作をマスターしよう

```
【図6-2：リスト操作の完全ガイド】

📋 作成と初期化
┌─────────────────────────────────────────────┐
│ # 空のリスト作成                             │
│ empty_list = []                              │
│ empty_list = list()                          │
│                                           │
│ # 値を入れてリスト作成                        │
│ fruits = ["apple", "banana", "cherry"]       │
│ numbers = [1, 2, 3, 4, 5]                   │
│                                           │
│ # 同じ値で初期化                             │
│ zeros = [0] * 5          # [0, 0, 0, 0, 0]  │
│ matrix = [[0] * 3 for _ in range(2)]         │
│ # [[0, 0, 0], [0, 0, 0]]                    │
└─────────────────────────────────────────────┘

🔍 要素へのアクセス
┌─────────────────────────────────────────────┐
│ numbers = [10, 25, 7, 33, 2]                │
│                                           │
│ # 前から数える（正のインデックス）             │
│ print(numbers[0])        # 10（最初の要素） │
│ print(numbers[2])        # 7（3番目の要素）  │
│ print(numbers[4])        # 2（最後の要素）   │
│                                           │
│ # 後ろから数える（負のインデックス）           │
│ print(numbers[-1])       # 2（最後の要素）   │
│ print(numbers[-2])       # 33（後ろから2番目）│
│                                           │
│ # 範囲指定（スライス）                       │
│ print(numbers[1:4])      # [25, 7, 33]     │
│ print(numbers[:3])       # [10, 25, 7]     │
│ print(numbers[2:])       # [7, 33, 2]      │
└─────────────────────────────────────────────┘

➕ 要素の追加・挿入
┌─────────────────────────────────────────────┐
│ fruits = ["apple", "banana"]                │
│                                           │
│ # 末尾に追加                                │
│ fruits.append("cherry")                     │
│ print(fruits)  # ["apple", "banana", "cherry"]│
│                                           │
│ # 指定位置に挿入                            │
│ fruits.insert(1, "orange")                  │
│ print(fruits)  # ["apple", "orange", "banana", "cherry"]│
│                                           │
│ # 複数要素を一度に追加                       │
│ fruits.extend(["grape", "melon"])           │
│ print(fruits)  # ["apple", "orange", "banana", "cherry", "grape", "melon"]│
└─────────────────────────────────────────────┘

❌ 要素の削除・変更
┌─────────────────────────────────────────────┐
│ numbers = [10, 25, 7, 33, 2, 25]            │
│                                           │
│ # 値を指定して削除（最初に見つかったもの）      │
│ numbers.remove(25)                          │
│ print(numbers)  # [10, 7, 33, 2, 25]       │
│                                           │
│ # インデックスを指定して削除                 │
│ del numbers[0]                              │
│ print(numbers)  # [7, 33, 2, 25]           │
│                                           │
│ # 末尾要素を削除して取得                     │
│ last = numbers.pop()                        │
│ print(last)     # 25                       │
│ print(numbers)  # [7, 33, 2]               │
│                                           │
│ # 要素の変更                               │
│ numbers[0] = 100                            │
│ print(numbers)  # [100, 33, 2]             │
└─────────────────────────────────────────────┘
```

### 二次元リスト（表形式データ）の活用

```
【図6-3：二次元リストの構造と活用法】

📊 二次元リストの基本概念
┌─────────────────────────────────────────────┐
│ grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    │
│                                           │
│ 視覚的表現：                                │
│     列0  列1  列2  ← 列インデックス           │
│ 行0  1    2    3                          │
│ 行1  4    5    6                          │
│ 行2  7    8    9                          │
│ ↑                                         │
│ 行インデックス                             │
│                                           │
│ アクセス方法：                              │
│ print(grid[0][0])    # 1                   │
│ print(grid[1][2])    # 6                   │
│ print(grid[2][1])    # 8                   │
└─────────────────────────────────────────────┘

🏗️ 二次元リストの作成方法
┌─────────────────────────────────────────────┐
│ # 方法1: 直接作成                            │
│ matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  │
│                                           │
│ # 方法2: 内包表記を使用（推奨）               │
│ rows, cols = 3, 4                          │
│ matrix = [[0 for _ in range(cols)] for _ in range(rows)]│
│ # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]│
│                                           │
│ # 方法3: 値を入力しながら作成                 │
│ matrix = []                                │
│ for i in range(3):                         │
│     row = list(map(int, input().split()))  │
│     matrix.append(row)                     │
│                                           │
│ ❌ 危険な方法（避けるべき）：                 │
│ wrong = [[0] * 3] * 3  # 参照が共有されて問題発生│
└─────────────────────────────────────────────┘

🔄 二次元リストの操作パターン
┌─────────────────────────────────────────────┐
│ # 全要素への処理                             │
│ for i in range(len(matrix)):                │
│     for j in range(len(matrix[i])):         │
│         print(f"({i},{j}): {matrix[i][j]}") │
│                                           │
│ # より Pythonic な書き方                     │
│ for i, row in enumerate(matrix):            │
│     for j, value in enumerate(row):         │
│         print(f"({i},{j}): {value}")        │
│                                           │
│ # 行ごとの処理                              │
│ for row in matrix:                          │
│     print(sum(row))  # 各行の合計           │
│                                           │
│ # 列ごとの処理                              │
│ for j in range(len(matrix[0])):             │
│     col_sum = sum(matrix[i][j] for i in range(len(matrix)))│
│     print(col_sum)   # 各列の合計           │
└─────────────────────────────────────────────┘
```

### 競技プログラミングでのリスト活用例

```
【図6-4：実際の問題でのリスト活用パターン】

🎯 問題例1: 配列の最大値・最小値
┌─────────────────────────────────────────────┐
│ 問題：N個の整数が与えられる。最大値と最小値を出力せよ。│
│                                           │
│ 入力例：                                   │
│ 5                                          │
│ 3 1 4 1 5                                 │
│                                           │
│ 解法：                                     │
│ n = int(input())                           │
│ numbers = list(map(int, input().split()))  │
│ print(max(numbers), min(numbers))          │
│                                           │
│ 💡 ポイント：                              │
│ • リストに一度格納してから処理              │
│ • Pythonの組み込み関数max(), min()を活用    │
└─────────────────────────────────────────────┘

🎯 問題例2: 累積和の計算
┌─────────────────────────────────────────────┐
│ 問題：配列の各要素について、その位置までの累積和を求めよ。│
│                                           │
│ 入力例：                                   │
│ [1, 2, 3, 4, 5]                           │
│                                           │
│ 出力例：                                   │
│ [1, 3, 6, 10, 15]                         │
│                                           │
│ 解法：                                     │
│ numbers = [1, 2, 3, 4, 5]                 │
│ cumsum = []                               │
│ total = 0                                 │
│ for num in numbers:                       │
│     total += num                          │
│     cumsum.append(total)                  │
│ print(cumsum)                             │
│                                           │
│ 💡 応用：範囲合計をO(1)で計算可能            │
└─────────────────────────────────────────────┘

🎯 問題例3: 二次元グリッドの探索
┌─────────────────────────────────────────────┐
│ 問題：H×Wのグリッドで、'#'の隣接する'.'の個数を数えよ。│
│                                           │
│ 入力例：                                   │
│ 3 3                                       │
│ .#.                                       │
│ ###                                       │
│ .#.                                       │
│                                           │
│ 解法：                                     │
│ h, w = map(int, input().split())           │
│ grid = []                                 │
│ for _ in range(h):                        │
│     grid.append(input())                  │
│                                           │
│ count = 0                                 │
│ directions = [(0,1), (0,-1), (1,0), (-1,0)]│
│ for i in range(h):                        │
│     for j in range(w):                    │
│         if grid[i][j] == '#':             │
│             for di, dj in directions:     │
│                 ni, nj = i + di, j + dj   │
│                 if 0 <= ni < h and 0 <= nj < w:│
│                     if grid[ni][nj] == '.':│
│                         count += 1        │
│ print(count)                              │
└─────────────────────────────────────────────┘
```

## 6.2 辞書（ディクショナリ）で高速検索

リストは順番にデータを管理するのに適しているが、「特定の値を高速で検索したい」「データに名前を付けて管理したい」という場合には、辞書（ディクショナリ）が威力を発揮する。

![図6-2：リストvs辞書vs集合比較]({{ site.baseurl }}/images/figure6-2-list-dict-set-comparison.svg)

### 辞書の基本操作をマスターしよう

```
【図6-6：辞書操作の完全ガイド】

🏗️ 辞書の作成方法
┌─────────────────────────────────────────────┐
│ # 空の辞書作成                               │
│ empty_dict = {}                              │
│ empty_dict = dict()                          │
│                                           │
│ # 値を入れて辞書作成                         │
│ student = {"name": "Alice", "age": 14, "grade": "8th"}│
│ scores = {"math": 85, "english": 92, "science": 78}│
│                                           │
│ # dict()関数を使った作成                     │
│ colors = dict(red="赤", blue="青", green="緑")│
│                                           │
│ # リストのペアから作成                       │
│ items = [("apple", 100), ("banana", 80), ("cherry", 120)]│
│ prices = dict(items)                         │
│ print(prices)  # {"apple": 100, "banana": 80, "cherry": 120}│
└─────────────────────────────────────────────┘

🔍 要素へのアクセスと操作
┌─────────────────────────────────────────────┐
│ student = {"name": "Alice", "age": 14, "grade": "8th"}│
│                                           │
│ # 値の取得                                   │
│ print(student["name"])       # Alice        │
│ print(student.get("age"))    # 14           │
│ print(student.get("height", "不明"))  # 不明 │
│                                           │
│ # 値の変更・追加                             │
│ student["age"] = 15          # 変更         │
│ student["height"] = 160      # 追加         │
│ print(student)  # {"name": "Alice", "age": 15, "grade": "8th", "height": 160}│
│                                           │
│ # 要素の削除                                │
│ del student["height"]        # キー指定削除  │
│ grade = student.pop("grade") # 削除して値取得│
│ print(grade)                 # 8th          │
│ print(student)               # {"name": "Alice", "age": 15}│
└─────────────────────────────────────────────┘

🔄 辞書の反復処理
┌─────────────────────────────────────────────┐
│ scores = {"math": 85, "english": 92, "science": 78}│
│                                           │
│ # キーのみ取得                               │
│ for subject in scores:                      │
│     print(subject)                          │
│ # math, english, science                    │
│                                           │
│ # 値のみ取得                                │
│ for score in scores.values():               │
│     print(score)                            │
│ # 85, 92, 78                               │
│                                           │
│ # キーと値のペア取得                         │
│ for subject, score in scores.items():       │
│     print(f"{subject}: {score}")            │
│ # math: 85, english: 92, science: 78       │
│                                           │
│ # 条件付き処理                              │
│ high_scores = {k: v for k, v in scores.items() if v >= 80}│
│ print(high_scores)  # {"math": 85, "english": 92}│
└─────────────────────────────────────────────┘
```

### 競技プログラミングでの辞書活用パターン

```
【図6-7：辞書を使った典型的な解法パターン】

🎯 パターン1: カウント処理
┌─────────────────────────────────────────────┐
│ 問題：文字列中の各文字の出現回数を数えよ      │
│                                           │
│ 入力：programming                          │
│ 出力：p:1, r:2, o:1, g:2, a:1, m:2, i:1, n:1│
│                                           │
│ 解法：                                     │
│ text = "programming"                       │
│ char_count = {}                            │
│ for char in text:                          │
│     char_count[char] = char_count.get(char, 0) + 1│
│                                           │
│ for char, count in char_count.items():     │
│     print(f"{char}:{count}")               │
│                                           │
│ 💡 Pythonらしい書き方：                     │
│ from collections import Counter            │
│ char_count = Counter(text)                 │
│ print(dict(char_count))                    │
└─────────────────────────────────────────────┘

🎯 パターン2: グループ分け
┌─────────────────────────────────────────────┐
│ 問題：学生リストを学年でグループ分けせよ      │
│                                           │
│ 入力：[("Alice", "8th"), ("Bob", "7th"), ("Charlie", "8th")]│
│                                           │
│ 解法：                                     │
│ students = [("Alice", "8th"), ("Bob", "7th"), ("Charlie", "8th")]│
│ groups = {}                                │
│ for name, grade in students:               │
│     if grade not in groups:                │
│         groups[grade] = []                 │
│     groups[grade].append(name)             │
│                                           │
│ print(groups)                              │
│ # {"8th": ["Alice", "Charlie"], "7th": ["Bob"]}│
│                                           │
│ 💡 defaultdictを使った改良版：               │
│ from collections import defaultdict        │
│ groups = defaultdict(list)                 │
│ for name, grade in students:               │
│     groups[grade].append(name)             │
└─────────────────────────────────────────────┘

🎯 パターン3: 高速な存在確認・検索
┌─────────────────────────────────────────────┐
│ 問題：許可されたユーザーIDかどうかを高速判定せよ│
│                                           │
│ 解法：                                     │
│ allowed_users = {"alice", "bob", "charlie", "david"}│
│                                           │
│ def is_allowed(user_id):                   │
│     return user_id in allowed_users        │
│                                           │
│ # 使用例                                   │
│ print(is_allowed("alice"))     # True      │
│ print(is_allowed("eve"))       # False     │
│                                           │
│ 💡 リストとの比較：                         │
│ # リスト版（遅い：O(N)）                    │
│ allowed_list = ["alice", "bob", "charlie", "david"]│
│ def is_allowed_slow(user_id):              │
│     return user_id in allowed_list         │
│                                           │
│ # 辞書・集合版（速い：O(1)）                │
│ # 大量データでは圧倒的な差が出る              │
└─────────────────────────────────────────────┘

🎯 パターン4: メモ化（動的プログラミング）
┌─────────────────────────────────────────────┐
│ 問題：フィボナッチ数列のN番目を効率的に計算せよ │
│                                           │
│ 普通の再帰（遅い）：                        │
│ def fibonacci_slow(n):                     │
│     if n <= 1:                             │
│         return n                           │
│     return fibonacci_slow(n-1) + fibonacci_slow(n-2)│
│                                           │
│ メモ化版（速い）：                          │
│ memo = {}                                  │
│ def fibonacci_fast(n):                     │
│     if n in memo:                          │
│         return memo[n]                     │
│     if n <= 1:                             │
│         return n                           │
│     memo[n] = fibonacci_fast(n-1) + fibonacci_fast(n-2)│
│     return memo[n]                         │
│                                           │
│ 💡 効果：                                  │
│ fibonacci_slow(30)  # 数秒かかる           │
│ fibonacci_fast(30)  # 瞬時に計算           │
└─────────────────────────────────────────────┘
```

## 6.3 集合（セット）で重複を管理

データを扱っていると、「重複する要素を除去したい」「2つのグループの共通部分を知りたい」といった場面に遭遇する。そんなときに威力を発揮するのが、集合（セット）だ。

```
【図6-8：集合の基本概念と数学的背景】

🔢 集合とは何か？
┌─────────────────────────────────────────────┐
│ 数学での集合：{1, 2, 3, 4, 5}                │
│ Pythonでの集合：{1, 2, 3, 4, 5}              │
│                                           │
│ 特徴：                                     │
│ ✅ 重複する要素がない（自動的に除去）         │
│ ✅ 順序がない（インデックスでアクセス不可）    │
│ ✅ 高速な存在確認（O(1)）                    │
│ ✅ 集合演算（和集合、積集合など）が可能       │
│                                           │
│ 例：重複除去の自動化                        │
│ numbers = [1, 2, 2, 3, 3, 3, 4, 5]         │
│ unique = set(numbers)                      │
│ print(unique)  # {1, 2, 3, 4, 5}          │
└─────────────────────────────────────────────┘
```

### 集合の基本操作

```
【図6-9：集合操作の完全ガイド】

🏗️ 集合の作成
┌─────────────────────────────────────────────┐
│ # 空の集合作成                               │
│ empty_set = set()                            │
│ # empty_set = {}  # これは辞書になってしまう！│
│                                           │
│ # 値を入れて集合作成                         │
│ fruits = {"apple", "banana", "cherry"}       │
│ numbers = {1, 2, 3, 4, 5}                   │
│                                           │
│ # リストから集合作成（重複除去）              │
│ numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]     │
│ unique_numbers = set(numbers_list)           │
│ print(unique_numbers)  # {1, 2, 3, 4, 5}    │
│                                           │
│ # 文字列から集合作成                         │
│ chars = set("programming")                   │
│ print(chars)  # {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'}│
└─────────────────────────────────────────────┘

➕ 要素の追加・削除
┌─────────────────────────────────────────────┐
│ fruits = {"apple", "banana"}                 │
│                                           │
│ # 要素の追加                                │
│ fruits.add("cherry")                        │
│ print(fruits)  # {"apple", "banana", "cherry"}│
│                                           │
│ # 複数要素の追加                            │
│ fruits.update(["grape", "melon"])           │
│ fruits.update({"orange", "kiwi"})           │
│ print(fruits)  # {"apple", "banana", "cherry", "grape", "melon", "orange", "kiwi"}│
│                                           │
│ # 要素の削除                                │
│ fruits.remove("banana")     # ない場合エラー │
│ fruits.discard("pineapple") # ない場合無視   │
│ popped = fruits.pop()       # 任意の要素削除 │
│ print(popped)                               │
│                                           │
│ # 全削除                                   │
│ fruits.clear()                              │
│ print(fruits)  # set()                     │
└─────────────────────────────────────────────┘

🔍 存在確認と反復処理
┌─────────────────────────────────────────────┐
│ languages = {"Python", "Java", "C++", "JavaScript"}│
│                                           │
│ # 存在確認（高速：O(1)）                     │
│ print("Python" in languages)      # True   │
│ print("Ruby" in languages)        # False  │
│                                           │
│ # 要素数の取得                              │
│ print(len(languages))              # 4      │
│                                           │
│ # 全要素への反復処理                         │
│ for lang in languages:                      │
│     print(f"I can use {lang}")              │
│                                           │
│ # 条件付きフィルタリング                     │
│ short_names = {lang for lang in languages if len(lang) <= 4}│
│ print(short_names)  # {"Java", "C++"}      │
└─────────────────────────────────────────────┘
```

### 集合演算の活用

```
【図6-10：集合演算による高度なデータ処理】

🔢 基本的な集合演算
┌─────────────────────────────────────────────┐
│ A = {1, 2, 3, 4, 5}                         │
│ B = {4, 5, 6, 7, 8}                         │
│                                           │
│ # 和集合（union）：AまたはBに含まれる要素     │
│ union = A | B                               │
│ # または A.union(B)                         │
│ print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}   │
│                                           │
│ # 積集合（intersection）：AとBの両方に含まれる要素│
│ intersection = A & B                        │
│ # または A.intersection(B)                  │
│ print(intersection)  # {4, 5}              │
│                                           │
│ # 差集合（difference）：Aに含まれBに含まれない要素│
│ difference = A - B                          │
│ # または A.difference(B)                    │
│ print(difference)  # {1, 2, 3}             │
│                                           │
│ # 対称差集合（symmetric_difference）：どちらか一方のみに含まれる│
│ sym_diff = A ^ B                            │
│ # または A.symmetric_difference(B)          │
│ print(sym_diff)  # {1, 2, 3, 6, 7, 8}      │
└─────────────────────────────────────────────┘

📊 集合関係の判定
┌─────────────────────────────────────────────┐
│ A = {1, 2, 3}                               │
│ B = {1, 2, 3, 4, 5}                         │
│ C = {6, 7, 8}                               │
│                                           │
│ # 部分集合の判定                            │
│ print(A.issubset(B))       # True（AはBの部分集合）│
│ print(B.issubset(A))       # False         │
│                                           │
│ # 上位集合の判定                            │
│ print(B.issuperset(A))     # True（BはAの上位集合）│
│                                           │
│ # 素集合の判定（共通要素なし）                │
│ print(A.isdisjoint(C))     # True          │
│ print(A.isdisjoint(B))     # False         │
│                                           │
│ 💡 応用例：権限管理システム                  │
│ admin_permissions = {"read", "write", "delete", "admin"}│
│ user_permissions = {"read", "write"}        │
│ if user_permissions.issubset(admin_permissions):│
│     print("ユーザーの権限は管理者権限の範囲内です")│
└─────────────────────────────────────────────┘
```

### 競技プログラミングでの集合活用例

```
【図6-11：集合を使った効率的な解法例】

🎯 問題例1: 共通する要素の発見
┌─────────────────────────────────────────────┐
│ 問題：2つのリストに共通して含まれる要素を全て出力せよ│
│                                           │
│ 入力：                                     │
│ list1 = [1, 2, 3, 4, 5]                   │
│ list2 = [4, 5, 6, 7, 8]                   │
│                                           │
│ 解法：                                     │
│ set1 = set(list1)                          │
│ set2 = set(list2)                          │
│ common = set1 & set2                       │
│ print(sorted(common))  # [4, 5]            │
│                                           │
│ 💡 リストでやると非効率：                    │
│ # O(N×M)の時間がかかる                      │
│ common = [x for x in list1 if x in list2]  │
│ # 集合なら O(N+M)で高速処理                 │
└─────────────────────────────────────────────┘

🎯 問題例2: 重複除去と順序保持
┌─────────────────────────────────────────────┐
│ 問題：リストから重複を除去しつつ、最初の出現順序を保持せよ│
│                                           │
│ 入力：[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]       │
│ 出力：[3, 1, 4, 5, 9, 2, 6]                │
│                                           │
│ 解法：                                     │
│ def remove_duplicates_keep_order(lst):     │
│     seen = set()                           │
│     result = []                            │
│     for item in lst:                       │
│         if item not in seen:               │
│             seen.add(item)                 │
│             result.append(item)            │
│     return result                          │
│                                           │
│ numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]   │
│ unique = remove_duplicates_keep_order(numbers)│
│ print(unique)  # [3, 1, 4, 5, 9, 2, 6]     │
└─────────────────────────────────────────────┘

🎯 問題例3: グループの分類
┌─────────────────────────────────────────────┐
│ 問題：学生を「数学が得意」「英語が得意」「両方得意」「どちらも普通」│
│       の4グループに分類せよ                    │
│                                           │
│ 解法：                                     │
│ math_good = {"Alice", "Bob", "Charlie", "David"}│
│ english_good = {"Bob", "Charlie", "Eve", "Frank"}│
│ all_students = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"}│
│                                           │
│ # 両方得意                                 │
│ both_good = math_good & english_good       │
│ print("両方得意:", both_good)               │
│ # {"Bob", "Charlie"}                       │
│                                           │
│ # 数学のみ得意                             │
│ math_only = math_good - english_good       │
│ print("数学のみ:", math_only)               │
│ # {"Alice", "David"}                       │
│                                           │
│ # 英語のみ得意                             │
│ english_only = english_good - math_good    │
│ print("英語のみ:", english_only)            │
│ # {"Eve", "Frank"}                         │
│                                           │
│ # どちらも普通                             │
│ normal = all_students - (math_good | english_good)│
│ print("どちらも普通:", normal)               │
│ # {"Grace"}                                │
└─────────────────────────────────────────────┘
```

## 6.4 スタックとキューの考え方

データ構造の中でも、特に「データの取り出し順序」が重要な役割を果たすのが、スタックとキューだ。これらは、プログラムでよく使われる「後入れ先出し」と「先入れ先出し」という概念を具現化したものだ。

![図6-3：スタックとキューの活用]({{ site.baseurl }}/images/figure6-3-stack-queue-utilization.svg)

### Pythonでのスタック実装

```
【図6-13：Pythonでのスタック実装と活用】

📚 リストを使ったスタック実装
┌─────────────────────────────────────────────┐
│ # スタックの作成                             │
│ stack = []                                  │
│                                           │
│ # 要素の追加（push）                         │
│ stack.append(1)                            │
│ stack.append(2)                            │
│ stack.append(3)                            │
│ print(stack)  # [1, 2, 3]                 │
│                                           │
│ # 要素の取り出し（pop）                      │
│ top = stack.pop()                          │
│ print(top)    # 3（最後に追加した要素）     │
│ print(stack)  # [1, 2]                    │
│                                           │
│ # 先頭要素の確認（取り出さない）              │
│ if stack:                                  │
│     print(stack[-1])  # 2                 │
│                                           │
│ # スタックが空かどうかの確認                 │
│ print(len(stack) == 0)  # False           │
└─────────────────────────────────────────────┘

🎯 スタックの典型的な使用例
┌─────────────────────────────────────────────┐
│ 例1: 括弧の対応チェック                      │
│ def is_balanced_parentheses(s):            │
│     stack = []                             │
│     for char in s:                         │
│         if char == '(':                    │
│             stack.append(char)             │
│         elif char == ')':                  │
│             if not stack:                  │
│                 return False               │
│             stack.pop()                    │
│     return len(stack) == 0                 │
│                                           │
│ print(is_balanced_parentheses("((()))"))  # True│
│ print(is_balanced_parentheses("(()))"))   # False│
│                                           │
│ 例2: 逆ポーランド記法の計算                  │
│ def eval_rpn(tokens):                      │
│     stack = []                             │
│     for token in tokens:                   │
│         if token in ['+', '-', '*', '/']:  │
│             b = stack.pop()                │
│             a = stack.pop()                │
│             if token == '+': stack.append(a + b)│
│             elif token == '-': stack.append(a - b)│
│             elif token == '*': stack.append(a * b)│
│             elif token == '/': stack.append(a // b)│
│         else:                              │
│             stack.append(int(token))       │
│     return stack[0]                        │
│                                           │
│ print(eval_rpn(["2", "1", "+", "3", "*"])) # 9│
└─────────────────────────────────────────────┘
```

### Pythonでのキュー実装

```
【図6-14：Pythonでのキュー実装と活用】

🚶 dequeを使った効率的なキュー実装
┌─────────────────────────────────────────────┐
│ from collections import deque               │
│                                           │
│ # キューの作成                              │
│ queue = deque()                            │
│                                           │
│ # 要素の追加（enqueue）                     │
│ queue.append(1)                            │
│ queue.append(2)                            │
│ queue.append(3)                            │
│ print(queue)  # deque([1, 2, 3])          │
│                                           │
│ # 要素の取り出し（dequeue）                  │
│ front = queue.popleft()                    │
│ print(front)  # 1（最初に追加した要素）     │
│ print(queue)  # deque([2, 3])             │
│                                           │
│ # 先頭要素の確認（取り出さない）              │
│ if queue:                                  │
│     print(queue[0])  # 2                  │
│                                           │
│ # キューが空かどうかの確認                   │
│ print(len(queue) == 0)  # False           │
└─────────────────────────────────────────────┘

⚠️ リストをキューとして使うべきでない理由
┌─────────────────────────────────────────────┐
│ # ❌ 効率が悪い方法                          │
│ queue = []                                 │
│ queue.append(1)    # O(1) - 問題なし       │
│ queue.append(2)    # O(1) - 問題なし       │
│ front = queue.pop(0)  # O(N) - 遅い！      │
│                                           │
│ # ✅ 効率的な方法                           │
│ from collections import deque              │
│ queue = deque()                            │
│ queue.append(1)       # O(1)              │
│ queue.append(2)       # O(1)              │
│ front = queue.popleft()  # O(1) - 高速！   │
│                                           │
│ 💡 理由：                                  │
│ リストのpop(0)は全要素を左にシフトする必要があり、│
│ 要素数Nに比例した時間がかかる（O(N)）        │
│ dequeのpopleft()は常に一定時間（O(1)）      │
└─────────────────────────────────────────────┘

🎯 キューの典型的な使用例
┌─────────────────────────────────────────────┐
│ 例1: 幅優先探索（BFS）                       │
│ def bfs(graph, start):                     │
│     visited = set()                        │
│     queue = deque([start])                 │
│     result = []                            │
│                                           │
│     while queue:                           │
│         node = queue.popleft()             │
│         if node not in visited:            │
│             visited.add(node)              │
│             result.append(node)            │
│             for neighbor in graph[node]:   │
│                 if neighbor not in visited:│
│                     queue.append(neighbor) │
│     return result                          │
│                                           │
│ 例2: タスクの順番処理                        │
│ def process_tasks():                       │
│     task_queue = deque()                   │
│                                           │
│     # タスクの追加                          │
│     task_queue.append("メール送信")         │
│     task_queue.append("データ処理")         │
│     task_queue.append("レポート作成")       │
│                                           │
│     # タスクの順次処理                      │
│     while task_queue:                      │
│         current_task = task_queue.popleft()│
│         print(f"実行中: {current_task}")    │
│         # 実際の処理はここに書く             │
└─────────────────────────────────────────────┘
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
