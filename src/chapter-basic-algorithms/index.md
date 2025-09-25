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

【図5-4：数値の各桁分解プロセス】

<figure class="pseudocode">
  <figcaption>各桁の和を求める（手続きの流れ）</figcaption>
  <pre><code class="language-text">例：数値 1234 の各桁の和を求める

Step 1: temp = 1234, digit_sum = 0
  temp % 10 = 4（最下位桁） → digit_sum = 4 → temp = 123

Step 2: temp = 123, digit_sum = 4
  temp % 10 = 3 → digit_sum = 7 → temp = 12

Step 3: temp = 12, digit_sum = 7
  temp % 10 = 2 → digit_sum = 9 → temp = 1

Step 4: temp = 1, digit_sum = 9
  temp % 10 = 1 → digit_sum = 10 → temp = 0

Step 5: temp = 0 → ループ終了
結果: digit_sum = 10</code></pre>
  <figcaption>💡 重要な演算子</figcaption>
  <pre><code class="language-text">• % (mod): 余りを求める → 最下位桁の取得
• // (整数除算): 小数切り捨ての除算 → 最下位桁の除去</code></pre>
</figure>

### より複雑な全探索の例

<figure>
  <img src="{{ '/assets/diagrams/generated/ch5-bruteforce.svg' | relative_url }}" alt="図5-x：全探索の基本フロー">
  <figcaption>図5-x：全探索の基本フロー</figcaption>
</figure>

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

## 5.2 条件分岐で場合分けしよう

### 複雑な条件分岐の整理法

競技プログラミングでは、複数の条件が組み合わさった複雑な場合分けが必要になることがある。整理して考える方法を学ぼう。

【図5-6：条件分岐の段階的構築】

問題例：「点数に応じて成績を判定」  
90点以上：A, 80点以上：B, 70点以上：C, 60点以上：D, 未満：F

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

{% capture anti_patterns %}
誤りがちな書き方と修正の着眼点  
• 「上限条件の二重指定」… elif では前件が偽なため、`< 90` などの上限は不要  
• 「境界のズレ」… `>=` と `>` を混在させると境界60/70/80/90で誤判定  
• 「順序の逆転」… 大きい方から条件を書く（90→80→70→60）と簡潔で安全
{% endcapture %}
{% include panel.html type="warn" title="⚠️ アンチパターンと直し方" content=anti_patterns %}

### 複雑な論理演算の活用

【図5-7：論理演算子の効果的な使用】

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

【図5-8：条件分岐の表による整理】

{% capture pat_list %}
可能なパターン（6通り）  
• a ≥ b ≥ c → a b c  
• a ≥ c ≥ b → a c b  
• b ≥ a ≥ c → b a c  
• b ≥ c ≥ a → b c a  
• c ≥ a ≥ b → c a b  
• c ≥ b ≥ a → c b a
{% endcapture %}
{% include panel.html type="info" title="大小関係の6パターン" content=pat_list %}

<figure class="pseudocode">
  <figcaption>実装方法1: 全パターンを条件分岐</figcaption>
  <pre><code class="language-python">a, b, c = map(int, input().split())
if a &gt;= b &gt;= c:
    print(a, b, c)
elif a &gt;= c &gt;= b:
    print(a, c, b)
elif b &gt;= a &gt;= c:
    print(b, a, c)
elif b &gt;= c &gt;= a:
    print(b, c, a)
elif c &gt;= a &gt;= b:
    print(c, a, b)
else:  # c &gt;= b &gt;= a
    print(c, b, a)</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>実装方法2: ソートを活用（推奨）</figcaption>
  <pre><code class="language-python">a, b, c = map(int, input().split())
numbers = [a, b, c]
numbers.sort(reverse=True)  # 降順
print(*numbers)</code></pre>
</figure>

{% capture learn_pts %}
• 複雑な条件分岐は、より簡潔な手段がないか検討  
• ソート等の既存機能を積極活用  
• 練習として愚直な分岐を書くのも有用
{% endcapture %}
{% include panel.html type="steps" title="💡 学習ポイント" content=learn_pts %}

## 5.3 数学の公式を使ってみよう

### 最大公約数（GCD）の理解と実装

数学の知識は競技プログラミングで非常に重要だ。特に最大公約数は頻出なので、しっかりマスターしよう。

【図5-9：ユークリッドの互除法の理解】

<figure class="pseudocode">
  <figcaption>反復版（ユークリッドの互除法）</figcaption>
  <pre><code class="language-python">def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6</code></pre>
</figure>

{% capture gcd_principle %}
💡 原理  
gcd(a, b) = gcd(b, a % b)（b=0で停止）
{% endcapture %}
{% include panel.html type="info" title="アルゴリズムの原理" content=gcd_principle %}

【図5-10：GCDの実装と応用】

<figure class="pseudocode">
  <figcaption>基本実装（ユークリッドの互除法）</figcaption>
  <pre><code class="language-python">def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6
print(gcd(17, 13))  # 1（互いに素）</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>標準ライブラリの利用</figcaption>
  <pre><code class="language-python">import math
print(math.gcd(48, 18))  # 6

from functools import reduce
numbers = [48, 18, 24]
print(reduce(math.gcd, numbers))  # 6</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>LCM（最小公倍数）と活用例</figcaption>
  <pre><code class="language-python">def lcm(a, b):
    return (a * b) // gcd(a, b)  # lcm*gcd = a*b

print(lcm(48, 18))  # 144

# 分数 a/b の約分
a, b = map(int, input().split())
g = math.gcd(a, b)
print(a // g, b // g)

# 2つの周期が同時に起こる時刻
a, b = map(int, input().split())
print(lcm(a, b))</code></pre>
</figure>

### 素数判定と素数の性質

【図5-11：効率的な素数判定】

<figure class="pseudocode">
  <figcaption>素朴な素数判定（O(n)）</figcaption>
  <pre><code class="language-python">def is_prime_simple(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>改良版：√n までチェック（O(√n)）</figcaption>
  <pre><code class="language-python">import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>素数の性質の活用例</figcaption>
  <pre><code class="language-python"># N 以下の素数の個数
n = int(input())
count = 0
for i in range(2, n + 1):
    if is_prime(i):
        count += 1
print(count)

# N を2つの素数の和で表せるか
n = int(input())
for i in range(2, n // 2 + 1):
    if is_prime(i) and is_prime(n - i):
        print(f"{n} = {i} + {n - i}")
        break
else:
    print("表せません")</code></pre>
</figure>

### 数学的な性質の活用

![図5-3：数学的性質の活用]({{ site.baseurl }}/images/figure5-3-mathematical-properties-utilization.svg)

競技プログラミングでは、数学的な性質を理解し活用することで、計算量を劇的に削減できる。

【図5-12：競技プログラミングでよく使う数学的性質】

<figure class="pseudocode">
  <figcaption>奇数・偶数の性質と応用</figcaption>
  <pre><code class="language-python"># 偶数+偶数=偶数 / 奇数+奇数=偶数 / 偶数+奇数=奇数
numbers = list(map(int, input().split()))
even = sum(1 for x in numbers if x % 2 == 0)
odd = len(numbers) - even
# 偶数同士 + 奇数同士 のペア数
pairs = even * (even - 1) // 2 + odd * (odd - 1) // 2
print(pairs)</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>約数の性質（√N まで調べる）</figcaption>
  <pre><code class="language-python">def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # 重複回避
                divisors.append(n // i)
    return sorted(divisors)

print(get_divisors(12))  # [1, 2, 3, 4, 6, 12]</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>組み合わせ nCr の効率計算</figcaption>
  <pre><code class="language-python">def combination(n, r):
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)  # 対称性
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result

print(combination(5, 2))  # 10</code></pre>
</figure>

## 5.4 文字列を操作してみよう

### 文字列操作の実践パターン

文字列処理は競技プログラミングで頻出の分野だ。様々なパターンをマスターしよう。

【図5-13：競技プログラミングでよく使う文字列操作】

<figure class="pseudocode">
  <figcaption>パターン1：文字の出現回数カウント</figcaption>
  <pre><code class="language-python"># 方法1: 手動カウント
s = input()
char_count = {}
for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1
print(char_count)

# 方法2: Counter
from collections import Counter
print(Counter(s))</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン2：検索・置換・トリム</figcaption>
  <pre><code class="language-python">s = "Hello World Hello"
# 検索
print("Hello" in s)
print(s.find("World"))
print(s.count("Hello"))
# 置換
s2 = s.replace("Hello", "Hi")
print(s2)  # Hi World Hi
# トリム
s3 = "  programming  "
print(s3.strip()); print(s3.lstrip()); print(s3.rstrip())</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン3：分割・結合・正規表現</figcaption>
  <pre><code class="language-python">sentence = "apple,banana,cherry"
fruits = sentence.split(',')
print(fruits)

words = ["Hello", "World", "Python"]
print(' '.join(words))

import re
text = "a1b2c3d4"
parts = re.split(r'\\d', text)
print(parts)</code></pre>
</figure>

### 回文（Palindrome）判定

【図5-14：回文判定の様々な実装】

<figure class="pseudocode">
  <figcaption>基本：スライスで反転比較</figcaption>
  <pre><code class="language-python">def is_palindrome_basic(s):
    return s == s[::-1]

print(is_palindrome_basic("racecar"))  # True
print(is_palindrome_basic("hello"))    # False</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>大小無視・記号無視</figcaption>
  <pre><code class="language-python">def is_palindrome_ignore_case(s):
    s = s.lower()
    return s == s[::-1]

def is_palindrome_advanced(s):
    clean = ''.join(c.lower() for c in s if c.isalpha())
    return clean == clean[::-1]

print(is_palindrome_ignore_case("Racecar"))  # True
print(is_palindrome_advanced("A man, a plan, a canal: Panama"))  # True</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>効率的：両端からの比較</figcaption>
  <pre><code class="language-python">def is_palindrome_efficient(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1; right -= 1
    return True  # 途中終了可能で効率的</code></pre>
</figure>

### 文字列の辞書順ソート

【図5-15：文字列のソートと順序】

<figure class="pseudocode">
  <figcaption>基本の文字列ソート</figcaption>
  <pre><code class="language-python">words = ["banana", "apple", "cherry", "date"]
words.sort()
print(words)  # ['apple', 'banana', 'cherry', 'date']

# 長さでソート
words.sort(key=len)
print(words)

# 複合条件（長さ→辞書順）
words.sort(key=lambda x: (len(x), x))
print(words)</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>大小比較の基礎と注意</figcaption>
  <pre><code class="language-python"># 辞書順の比較
print("apple" < "banana")
print("Apple" < "apple")  # 大文字が先
print("a" < "aa")

# 数値文字列の比較（注意）
print("10" < "2")   # True（文字列の比較）
print("10" < "02")  # False

# 数値として比較
numbers = ["10", "2", "1", "20"]
numbers.sort(key=int)
print(numbers)</code></pre>
</figure>

## 5.5 ソート（並び替え）を活用しよう

### Pythonでのソート完全活用

ソートは非常に強力な道具だ。単なる並び替えだけでなく、様々な問題解決に活用できる。

![図5-16：Pythonでのソート完全ガイド]({{ site.baseurl }}/assets/diagrams/chapter5/figure5-16-python-sort-complete-guide.svg)

### ソートを活用した問題解決パターン

【図5-17：ソートによる問題解決の典型例】

<figure class="pseudocode">
  <figcaption>パターン1: 中央値</figcaption>
  <pre><code class="language-python">def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        return (mid1 + mid2) / 2

print(find_median([3, 1, 4, 1, 5]))  # 3
print(find_median([3, 1, 4, 1]))     # 2.5</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン2: 最小差分ペア</figcaption>
  <pre><code class="language-python">def min_difference_pair(numbers):
    numbers.sort()
    min_diff = float('inf')
    best_pair = None
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            best_pair = (numbers[i], numbers[i + 1])
    return best_pair, min_diff

nums = [4, 2, 1, 3]
pair, diff = min_difference_pair(nums)
print(f"最小差分ペア: {pair}, 差分: {diff}")</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>パターン3: 重複除去（順序保持）</figcaption>
  <pre><code class="language-python">def remove_duplicates_sorted(numbers):
    numbers.sort()
    if not numbers:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            result.append(numbers[i])
    return result

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique = remove_duplicates_sorted(nums)
print(unique)

# Pythonらしい書き方
print(sorted(set(nums)))</code></pre>
</figure>

## 5.6 貪欲法（グリーディ）で最適解を見つけよう

### 貪欲法の基本的な考え方

貪欲法は「その時々で最も良い選択をしていけば、全体として最適解が得られる」という考え方のアルゴリズムだ。

![図5-4：貪欲法アルゴリズム]({{ site.baseurl }}/images/figure5-4-greedy-algorithm-patterns.svg)

【図5-19：コイン問題の実装】

<figure class="pseudocode">
  <figcaption>貪欲によるコイン最少枚数</figcaption>
  <pre><code class="language-python">def min_coins(target):
    coins = [500, 100, 50, 10, 1]
    count = 0
    result = []
    for coin in coins:
        if target >= coin:
            num = target // coin
            count += num
            target %= coin
            result.append((coin, num))
    return count, result

target = 890
total, detail = min_coins(target)
print(total)
for coin, num in detail:
    print(coin, num)</code></pre>
</figure>

### 区間スケジューリング問題

貪欲法の応用として、区間スケジューリング問題も重要だ：

【図5-20：区間スケジューリング問題】

{% capture interval_strategy %}
貪欲戦略：「終了時刻が早い会議から選ぶ」  
1) 終了時刻順にソート → 2) 最初を選択 → 3) 前と重ならない次を選択（繰り返し）
{% endcapture %}
{% include panel.html type="steps" title="戦略" content=interval_strategy %}

<figure class="pseudocode">
  <figcaption>実装</figcaption>
  <pre><code class="language-python">def max_meetings(meetings):
    # meetings: (start, end, name)
    meetings.sort(key=lambda x: x[1])
    selected = []
    last_end = 0
    for start, end, name in meetings:
        if start >= last_end:
            selected.append((start, end, name))
            last_end = end
    return selected

meetings = [
    (9.0, 10.5, "会議A"),
    (10.0, 11.5, "会議B"),
    (11.0, 12.0, "会議C"),
    (11.5, 12.5, "会議D"),
    (12.0, 13.0, "会議E"),
]
print(max_meetings(meetings))</code></pre>
</figure>

### 貪欲法の注意点

【図5-21：貪欲法が失敗する例】

{% capture bad_coin %}
コイン系の反例（[1,3,4] で 6 を作る）  
• 貪欲: 4+1+1 = 3枚（最適ではない）  
• 最適: 3+3 = 2枚  
→ 貪欲は常に最適を保証しない
{% endcapture %}
{% include panel.html type="warn" title="❌ 反例：特殊なコイン系" content=bad_coin %}

{% capture bad_knapsack %}
ナップサックの反例（価値/重み比の貪欲）  
• 局所最適選択が全体最適に繋がらない例がある  
• DP等の最適解手法が必要
{% endcapture %}
{% include panel.html type="warn" title="❌ 反例：ナップサック" content=bad_knapsack %}

{% capture greedy_guides %}
✅ 使って良い場合  
• 局所最適＝全体最適が証明できる  
• 後の選択が前の選択に影響しない  
• 例：日本硬貨の両替、区間スケジューリング

⚠️ 注意が必要  
• ナップサック、（多くの）最短経路、複雑な最適化
{% endcapture %}
{% include panel.html type="info" title="💡 貪欲法を使う判断基準" content=greedy_guides %}

## 典型的な誤りと修正（アルゴリズム）

{% capture algo_wrong %}
ケース1: 二重ループで i<j の制約を忘れる  
→ 重複カウントや同一要素の組を数えてしまう。修正: `for i in range(n): for j in range(i+1, n): ...`

ケース2: 計算量の過小評価  
→ N=10^5 で O(N^2) を選ぶ。修正: 上限から計算量を見積もり、O(N log N) などへ設計変更

ケース3: 条件分岐の境界ズレ  
→ `>=`/`>` の混在で境界が誤判定。修正: 大きい方から順に if/elif を設計
{% endcapture %}
{% include panel.html type="warn" title="⚠️ よくある誤り" content=algo_wrong %}

## まとめ：アルゴリズムの道具箱を手に入れた！

この章では、競技プログラミングで最も頻繁に使用される6つの基本アルゴリズムを学んだ。

【図5-22：この章で身につけたアルゴリズム道具箱】

{% capture ch5_gained %}
✅ 全探索／条件分岐  
✅ 数学活用（GCD・素数・組み合わせ）  
✅ 文字列処理  
✅ ソート活用  
✅ 貪欲法
{% endcapture %}
{% include panel.html type="steps" title="🔧 習得したアルゴリズム" content=ch5_gained %}

{% capture ch5_guide %}
• 計算量が許せば全探索  
• 数学的性質があれば公式・定理  
• 順序が鍵ならソート  
• 局所最適＝全体最適が保証されるなら貪欲
{% endcapture %}
{% include panel.html type="info" title="🎯 使い分けの指針" content=ch5_guide %}

{% capture ch5_next %}
第6章: データ構造を理解して活用  
• 効率的なデータ管理  
• リスト/辞書/集合の応用  
• アルゴリズムとの組み合わせ
{% endcapture %}
{% include panel.html type="plan" title="🚀 次のステップ" content=ch5_next %}

この章で学んだアルゴリズムは、競技プログラミングにおける「基本的な道具」だ。大工さんが金槌だけで家を建てられないように、プログラマーも複数の道具を組み合わせて問題を解決する。

重要なのは、「どの道具をいつ使うか」を判断する力だ。問題を見た時に：

1. **まず全探索で解けないか？** → 計算量を見積もる
2. **数学的な性質はないか？** → 公式や定理で簡単になる
3. **ソートしたら簡単になるか？** → 順序関係が重要な問題
4. **貪欲に選択して大丈夫か？** → 局所最適＝全体最適の保証

この判断力は、実際に多くの問題を解くことで身についてくる。次の章では、これらのアルゴリズムをより効率的に実行するための「データ構造」について学ぼう。適切なデータ構造を選ぶことで、同じアルゴリズムでも劇的に高速化できるんだ！
