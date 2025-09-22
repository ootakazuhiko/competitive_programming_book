---
title: "第5章：基本アルゴリズムの道具箱"
layout: book
order: 5
checklist:
  - 全探索/条件分岐/ソート/貪欲の適用場面を説明できる
  - 計算量の目安を見積もれる
pitfalls:
  - 二重/三重ループの境界条件ミス
  - ソート順や安定性の取り違え
exercises:
  - { level: A, text: "二重ループでペアの和を数える", link: "https://atcoder.jp/contests/abc144/tasks/abc144_b" }
  - { level: B, text: "ソートを用いた実装", link: "https://atcoder.jp/contests/abc085/tasks/abc085_b" }
  - { level: B, text: "貪欲的な選択", link: "https://atcoder.jp/contests/abc085/tasks/abc085_c" }
---

<!-- 
本章は「中学生向け競技プログラミング入門書」の一部であり、
CC BY-NC-SA 4.0ライセンスの下で提供されます。
商用利用は事前許諾が必要です。
詳細：../../LICENSE.md
-->

# 第5章：基本アルゴリズムの道具箱

## 章の学習目標

この章を読み終わることで、以下ができるようになります：
- 全探索による確実な問題解決ができるようになる
- 複雑な条件分岐を整理して実装できるようになる  
- 数学的な公式・性質を問題解決に活用できるようになる
- 文字列処理の基本パターンをマスターできるようになる
- ソートを効果的に使った問題解決ができるようになる
- 貪欲法による最適化問題の解法を理解できるようになる

入出力処理をマスターした君は、いよいよ問題解決の「道具」を手に入れる段階に来た。大工さんが金槌やのこぎりを使って家を建てるように、プログラマーはアルゴリズムという道具を使って問題を解決する。この章では、競技プログラミングで最もよく使われる基本的な道具たちを学ぼう。

## 5.1 全探索（しらみつぶし）で解いてみよう

### 全探索の考え方（Scratchとの関連）

![図5-1：Scratchのゲーム開発と全探索の関係]({{ site.baseurl }}/assets/diagrams/chapter5/figure5-1-scratch-brute-force-relationship.svg)

全探索（Brute Force）は、最もシンプルで確実なアルゴリズムだ。「全ての可能性を試して、条件に合うものを見つける」という、とても素直な考え方だ。

### 全探索が有効な条件

全探索は確実だが、時間がかかる方法でもある。いつ使うべきかを理解しよう：

![図5-2：全探索の適用条件]({{ site.baseurl }}/assets/diagrams/chapter5/figure5-2-brute-force-application-conditions.svg)

### 具体的な全探索の実装

![図5-3：全探索実装パターン]({{ site.baseurl }}/assets/diagrams/chapter5/figure5-3-brute-force-implementation-pattern.svg)

### 各桁の和を求める処理の詳細

上記のコードで重要な部分である「各桁の和」の計算について、詳しく理解しよう：

```
【図5-4：数値の各桁分解プロセス】

例：数値 1234 の各桁の和を求める

Step 1: temp = 1234, digit_sum = 0
temp % 10 = 4  ← 最下位桁
digit_sum = 0 + 4 = 4
temp = temp // 10 = 123

Step 2: temp = 123, digit_sum = 4  
temp % 10 = 3  ← 最下位桁
digit_sum = 4 + 3 = 7
temp = temp // 10 = 12

Step 3: temp = 12, digit_sum = 7
temp % 10 = 2  ← 最下位桁  
digit_sum = 7 + 2 = 9
temp = temp // 10 = 1

Step 4: temp = 1, digit_sum = 9
temp % 10 = 1  ← 最下位桁
digit_sum = 9 + 1 = 10
temp = temp // 10 = 0

Step 5: temp = 0 → ループ終了
結果: digit_sum = 10

💡 重要な演算子：
• % (mod): 余りを求める → 最下位桁の取得
• // (整数除算): 小数切り捨ての除算 → 最下位桁の除去
```

### より複雑な全探索の例

<figure>
  <img src="{{ '/assets/diagrams/generated/ch5-bruteforce.svg' | relative_url }}" alt="図5-x：全探索の基本フロー">
  <figcaption>図5-x：全探索の基本フロー</figcaption>
</figure>

```
【図5-5：二重ループによる全探索】

問題例：「N個の数から2つ選んで、その和がKになる組み合わせの個数を求める」

入力例：
4 7
1 3 4 6

出力例：
2

解法分析：
{% capture plan %}
- 全ての i < j の組を調べる
- arr[i] + arr[j] == k を満たす組をカウント
{% endcapture %}
{% include panel.html type="plan" title="🎯 方針" content=plan %}

{% capture steps %}
1. i と j の全組合せ（i < j）を列挙  
2. 和が k か判定  
3. 条件を満たす組をカウント
{% endcapture %}
{% include panel.html type="steps" title="📝 手順" content=steps %}

{% capture examples %}
• (0,1): 1+3=4 ≠ 7  
• (0,3): 1+6=7 = 7 ✅  
• (1,2): 3+4=7 = 7 ✅  
→ 合計: 2個
{% endcapture %}
{% include panel.html type="info" title="🔍 具体例" content=examples %}

実装：
<figure class="pseudocode">
<figcaption>二重ループによる全探索（Python）</figcaption>

```python
n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i + 1, n):  # i < j を保証
        if arr[i] + arr[j] == k:
            count += 1

print(count)
```
</figure>

💡 重要なポイント：
• range(i + 1, n) により、i < j を保証
• これで重複や同じ要素の組み合わせを避けられる
• 計算量は O(N^2) - N個から2つ選ぶ組み合わせ
```

## 5.2 条件分岐で場合分けしよう

### 複雑な条件分岐の整理法

競技プログラミングでは、複数の条件が組み合わさった複雑な場合分けが必要になることがある。整理して考える方法を学ぼう。

```
【図5-6：条件分岐の段階的構築】

問題例：「点数に応じて成績を判定」  
90点以上：A, 80点以上：B, 70点以上：C, 60点以上：D, 未満：F
```

<figure class="pseudocode">
  <figcaption>悪い例（冗長な条件）</figcaption>
  <pre><code class="language-python">if score &gt;= 90:
    grade = "A"
elif score &gt;= 80 and score &lt; 90:  # 不要な条件
    grade = "B"
elif score &gt;= 70 and score &lt; 80:  # 不要な条件
    grade = "C"
elif score &gt;= 60 and score &lt; 70:  # 不要な条件
    grade = "D"
else:
    grade = "F"</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>良い例（段階的な条件分岐）</figcaption>
  <pre><code class="language-python">if score &gt;= 90:
    grade = "A"
elif score &gt;= 80:   # 既に90未満が確定
    grade = "B"
elif score &gt;= 70:   # 既に80未満が確定
    grade = "C"
elif score &gt;= 60:   # 既に70未満が確定
    grade = "D"
else:                 # 60未満
    grade = "F"</code></pre>
</figure>

{% capture cond_points %}
• elif では前の条件が偽であることが保証される  
• 冗長な上限条件は不要（流れで確定）  
• 上から順に条件を評価する設計を意識
{% endcapture %}
{% include panel.html type="info" title="💡 ポイント" content=cond_points %}

### 複雑な論理演算の活用

```
【図5-7：論理演算子の効果的な使用】
```

{% capture logic_ops %}
基本的な論理演算子  
• and: 両方が真の場合に真  
• or:  どちらかが真の場合に真  
• not: 真偽を反転
{% endcapture %}
{% include panel.html type="steps" title="論理演算子の基本" content=logic_ops %}

<figure class="pseudocode">
  <figcaption>実践例：うるう年の判定（2通り）</figcaption>
  <pre><code class="language-python"># 複雑だが正確な条件
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("うるう年")
else:
    print("平年")

# より分かりやすい段階的判定
if year % 400 == 0:
    print("うるう年")
elif year % 100 == 0:
    print("平年")
elif year % 4 == 0:
    print("うるう年")
else:
    print("平年")</code></pre>
</figure>

### 場合分けの可視化技法

複雑な条件分岐は、表や図で整理すると理解しやすい：

```
【図5-8：条件分岐の表による整理】

問題例：「3つの数a, b, cの大小関係を判定」

可能なパターン（6通り）：
┌─────────────────────────────────────────────┐
│ パターン1: a ≥ b ≥ c  → "a b c"             │
│ パターン2: a ≥ c ≥ b  → "a c b"             │
│ パターン3: b ≥ a ≥ c  → "b a c"             │
│ パターン4: b ≥ c ≥ a  → "b c a"             │
│ パターン5: c ≥ a ≥ b  → "c a b"             │
│ パターン6: c ≥ b ≥ a  → "c b a"             │
└─────────────────────────────────────────────┘

実装方法1: 全パターンを条件分岐
┌─────────────────────────────────────────────┐
│ a, b, c = map(int, input().split())           │
│                                             │
│ if a >= b >= c:                              │
│     print(a, b, c)                           │
│ elif a >= c >= b:                            │
│     print(a, c, b)                           │
│ elif b >= a >= c:                            │
│     print(b, a, c)                           │
│ elif b >= c >= a:                            │
│     print(b, c, a)                           │
│ elif c >= a >= b:                            │
│     print(c, a, b)                           │
│ else:  # c >= b >= a                         │
│     print(c, b, a)                           │
└─────────────────────────────────────────────┘

実装方法2: ソートを活用（より簡潔）
┌─────────────────────────────────────────────┐
│ a, b, c = map(int, input().split())           │
│ numbers = [a, b, c]                          │
│ numbers.sort(reverse=True)  # 降順ソート     │
│ print(*numbers)                              │
└─────────────────────────────────────────────┘

💡 学習ポイント：
• 複雑な条件分岐は、より簡潔な方法がないか検討する
• ソートなど既存の機能を活用できる場合は積極的に使う
• ただし、条件分岐の練習として敢えて愚直に書くのも良い
```

## 5.3 数学の公式を使ってみよう

### 最大公約数（GCD）の理解と実装

数学の知識は競技プログラミングで非常に重要だ。特に最大公約数は頻出なので、しっかりマスターしよう。

```
【図5-9：ユークリッドの互除法の視覚的理解】

例：gcd(48, 18)を求める

Step 1: 48 ÷ 18 = 2 余り 12
┌─────────┬─────────┬─────────┐
│    18   │   18    │   12    │  48を18で割った余り
└─────────┴─────────┴─────────┘

Step 2: 18 ÷ 12 = 1 余り 6  
┌─────────┬─────────┐
│   12    │    6    │  18を12で割った余り
└─────────┴─────────┘

Step 3: 12 ÷ 6 = 2 余り 0
┌─────────┬─────────┐
│    6    │    6    │  12を6で割った余り
└─────────┴─────────┘

余りが0になったので、gcd(48, 18) = 6

💡 アルゴリズムの原理：
gcd(a, b) = gcd(b, a % b)
この性質を余りが0になるまで繰り返す
```

```
【図5-10：GCDの実装と応用】

基本実装：
┌─────────────────────────────────────────────┐
│ def gcd(a, b):                                │
│     while b:                                  │
│         a, b = b, a % b                       │
│     return a                                  │
│                                             │
│ # 使用例                                     │
│ print(gcd(48, 18))  # 6                      │
│ print(gcd(17, 13))  # 1（互いに素）           │
└─────────────────────────────────────────────┘

Python標準ライブラリの利用：
┌─────────────────────────────────────────────┐
│ import math                                   │
│ print(math.gcd(48, 18))  # 6                 │
│                                             │
│ # 複数の数のGCD                              │
│ from functools import reduce                  │
│ numbers = [48, 18, 24]                       │
│ result = reduce(math.gcd, numbers)            │
│ print(result)  # 6                           │
└─────────────────────────────────────────────┘

LCM（最小公倍数）の計算：
┌─────────────────────────────────────────────┐
│ def lcm(a, b):                                │
│     return (a * b) // gcd(a, b)               │
│                                             │
│ # 公式：lcm(a, b) × gcd(a, b) = a × b        │
│ print(lcm(48, 18))  # 144                    │
└─────────────────────────────────────────────┘

実際の問題での活用例：
┌─────────────────────────────────────────────┐
│ # 「分数 a/b を約分せよ」                    │
│ a, b = map(int, input().split())              │
│ g = math.gcd(a, b)                           │
│ print(a // g, b // g)                        │
│                                             │
│ # 「2つの周期がa, bの現象が同時に起こるのは？」│
│ a, b = map(int, input().split())              │
│ print(lcm(a, b))                             │
└─────────────────────────────────────────────┘
```

### 素数判定と素数の性質

```
【図5-11：効率的な素数判定】

素朴な素数判定：
┌─────────────────────────────────────────────┐
│ def is_prime_simple(n):                       │
│     if n < 2:                                 │
│         return False                          │
│     for i in range(2, n):                     │
│         if n % i == 0:                        │
│             return False                      │
│     return True                               │
│                                             │
│ # 問題：nが大きいと非常に遅い（O(n)）          │
└─────────────────────────────────────────────┘

改良版（√nまでチェック）：
┌─────────────────────────────────────────────┐
│ import math                                   │
│                                             │
│ def is_prime(n):                              │
│     if n < 2:                                 │
│         return False                          │
│     if n == 2:                                │
│         return True                           │
│     if n % 2 == 0:                            │
│         return False                          │
│                                             │
│     for i in range(3, int(math.sqrt(n)) + 1, 2):│
│         if n % i == 0:                        │
│             return False                      │
│     return True                               │
│                                             │
│ # 計算量：O(√n) - 大幅な高速化                │
└─────────────────────────────────────────────┘

素数の性質を活用した問題例：
┌─────────────────────────────────────────────┐
│ # 「N以下の素数の個数を求める」               │
│ n = int(input())                              │
│ count = 0                                     │
│ for i in range(2, n + 1):                     │
│     if is_prime(i):                           │
│         count += 1                            │
│ print(count)                                  │
│                                             │
│ # 「Nを2つの素数の和で表せるか？」            │
│ n = int(input())                              │
│ for i in range(2, n // 2 + 1):                │
│     if is_prime(i) and is_prime(n - i):       │
│         print(f"{n} = {i} + {n - i}")         │
│         break                                 │
│ else:                                         │
│     print("表せません")                       │
└─────────────────────────────────────────────┘
```

### 数学的な性質の活用

![図5-3：数学的性質の活用]({{ site.baseurl }}/images/figure5-3-mathematical-properties-utilization.svg)

競技プログラミングでは、数学的な性質を理解し活用することで、計算量を劇的に削減できる。

```
【図5-12：競技プログラミングでよく使う数学的性質】

奇数・偶数の性質：
┌─────────────────────────────────────────────┐
│ # 偶数 + 偶数 = 偶数                         │
│ # 奇数 + 奇数 = 偶数                         │
│ # 偶数 + 奇数 = 奇数                         │
│                                             │
│ # 活用例：「2つの数の和が偶数になるペア数」    │
│ numbers = list(map(int, input().split()))     │
│ even_count = sum(1 for x in numbers if x % 2 == 0)│
│ odd_count = len(numbers) - even_count         │
│ # 偶数同士 + 奇数同士のペア数                 │
│ pairs = even_count * (even_count - 1) // 2 + odd_count * (odd_count - 1) // 2│
│ print(pairs)                                  │
└─────────────────────────────────────────────┘

約数の性質：
┌─────────────────────────────────────────────┐
│ # N の約数は √N を境に対になって存在          │
│ def get_divisors(n):                          │
│     divisors = []                             │
│     for i in range(1, int(n**0.5) + 1):       │
│         if n % i == 0:                        │
│             divisors.append(i)                │
│             if i != n // i:  # 重複避け       │
│                 divisors.append(n // i)       │
│     return sorted(divisors)                   │
│                                             │
│ print(get_divisors(12))  # [1, 2, 3, 4, 6, 12]│
└─────────────────────────────────────────────┘

組み合わせの計算：
┌─────────────────────────────────────────────┐
│ # nCr = n! / (r! * (n-r)!)                   │
│ def combination(n, r):                        │
│     if r > n or r < 0:                        │
│         return 0                              │
│     if r == 0 or r == n:                      │
│         return 1                              │
│                                             │
│     # 効率的な計算（大きな階乗を避ける）       │
│     r = min(r, n - r)  # C(n,r) = C(n,n-r)    │
│     result = 1                                │
│     for i in range(r):                        │
│         result = result * (n - i) // (i + 1)  │
│     return result                             │
│                                             │
│ print(combination(5, 2))  # 10               │
└─────────────────────────────────────────────┘
```

## 5.4 文字列を操作してみよう

### 文字列操作の実践パターン

文字列処理は競技プログラミングで頻出の分野だ。様々なパターンをマスターしよう。

```
【図5-13：競技プログラミングでよく使う文字列操作】

パターン1：文字の出現回数カウント
┌─────────────────────────────────────────────┐
│ # 方法1: 辞書を手動で作成                    │
│ s = input()  # "programming"                 │
│ char_count = {}                               │
│ for char in s:                                │
│     if char in char_count:                    │
│         char_count[char] += 1                 │
│     else:                                     │
│         char_count[char] = 1                  │
│ print(char_count)                             │
│                                             │
│ # 方法2: get()メソッドを使用（推奨）          │
│ char_count = {}                               │
│ for char in s:                                │
│     char_count[char] = char_count.get(char, 0) + 1│
│                                             │
│ # 方法3: Counterを使用（最も簡潔）            │
│ from collections import Counter               │
│ char_count = Counter(s)                       │
│ print(char_count)                             │
│ # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})│
└─────────────────────────────────────────────┘

パターン2：文字列の検索・置換
┌─────────────────────────────────────────────┐
│ s = "Hello World Hello"                       │
│                                             │
│ # 部分文字列の検索                           │
│ print("Hello" in s)        # True            │
│ print(s.find("World"))     # 6（位置）        │
│ print(s.count("Hello"))    # 2（出現回数）     │
│                                             │
│ # 文字列の置換                               │
│ s2 = s.replace("Hello", "Hi")                 │
│ print(s2)  # "Hi World Hi"                   │
│                                             │
│ # 先頭・末尾の削除                           │
│ s3 = "  programming  "                       │
│ print(s3.strip())          # "programming"   │
│ print(s3.lstrip())         # "programming  " │
│ print(s3.rstrip())         # "  programming" │
└─────────────────────────────────────────────┘

パターン3：文字列の分割・結合
┌─────────────────────────────────────────────┐
│ # 分割                                       │
│ sentence = "apple,banana,cherry"              │
│ fruits = sentence.split(",")                  │
│ print(fruits)  # ['apple', 'banana', 'cherry']│
│                                             │
│ # 結合                                       │
│ words = ["Hello", "World", "Python"]          │
│ result = " ".join(words)                      │
│ print(result)  # "Hello World Python"        │
│                                             │
│ # より複雑な分割                             │
│ text = "a1b2c3d4"                            │
│ import re                                     │
│ parts = re.split(r'\d', text)  # 数字で分割   │
│ print(parts)  # ['a', 'b', 'c', 'd', '']     │
└─────────────────────────────────────────────┘
```

### 回文（Palindrome）判定

```
【図5-14：回文判定の様々な実装】

基本的な回文判定：
┌─────────────────────────────────────────────┐
│ def is_palindrome_basic(s):                   │
│     return s == s[::-1]                       │
│                                             │
│ # テスト                                     │
│ print(is_palindrome_basic("racecar"))  # True│
│ print(is_palindrome_basic("hello"))    # False│
└─────────────────────────────────────────────┘

大文字小文字を無視する回文判定：
┌─────────────────────────────────────────────┐
│ def is_palindrome_ignore_case(s):             │
│     s = s.lower()                             │
│     return s == s[::-1]                       │
│                                             │
│ print(is_palindrome_ignore_case("Racecar"))  # True│
│ print(is_palindrome_ignore_case("RaceCar"))  # True│
└─────────────────────────────────────────────┘

空白・記号を無視する回文判定：
┌─────────────────────────────────────────────┐
│ def is_palindrome_advanced(s):                │
│     # アルファベットのみを抽出               │
│     clean = ''.join(c.lower() for c in s if c.isalpha())│
│     return clean == clean[::-1]               │
│                                             │
│ print(is_palindrome_advanced("A man, a plan, a canal: Panama"))│
│ # True（amanaplanacanalpanama）              │
└─────────────────────────────────────────────┘

効率的な回文判定（大きな文字列用）：
┌─────────────────────────────────────────────┐
│ def is_palindrome_efficient(s):               │
│     left, right = 0, len(s) - 1               │
│     while left < right:                       │
│         if s[left] != s[right]:               │
│             return False                      │
│         left += 1                             │
│         right -= 1                            │
│     return True                               │
│                                             │
│ # メモリ使用量が少なく、途中で判定終了可能    │
└─────────────────────────────────────────────┘
```

### 文字列の辞書順ソート

```
【図5-15：文字列のソートと順序】

基本的な文字列ソート：
┌─────────────────────────────────────────────┐
│ words = ["banana", "apple", "cherry", "date"] │
│ words.sort()                                  │
│ print(words)  # ['apple', 'banana', 'cherry', 'date']│
│                                             │
│ # 文字列の長さでソート                       │
│ words.sort(key=len)                           │
│ print(words)  # ['date', 'apple', 'banana', 'cherry']│
│                                             │
│ # 複合条件でソート（長さ→辞書順）             │
│ words.sort(key=lambda x: (len(x), x))         │
│ print(words)  # ['date', 'apple', 'banana', 'cherry']│
└─────────────────────────────────────────────┘

文字列の大小比較の理解：
┌─────────────────────────────────────────────┐
│ # 辞書順の比較                               │
│ print("apple" < "banana")     # True         │
│ print("Apple" < "apple")      # True（大文字が先）│
│ print("a" < "aa")            # True          │
│                                             │
│ # 数値文字列の比較（注意が必要）              │
│ print("10" < "2")            # True（文字列として）│
│ print("10" < "02")           # False         │
│                                             │
│ # 数値として比較したい場合                   │
│ numbers = ["10", "2", "1", "20"]              │
│ numbers.sort(key=int)                         │
│ print(numbers)  # ['1', '2', '10', '20']     │
└─────────────────────────────────────────────┘
```

## 5.5 ソート（並び替え）を活用しよう

### Pythonでのソート完全活用

ソートは非常に強力な道具だ。単なる並び替えだけでなく、様々な問題解決に活用できる。

![図5-16：Pythonでのソート完全ガイド]({{ site.baseurl }}/assets/diagrams/chapter5/figure5-16-python-sort-complete-guide.svg)

### ソートを活用した問題解決パターン

```
【図5-17：ソートによる問題解決の典型例】

パターン1: 中央値の求取
┌─────────────────────────────────────────────┐
│ def find_median(numbers):                     │
│     sorted_nums = sorted(numbers)             │
│     n = len(sorted_nums)                      │
│     if n % 2 == 1:                            │
│         return sorted_nums[n // 2]            │
│     else:                                     │
│         mid1 = sorted_nums[n // 2 - 1]        │
│         mid2 = sorted_nums[n // 2]            │
│         return (mid1 + mid2) / 2              │
│                                             │
│ print(find_median([3, 1, 4, 1, 5]))  # 3     │
│ print(find_median([3, 1, 4, 1]))     # 2.5   │
└─────────────────────────────────────────────┘

パターン2: 最小差分ペアの発見
┌─────────────────────────────────────────────┐
│ def min_difference_pair(numbers):             │
│     numbers.sort()                            │
│     min_diff = float('inf')                   │
│     best_pair = None                          │
│                                             │
│     for i in range(len(numbers) - 1):         │
│         diff = numbers[i + 1] - numbers[i]    │
│         if diff < min_diff:                   │
│             min_diff = diff                   │
│             best_pair = (numbers[i], numbers[i + 1])│
│                                             │
│     return best_pair, min_diff                │
│                                             │
│ nums = [4, 2, 1, 3]                          │
│ pair, diff = min_difference_pair(nums)        │
│ print(f"最小差分ペア: {pair}, 差分: {diff}")   │
│ # 最小差分ペア: (1, 2), 差分: 1               │
└─────────────────────────────────────────────┘

パターン3: 重複の除去（順序保持）
┌─────────────────────────────────────────────┐
│ def remove_duplicates_sorted(numbers):        │
│     numbers.sort()                            │
│     if not numbers:                           │
│         return []                             │
│                                             │
│     result = [numbers[0]]                     │
│     for i in range(1, len(numbers)):          │
│         if numbers[i] != numbers[i - 1]:      │
│             result.append(numbers[i])         │
│     return result                             │
│                                             │
│ nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]           │
│ unique = remove_duplicates_sorted(nums)       │
│ print(unique)  # [1, 2, 3, 4, 5, 6, 9]       │
│                                             │
│ # Pythonらしい書き方                         │
│ unique = sorted(set(nums))                    │
│ print(unique)  # [1, 2, 3, 4, 5, 6, 9]       │
└─────────────────────────────────────────────┘
```

## 5.6 貪欲法（グリーディ）で最適解を見つけよう

### 貪欲法の基本的な考え方

貪欲法は「その時々で最も良い選択をしていけば、全体として最適解が得られる」という考え方のアルゴリズムだ。

![図5-4：貪欲法アルゴリズム]({{ site.baseurl }}/images/figure5-4-greedy-algorithm-patterns.svg)

```
【図5-19：コイン問題の実装】

実装：
┌─────────────────────────────────────────────┐
│ def min_coins(target):                        │
│     coins = [500, 100, 50, 10, 1]             │
│     count = 0                                 │
│     result = []                               │
│                                             │
│     for coin in coins:                        │
│         if target >= coin:                    │
│             num_coins = target // coin        │
│             count += num_coins                │
│             target %= coin                    │
│             result.append((coin, num_coins))  │
│                                             │
│     return count, result                      │
│                                             │
│ # 使用例                                     │
│ target = 890                                  │
│ total_coins, detail = min_coins(target)       │
│ print(f"必要なコイン数: {total_coins}")        │
│ for coin, num in detail:                      │
│     print(f"{coin}円硬貨: {num}枚")           │
│                                             │
│ # 出力:                                      │
│ # 必要なコイン数: 9                          │
│ # 500円硬貨: 1枚                            │
│ # 100円硬貨: 3枚                            │
│ # 50円硬貨: 1枚                             │
│ # 10円硬貨: 4枚                             │
└─────────────────────────────────────────────┘
```

### 区間スケジューリング問題

貪欲法の応用として、区間スケジューリング問題も重要だ：

```
【図5-20：区間スケジューリング問題】

問題：「複数の会議があり、重複しないよう最大数の会議に参加したい」

会議データ例：
┌─────────────────────────────────────────────┐
│ 会議A: 9:00-10:30                           │
│ 会議B: 10:00-11:30                          │
│ 会議C: 11:00-12:00                          │
│ 会議D: 11:30-12:30                          │
│ 会議E: 12:00-13:00                          │
└─────────────────────────────────────────────┘

貪欲戦略：「終了時刻が早い会議から選ぶ」
┌─────────────────────────────────────────────┐
│ 1. 終了時刻順にソート                        │
│ 2. 最初の会議を選択                         │
│ 3. 前の会議と重複しない次の会議を選択         │
│ 4. 3を繰り返す                              │
└─────────────────────────────────────────────┘

実装：
┌─────────────────────────────────────────────┐
│ def max_meetings(meetings):                   │
│     # (開始時刻, 終了時刻, 名前) のタプルのリスト│
│     meetings.sort(key=lambda x: x[1])  # 終了時刻でソート│
│                                             │
│     selected = []                             │
│     last_end_time = 0                         │
│                                             │
│     for start, end, name in meetings:         │
│         if start >= last_end_time:            │
│             selected.append((start, end, name))│
│             last_end_time = end               │
│                                             │
│     return selected                           │
│                                             │
│ # 使用例                                     │
│ meetings = [                                  │
│     (9.0, 10.5, "会議A"),                     │
│     (10.0, 11.5, "会議B"),                    │
│     (11.0, 12.0, "会議C"),                    │
│     (11.5, 12.5, "会議D"),                    │
│     (12.0, 13.0, "会議E")                     │
│ ]                                            │
│                                             │
│ result = max_meetings(meetings)               │
│ print("選択された会議:")                      │
│ for start, end, name in result:               │
│     print(f"{name}: {start}-{end}")           │
│                                             │
│ # 出力: 会議A, 会議C, 会議E が選択される       │
└─────────────────────────────────────────────┘
```

### 貪欲法の注意点

```
【図5-21：貪欲法が失敗する例】

❌ 貪欲法が最適解を保証しない例：

コイン問題（特殊なコインシステム）：
┌─────────────────────────────────────────────┐
│ 利用可能コイン：[1, 3, 4] 円                  │
│ 目標：6円を作る                              │
│                                             │
│ 貪欲法の結果：                               │
│ 4円×1 + 1円×2 = 3枚                        │
│                                             │
│ 最適解：                                     │
│ 3円×2 = 2枚                                │
│                                             │
│ → 貪欲法では最適解が得られない！              │
└─────────────────────────────────────────────┘

ナップサック問題（重みと価値がある場合）：
┌─────────────────────────────────────────────┐
│ 容量10のナップサックに以下の品物を入れる：     │
│ 品物A: 重み6, 価値30                        │
│ 品物B: 重み3, 価値14                        │
│ 品物C: 重み4, 価値16                        │
│ 品物D: 重み2, 価値9                         │
│                                             │
│ 貪欲法（価値/重み比で選択）：                 │
│ A(5.0) > C(4.0) > D(4.5) > B(4.67)         │
│ → A を選択（重み6, 価値30）                  │
│ → 残り容量4でCまたはBを選択                  │
│                                             │
│ 最適解：                                     │
│ B + C + D を選択（重み9, 価値39）            │
│ → 貪欲法の結果（価値34）より良い              │
└─────────────────────────────────────────────┘

💡 貪欲法を使う際の判断基準：
✅ 使って良い場合：
• 局所的最適解が全体最適解につながることが証明できる
• 問題の性質上、後の選択が前の選択に影響しない
• コイン問題（日本の硬貨システム）、区間スケジューリングなど

❌ 注意が必要な場合：
• ナップサック問題（動的プログラミングが必要）
• 最短経路問題（一部を除く）
• 複雑な最適化問題
```

## まとめ：アルゴリズムの道具箱を手に入れた！

この章では、競技プログラミングで最も頻繁に使用される6つの基本アルゴリズムを学んだ。

```
【図5-22：この章で身につけたアルゴリズム道具箱】

🔧 習得したアルゴリズム
┌─────────────────────────────────────────────┐
│ ✅ 全探索: 確実だが時間のかかる万能手法        │
│ ✅ 条件分岐: 複雑な場合分けの整理術           │
│ ✅ 数学活用: GCD、素数判定、組み合わせ計算     │
│ ✅ 文字列処理: 検索、置換、パターンマッチング  │
│ ✅ ソート: 並び替えによる問題の簡単化         │
│ ✅ 貪欲法: 局所最適による全体最適化           │
└─────────────────────────────────────────────┘

🎯 使い分けの指針
┌─────────────────────────────────────────────┐
│ • 計算量が許す範囲なら全探索が最も確実        │
│ • 数学的性質がある場合は公式・定理を活用      │
│ • データに順序がある場合はソートを検討        │
│ • 局所最適＝全体最適が保証される場合は貪欲法  │
└─────────────────────────────────────────────┘

🚀 次のステップ
┌─────────────────────────────────────────────┐
│ 第6章: データ構造を理解して活用しよう          │
│ • より効率的なデータ管理手法の習得           │
│ • リスト、辞書、集合の応用技法              │
│ • アルゴリズムとデータ構造の組み合わせ        │
└─────────────────────────────────────────────┘
```

この章で学んだアルゴリズムは、競技プログラミングにおける「基本的な道具」だ。大工さんが金槌だけで家を建てられないように、プログラマーも複数の道具を組み合わせて問題を解決する。

重要なのは、「どの道具をいつ使うか」を判断する力だ。問題を見た時に：

1. **まず全探索で解けないか？** → 計算量を見積もる
2. **数学的な性質はないか？** → 公式や定理で簡単になる
3. **ソートしたら簡単になるか？** → 順序関係が重要な問題
4. **貪欲に選択して大丈夫か？** → 局所最適＝全体最適の保証

この判断力は、実際に多くの問題を解くことで身についてくる。次の章では、これらのアルゴリズムをより効率的に実行するための「データ構造」について学ぼう。適切なデータ構造を選ぶことで、同じアルゴリズムでも劇的に高速化できるんだ！
