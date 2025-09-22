---
title: "第7章：ABC A・B問題を攻略しよう"
layout: book
order: 7
checklist:
  - A/Bの典型パターンを説明できる
  - 制約から解法を選べる
pitfalls:
  - 問題文の読み落とし
  - サンプル通過に合わせたハードコード
exercises:
  - { level: A, text: "条件分岐の基本", link: "https://atcoder.jp/contests/abc081/tasks/abc081_a" }
  - { level: B, text: "反復処理の基本", link: "https://atcoder.jp/contests/abc081/tasks/abc081_b" }
---

<!-- 
本章は「中学生向け競技プログラミング入門書」の一部であり、
CC BY-NC-SA 4.0ライセンスの下で提供されます。
商用利用は事前許諾が必要です。
詳細：../../LICENSE.md
-->

# 第7章：ABC A・B問題を攻略しよう

## 7.1 A問題の特徴と対策

いよいよ実際のAtCoder Beginner Contest（ABC）の問題に挑戦する時が来た！これまで学んだ技術を、本物の競技で活用しよう。まずはA問題から始めて、確実に得点できるようになることが大切だ。

【図7-1：ABC A問題の全体像と出題傾向】

{% capture a_overview %}
**配点**: 100–200点（全体の約15%）  
**制約**: 小規模（N ≤ 100 程度）  
**時間**: 5–10分目標  
**難易度**: 初心者向け
{% endcapture %}
{% include panel.html type="info" title="🎯 A問題の基本特徴" content=a_overview %}

{% capture a_skills %}
✅ 基本的な入出力処理  
✅ 四則演算と条件分岐  
✅ 簡単な文字列操作  
✅ 問題文の正確な理解
{% endcapture %}
{% include panel.html type="steps" title="🧰 求められるスキル" content=a_skills %}

### A問題の出題パターン分析

![ABC A問題の典型パターンと実装戦略を示す図表：四則演算、文字列操作、条件分岐、入出力処理の4つのパターンを頻度順で表示]({{ site.baseurl }}/assets/diagrams/chapter7/figure7-2-abc-a-problem-patterns.svg)

ABC A問題は、以下の4つの典型パターンに分類できる：

📊 パターン1：四則演算（約35%）
{% capture pat1 %}
**特徴**: 数値計算、単位変換、簡単な数式  
**例**: ABC001 A - 積雪深差（H2-H1を出力）  
**入出力**: 例 15 20 → 5  
**解法**:
```python
h1 = int(input())
h2 = int(input())
print(h2 - h1)
```

**ポイント**:  
• 問題文を式に翻訳する  
• 演算子の選択（+, -, *, //, %）  
• 入力形式の正確な理解
{% endcapture %}
{% include panel.html type="info" title="四則演算" content=pat1 %}

📊 パターン2：条件判定・場合分け（約30%）
{% capture pat2 %}
**特徴**: if文による条件分岐、Yes/No判定  
**例**: ABC086 A - Product（2つの整数A,Bの積が偶数か奇数か）  
**入出力**: 入力例 3 4 → 出力例 Even  
**解法**:
```python
a, b = map(int, input().split())
print("Even" if (a*b) % 2 == 0 else "Odd")
```

**ポイント**:  
• 偶奇性の理解（偶数×任意=偶数）  
• 条件分岐の正確な実装  
• 出力形式の厳密な遵守
{% endcapture %}
{% include panel.html type="info" title="条件判定・場合分け" content=pat2 %}

📊 パターン3：文字列操作（約20%）
{% capture pat3 %}
**特徴**: 文字列の長さ、分割、結合、置換など  
**例**: ABC081 A - Placing Marbles（文字列s中の'1'の個数）  
**入出力**: 入力例 101 → 出力例 2  
**解法**:
```python
s = input()
print(s.count('1'))
```

または:
```python
s = input()
count = 0
for ch in s:
    if ch == '1':
        count += 1
print(count)
```
{% endcapture %}
{% include panel.html type="info" title="文字列操作" content=pat3 %}
{% capture pat3_points %}
💡 ポイント  
• 基本的な文字列メソッドの活用（`count`, `replace`, `split` など）  
• 文字の個別処理（forで1文字ずつ確認）  
• 短く正確に書ける方法を優先（読みやすさも重視）
{% endcapture %}
{% include panel.html type="steps" title="文字列操作のポイント" content=pat3_points %}

📊 パターン4：配列・リストの基本操作（約15%）
{% capture pat4 %}
**特徴**: 最大値・最小値、合計、要素数など  
**例**: ABC071 A - Meal Delivery（x と a, b の距離を比較）  
**入出力**: 入力例 10 3 8 → 出力例 B  
**解法**:
```python
x, a, b = map(int, input().split())
print("A" if abs(x - a) < abs(x - b) else "B")
```

**ポイント**:  
• 距離の概念（絶対値）の理解  
• 複数値の比較  
• 数学関数（`abs`）の活用
{% endcapture %}
{% include panel.html type="info" title="配列・リストの基本操作" content=pat4 %}

### A問題攻略の標準プロセス

{% capture s1_read %}
✅ やること  
• 問題文を最低2回読む  
• 何を求められているかを明確化  
• 入力形式と出力形式を正確に把握  
• 制約条件（数値の範囲など）を確認

💡 チェックポイント  
• 計算式が必要か／条件分岐が必要か  
• 文字列処理か数値処理か  
• 出力は数値か文字列か  
• 特別な条件や例外はあるか

🚫 やらないこと  
• いきなりコードを書く  
• 複雑な解法を先に考える
{% endcapture %}
{% include panel.html type="steps" title="🔍 Step 1: 問題文の精読（2–3分）" content=s1_read %}

{% capture s2_sample %}
✅ サンプルの活用  
• 入力→出力の変換過程を手で追う  
• なぜその出力かを論理的に理解  
• サンプルで正しく動くか検証

例：積雪深差  
• 入力: 15, 20 → 思考: 20-15=5 → 出力: 5 ✅

💭 自問自答  
• 他のケースでも正しいか  
• 特殊ケース（負/0）は大丈夫か  
• 計算の順序は正しいか
{% endcapture %}
{% include panel.html type="info" title="💡 Step 2: サンプル分析（1–2分）" content=s2_sample %}

{% capture s3_order %}
✅ 効率的な実装順序  
1. 入力処理から書き始める  
2. メインロジック（計算・判定）を実装  
3. 出力処理を書く  
4. コメントやサンプルで動作確認
{% endcapture %}
{% include panel.html type="steps" title="⌨️ Step 3: 実装（3–5分）" content=s3_order %}

<figure class="pseudocode">
  <figcaption>実装例（積雪深差）</figcaption>
  <pre><code class="language-python"># 入力処理
h1 = int(input())
h2 = int(input())

# メインロジック
snow_depth = h2 - h1

# 出力処理
print(snow_depth)</code></pre>
</figure>

{% capture s3_anti %}
🚫 避けるべき実装  
• 一行にまとめすぎる複雑なコード  
• 意味の薄い変数名（`a1`, `x2` など）  
• デバッグ用 `print` の残存
{% endcapture %}
{% include panel.html type="warn" title="実装時のアンチパターン" content=s3_anti %}

{% capture s4_checks %}
✅ 必須チェック項目  
• サンプル入力での動作確認  
• 手動計算との結果照合  
• 出力形式の正確性（改行・スペース）  
• エッジケース（最小値・最大値）の想定
{% endcapture %}
{% include panel.html type="steps" title="🧪 Step 4: 検証（1–2分）" content=s4_checks %}

{% capture s4_how %}
💡 検証方法  
• 頭の中でサンプルをトレース  
• 紙に書いて計算過程を確認  
• 別の方法でも同じ答えになるかを確認
{% endcapture %}
{% include panel.html type="info" title="検証の進め方" content=s4_how %}

{% capture s5_submit %}
✅ 提出前の最終確認  
• 言語がPython 3か  
• コード全体を正しくコピー  
• 不要な print やコメントなし

🎯 提出のタイミング  
• サンプル通過を確認後すぐ提出  
• 悩みすぎて時間を浪費しない  
• A問題は完璧より提出を優先

⏱️ 時間管理  
• A問題は10分以内を目安  
• 15分超なら一旦飛ばす  
• B問題の時間を確保
{% endcapture %}
{% include panel.html type="steps" title="🚀 Step 5: 提出（30秒）" content=s5_submit %}


### 実際のA問題解法実演

【図7-4：ABC085 A問題完全解法プロセス】

{% capture already_problem %}
高橋君は年賀状に「2017年」と書いてしまった。これを「2018年」に修正して出力する。  
入力: 1行の文字列（例: 2017年）  
出力: 修正後の文字列（例: 2018年）
{% endcapture %}
{% include panel.html type="info" title="📋 問題文（ABC085 A - Already 2018）" content=already_problem %}

{% capture already_analysis %}
理解したこと  
• 文字列の一部を置換する問題  
• 「2017」を「2018」に置換すればよい

方針  
• `str.replace("2017", "2018")` を使う
{% endcapture %}
{% include panel.html type="steps" title="🔍 分析" content=already_analysis %}

<figure class="pseudocode">
  <figcaption>実装（置換の活用）</figcaption>
  <pre><code class="language-python">s = input()
print(s.replace('2017', '2018'))</code></pre>
  <figcaption>別解（分割・結合）</figcaption>
  <pre><code class="language-python">s = input()
parts = s.split('2017')
print('2018'.join(parts))</code></pre>
  <figcaption>検証（サンプル）</figcaption>
  <pre><code class="language-text">入力: 2017年 → 出力: 2018年</code></pre>
</figure>

{% capture already_submit %}
提出時の確認  
✅ 余計な空白/改行がない  
✅ 入力に「2017」が複数あっても置換できる
{% endcapture %}
{% include panel.html type="steps" title="🧪 検証/提出" content=already_submit %}

## 7.2 A問題を実際に解いてみよう

理論だけでなく、実際の問題をいくつか解いて、パターンを体感してみよう。様々なタイプの問題を通じて、A問題のコツを掴んでいこう。

### 四則演算タイプの実演

【図7-5：ABC150 A問題「500 Yen Coins」完全解法】

{% capture coins500_problem %}
500円玉を K 枚持っている。X 円の品物を買えるか判定せよ（Yes/No）。  
入力: K X（Kは500円玉の枚数, Xは値段）
{% endcapture %}
{% include panel.html type="info" title="📋 問題文（ABC150 A）" content=coins500_problem %}

{% capture coins500_analysis %}
判定条件  
• 所持金 = 500 × K  
• 所持金 ≥ X なら Yes
{% endcapture %}
{% include panel.html type="steps" title="🔍 分析" content=coins500_analysis %}

<figure class="pseudocode">
  <figcaption>実装（シンプルな比較）</figcaption>
  <pre><code class="language-python">k, x = map(int, input().split())
print('Yes' if 500 * k >= x else 'No')</code></pre>
  <figcaption>サンプル検証</figcaption>
  <pre><code class="language-text">入力: 2 900 → 500*2=1000 ≥ 900 → Yes</code></pre>
</figure>

### 条件分岐タイプの実演

【図7-6：ABC088 A問題「Infinite Coins」完全解法】

{% capture infinite_problem %}
N 円の支払いが可能か判定する。A は所持している 1円玉の枚数。500円玉は無限に使える。  
入力: N, A  
出力: 支払えるなら Yes、そうでなければ No
{% endcapture %}
{% include panel.html type="info" title="📋 問題文（ABC088 A - Infinite Coins）" content=infinite_problem %}

{% capture infinite_analysis %}
考え方  
• 500円玉をできるだけ使ったときの不足額は `N % 500`  
• この不足額を 1円玉 A 枚で埋められるか（`N % 500 <= A`）
{% endcapture %}
{% include panel.html type="steps" title="🔍 分析" content=infinite_analysis %}

<figure class="pseudocode">
  <figcaption>実装（剰余で判定）</figcaption>
  <pre><code class="language-python">n = int(input())
a = int(input())
print('Yes' if (n % 500) <= a else 'No')</code></pre>
  <figcaption>サンプル検証</figcaption>
  <pre><code class="language-text">入力: n=2018, a=218 → 2018%500=18 ≤ 218 → Yes</code></pre>
</figure>

### 文字列処理タイプの実演

```
【図7-7：ABC122 A問題「Double Helix」完全解法】

{% capture dna_problem %}
DNAは A, T, G, C の4つの塩基からなる。  
A と T、G と C はそれぞれ対応する。  
1文字の塩基 b が与えられるので、対応する塩基を出力せよ。  
対応関係: A↔T, G↔C  
入力例: A → 出力例: T
{% endcapture %}
{% include panel.html type="info" title="📋 問題文（ABC122 A）" content=dna_problem %}

{% capture dna_analysis %}
理解したこと  
• 4文字（A,T,G,C）の相互対応  
• 入力1文字に対し、対応する1文字を出力

解法の選択肢  
1) if-elif で場合分け  
2) 辞書で対応表を定義  
3) 文字列のインデックス対応
{% endcapture %}
{% include panel.html type="steps" title="🔍 問題分析" content=dna_analysis %}

<figure class="pseudocode">
  <figcaption>解法1: if-elif（分かりやすい）</figcaption>
  <pre><code class="language-python">b = input()
if b == 'A':
    print('T')
elif b == 'T':
    print('A')
elif b == 'G':
    print('C')
elif b == 'C':
    print('G')</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>解法2: 辞書を使用（スマート）</figcaption>
  <pre><code class="language-python">b = input()
pair = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
print(pair[b])</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>解法3: インデックス対応</figcaption>
  <pre><code class="language-python">b = input()
dna = "ATGC"
pairs = "TACG"
print(pairs[dna.index(b)])</code></pre>
</figure>

{% include panel.html type="info" title="💡 推奨" content="A問題では解法1が最も確実で推奨" %}

{% capture dna_tests %}
テストケース  
• A → T、T → A、G → C、C → G（全てOK）

各解法の確認  
• 解法1: 条件分岐が正しく動作  
• 解法2: 辞書のキー検索が正常  
• 解法3: インデックス検索が正常
{% endcapture %}
{% include panel.html type="steps" title="🧪 検証" content=dna_tests %}
```

## 7.3 B問題の特徴と対策

A問題に慣れてきたら、次はB問題に挑戦しよう。B問題はA問題より一段階レベルが上がり、より実践的なプログラミング技術が必要になる。

```
【図7-8：A問題からB問題への段階的ステップアップ】

📊 難易度・要求スキルの比較
|            | A問題         | B問題         |
|------------|---------------|---------------|
| 配点       | 100–200点     | 200–400点     |
| 解答時間   | 5–10分        | 10–20分       |
| データサイズ | 小（〜100）    | 中（〜1000）    |
| 必要スキル | 基本文法       | 基本アルゴリズム |
| 思考の深さ | 1–2段階       | 2–4段階        |
| 実装の複雑さ | 簡単          | やや複雑        |

🎯 B問題で新たに求められるスキル
{% capture bskills %}
✅ 繰り返し処理の応用／リスト・配列操作  
✅ 条件分岐の組み合わせ／文字列の高度な処理  
✅ 簡単なアルゴリズム（ソート・探索）  
✅ 数学的思考（GCD・素数など）／計算量の意識
{% endcapture %}
{% include panel.html type="steps" title="B問題に向けて身につけたいスキル" content=bskills %}
```

### B問題の典型パターン分析

```
【図7-9：ABC B問題の出題パターン（頻出順）】

🔄 パターン1：繰り返し処理・シミュレーション（約40%）
{% capture some_sums_desc %}
特徴：ルールに従って複数回の処理を実行  
例：ABC083 B - Some Sums  
問題：1以上N以下の整数のうち、各桁の和がA以上B以下であるものの総和
{% endcapture %}
{% include panel.html type="info" title="繰り返し×条件の応用" content=some_sums_desc %}

<figure class="pseudocode">
  <figcaption>実装（桁和でフィルタ）</figcaption>
  <pre><code class="language-python">n, a, b = map(int, input().split())
total = 0
for i in range(1, n + 1):
    s = sum(int(d) for d in str(i))
    if a <= s <= b:
        total += i
print(total)</code></pre>
</figure>

{% capture some_sums_points %}
• 全候補を調べる（全探索）  
• 条件判定を正確に  
• 桁和の実装を簡潔に
{% endcapture %}
{% include panel.html type="steps" title="💡 ポイント" content=some_sums_points %}

📊 パターン2：配列・リスト操作（約25%）
{% capture mochi_desc %}
特徴：データの整理・ソート・集計  
例：ABC085 B - Kagami Mochi  
問題：N個の直径から重ねられる段数（ユニーク直径数）を求める
{% endcapture %}
{% include panel.html type="info" title="ソート/重複除去の応用" content=mochi_desc %}

<figure class="pseudocode">
  <figcaption>実装（ユニーク直径の個数）</figcaption>
  <pre><code class="language-python">n = int(input())
diams = [int(input()) for _ in range(n)]
print(len(set(diams)))</code></pre>
</figure>

{% capture mochi_points %}
• 重複除去に set を活用  
• リスト内包表記で簡潔に  
• 問題の本質＝ユニーク要素数
{% endcapture %}
{% include panel.html type="steps" title="💡 ポイント" content=mochi_points %}

🔤 パターン3：文字列の高度な処理（約20%）
{% capture notfound_desc %}
特徴：文字列の変換・パターンマッチング  
例：ABC071 B - Not Found  
問題：文字列Sに含まれない英小文字のうち、アルファベット順で最初を出力（全て含むなら "None"）
{% endcapture %}
{% include panel.html type="info" title="文字列の欠損検索（Not Found）" content=notfound_desc %}

<figure class="pseudocode">
  <figcaption>実装（集合とアルファベット走査）</figcaption>
  <pre><code class="language-python">s = input()
s_set = set(s)
for c in "abcdefghijklmnopqrstuvwxyz":
    if c not in s_set:
        print(c)
        break
else:
    print("None")</code></pre>
</figure>

{% capture notfound_points %}
• 集合で高速な存在確認  
• アルファベット順で走査  
• for-else で見つからない場合を処理
{% endcapture %}
{% include panel.html type="steps" title="💡 ポイント" content=notfound_points %}

🧮 パターン4：数学・論理的思考（約15%）
{% capture coins_desc %}
特徴：数学的性質・論理推論  
例：ABC087 B - Coins  
問題：500円A枚、100円B枚、50円C枚でちょうどX円にする方法の数
{% endcapture %}
{% include panel.html type="info" title="数学・論理的思考の例（Coins）" content=coins_desc %}

<figure class="pseudocode">
  <figcaption>実装（2重ループ＋余り判定）</figcaption>
  <pre><code class="language-python">a, b, c, x = map(int, input().split())
count = 0
for i in range(a + 1):      # 500円の枚数
    for j in range(b + 1):  # 100円の枚数
        r = x - 500*i - 100*j
        if r >= 0 and r % 50 == 0:
            k = r // 50
            if k <= c:
                count += 1
print(count)</code></pre>
</figure>

{% capture coins_points %}
• 2重ループ＋余り判定で3重ループを回避  
• 数学的制約（余り）で探索を削減  
• 場合の数を正確にカウント
{% endcapture %}
{% include panel.html type="steps" title="💡 ポイント" content=coins_points %}
```

### B問題攻略の戦略的アプローチ

```
【図7-10：B問題を効率的に解くための戦略】
```
{% capture b_phase1 %}
🎯 Phase 1: 問題理解の深化（5–8分）  
✅ A問題より丁寧に分析  
• 問題文を3回読み、要求を完全に理解  
• 制約（データサイズ/時間）を詳細に確認  
• サンプルの意味を深く理解  
• 解法の方向性を複数検討

🤔 自問自答  
• 本質は何か  
• 全探索で解けるか／効率化は可能か  
• 適切なデータ構造は何か  
• エッジケースはあるか

💡 パターン識別  
• 全探索／カウント／最適化／シミュレーション
{% endcapture %}
{% include panel.html type="steps" title="B問題: Phase 1（理解の深化）" content=b_phase1 %}

{% capture b_phase2 %}
💡 Phase 2: 解法設計（3–5分）  
✅ 実装前の詳細設計  
• アルゴリズムの大枠／データ構造選定  
• 疑似コードで処理の流れを記述  
• 計算量の概算（制約に十分か）

🔍 設計の検証  
• サンプルを手動トレース  
• 計算量が制約内か  
• 実装が複雑すぎないか
{% endcapture %}
{% include panel.html type="steps" title="B問題: Phase 2（解法設計）" content=b_phase2 %}

⌨️ Phase 3: 確実な実装（8–12分）
{% capture b_phase3 %}
✅ 段階的に組み立てる  
• 入力処理 → ロジック → 出力の順で完成  
• ロジックは小さく分け、部分ごとにテスト  
• 条件式は分解して読みやすさを優先

💻 実装のコツ  
• 意味のある変数名／簡潔なコメント  
• デバッグ出力で確認（消し忘れ注意）

🚫 アンチパターン  
• 一気書き／深いネスト／読みにくいワンライナー
{% endcapture %}
{% include panel.html type="steps" title="B問題: Phase 3（実装）" content=b_phase3 %}

{% capture b_phase4 %}
🧪 Phase 4: 徹底的な検証（2–3分）  
✅ サンプル/エッジ/手動計算/計算量の再確認  
🔍 追加テスト: 境界値・特殊条件（同値/0含む等）・自作小ケース  
💡 見落とし: ループ開始（0/1）、範囲外、整数/実数除算、>= と > の違い
{% endcapture %}
{% include panel.html type="steps" title="B問題: Phase 4（徹底検証）" content=b_phase4 %}
```

## 7.4 B問題を実際に解いてみよう

理論の次は実践だ。実際のB問題を段階的に解いて、B問題攻略のコツを体感してみよう。

### 繰り返し処理タイプの実演

```
【図7-11：ABC081 B問題「Shift only」完全解法】

{% capture shift_problem %}
黒板に N 個の正の整数 A1..AN がある。全てが偶数の間、
「全ての数を2で割る」操作を繰り返す。操作回数を求めよ。  
入力: N と A1..AN  
例: N=3, A=[8,12,40] → 出力: 2
{% endcapture %}
{% include panel.html type="info" title="📋 問題文（Shift only／ABC081 B）" content=shift_problem %}

{% capture shift_analysis %}
理解  
• 全偶数の間だけ2で割る → 操作回数  
サンプルトレース  
• [8,12,40] → 1回目:[4,6,20] → 2回目:[2,3,10] → 終了（2回）  
解法  
1) シミュレーション  
2) 各数の「2の因数の個数」の最小値
{% endcapture %}
{% include panel.html type="steps" title="🔍 問題分析" content=shift_analysis %}

{% include panel.html type="steps" title="💡 解法1: シミュレーション（分かりやすい）" content="問題文通りに全偶数の間だけ2で割る操作を繰り返して回数を数える" %}

{% include panel.html type="steps" title="💡 解法2: 数学的（効率的）" content="各要素の『2の因数の個数』の最小値が答え（最初に奇数になる要素が制限要因）" %}

{% capture shift_verify %}
サンプル：[8,12,40]  
• 解法1: 2回で停止（[8,12,40]→[4,6,20]→[2,3,10]）  
• 解法2: 因数の個数 min(3,2,3)=2 → 2回  
どちらも一致。制約に応じて実装を選ぶ。
{% endcapture %}
{% include panel.html type="steps" title="🧪 検証" content=shift_verify %}
<figure class="pseudocode">
  <figcaption>解法1: シミュレーション</figcaption>
  <pre><code class="language-python">n = int(input())
arr = list(map(int, input().split()))
count = 0
while all(x % 2 == 0 for x in arr):
    arr = [x // 2 for x in arr]
    count += 1
print(count)</code></pre>
</figure>

<figure class="pseudocode">
  <figcaption>解法2: 2の因数の個数の最小値</figcaption>
  <pre><code class="language-python">def twos(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c

n = int(input())
arr = list(map(int, input().split()))
print(min(twos(x) for x in arr))</code></pre>
</figure>

### 配列操作タイプの実演

【図7-12：ABC095 B問題「Bitter Alchemy」完全解法】

{% capture bitter_problem %}
N 種類のドーナツがあり、種類 i を1個作るのに必要な小麦粉は m_i グラム。X グラムの小麦粉で、
「各種類を少なくとも1個」作るという条件のもとで作れるドーナツの最大個数を求めよ。  
入力: N X, 次のN行に m_1..m_N  
出力: 最大個数（合計個数）
{% endcapture %}
{% include panel.html type="info" title="📋 問題文（ABC095 B - Bitter Alchemy）" content=bitter_problem %}

{% capture bitter_analysis %}
考え方  
1) まず各種類を1個ずつ作る → `sum(m_i)` を消費  
2) 残り `rem = X - sum(m_i)` で最小コスト `min(m_i)` のドーナツを追加で作る  
3) 合計 = `N + rem // min(m_i)`
{% endcapture %}
{% include panel.html type="steps" title="🔍 分析" content=bitter_analysis %}

<figure class="pseudocode">
  <figcaption>実装（合計個数を計算）</figcaption>
  <pre><code class="language-python">n, x = map(int, input().split())
costs = [int(input()) for _ in range(n)]
required = sum(costs)
rem = x - required
min_cost = min(costs)
print(n + rem // min_cost)</code></pre>
  <figcaption>サンプル検証</figcaption>
  <pre><code class="language-text">入力: n=3, x=1000, m=[120,100,140]
required=360, rem=640, min=100 → 3 + 640//100 = 9（出力例1と一致）</code></pre>
</figure>

## 7.5 時間配分と戦略を立てよう

A問題とB問題の解法を理解したところで、実際のコンテストでの時間配分と戦略について学ぼう。限られた時間の中で最大の成果を出すための戦略的思考が重要だ。

```
【図7-13：ABC 100分コンテストの理想的時間配分】

⏰ フェーズ別時間配分戦略
{% include panel.html type="steps" title="大会の時間配分（全体）" content="0–15分: A確実攻略／15–40分: B挑戦／40–80分: C挑戦・学習／80–100分: 見直し・追加挑戦" %}
```

### フェーズ1：A問題確実攻略（0-15分）

```
【図7-14：A問題攻略フェーズの詳細戦略】

🎯 目標：A問題を確実にAC（正解）する
{% capture a_time %}
⏱️ 理想配分: 0–3分 読解/サンプル → 3–8分 実装 → 8–12分 検証/提出 → 12–15分 バッファ  
🎯 心構え: 完璧より確実／分かりやすい解法／通ったら提出／デバッグに時間を掛けすぎない  
🚨 危険サイン: 10分書けない／サンプル通らない原因不明／読解あいまい→Bへ切替
{% endcapture %}
{% include panel.html type="steps" title="A問題の流れ（15分）" content=a_time %}

📋 A問題での効率的な行動パターン
{% capture a_checklist %}
開始（0–3）: 深呼吸→問題を2回読む→サンプル理解→方針決定  
実装（3–8）: 入力処理から書く／短く意味ある変数名／printで補助  
検証（8–12）: サンプル手動テスト／形式確認／エッジ1–2個／typo/論理チェック  
提出（12–15）: 言語Python3／不要print削除／提出→ACでBへ
{% endcapture %}
{% include panel.html type="steps" title="A問題の実行チェックリスト" content=a_checklist %}
```

### フェーズ2：B問題挑戦（15-40分）

```
【図7-15：B問題挑戦フェーズの戦略的アプローチ】

🎯 目標：B問題のACを狙い、無理なら学習機会として活用

🧠 B問題での思考プロセス最適化
```

### フェーズ3：C問題挑戦・学習（40-80分）

```
【図7-16：C問題との向き合い方（中学生向け）】

🎯 目標：C問題を通じた実力向上と経験積み重ね

⏱️ C問題での時間の使い方
┌─────────────────────────────────────────────┐
{% capture think_experiment %}
💭 思考フェーズ（50–65分）  
• 既知アルゴリズムとの照合／全探索の計算量見積もり  
• より効率的な解法の検討／アイデアをメモ

✏️ 実験フェーズ（65–80分）  
• 簡単な部分だけでも実装  
• サンプルの一部で動作確認  
• 完全でなくても方向性を検証  
• 時間切れでも学習成果をメモ

🎯 成功の基準（下げて継続）  
• 理解できた → 成功  
• アプローチを得た → 大成功  
• 部分実装できた → 良い成果  
• 完全AC → 最高
{% endcapture %}
{% include panel.html type="steps" title="学習重視の進め方" content=think_experiment %}
```

### フェーズ4：見直し・追加挑戦（80-100分）

```
【図7-17：終盤戦での効果的な時間活用】

🔍 優先順位の明確化
{% capture priority_submit %}
1️⃣ 最優先：既存ACの安全確保  
• バグ/出力形式/エッジケースを再確認

2️⃣ 次優先：部分点の可能性  
• C問題など部分解でも提出  
• 小さなテストで確認して提出  
• 計算量が厳しくても方向性重視

3️⃣ 最後：新しい問題への挑戦  
• D以降は読むだけでも価値  
• 問題文理解を次への糧に  
• 無理実装より理解優先
{% endcapture %}
{% include panel.html type="plan" title="提出の優先順位" content=priority_submit %}

📝 コンテスト終了前の最終チェック
{% capture last15 %}
✅ 提出済み確認（5分）: A/BのAC・時刻・言語  
🎯 最後の挑戦（10分）: 解けそうな問題に再トライ／部分点提出／途中コード整理  
📊 振り返り準備（5分）: 成果と課題メモ／分野記録／改善点明確化／解説優先度付け
{% endcapture %}
{% include panel.html type="steps" title="ラスト15分の行動" content=last15 %}
```

## まとめ：A・B問題攻略の基盤完成

この章では、AtCoderの入り口となるA・B問題の攻略法を詳しく学んだ。

```
【図7-18：この章で習得したスキルと成果】

🏆 技術面での成果
{% capture learned %}
✅ A問題の典型パターン理解  
✅ B問題のアプローチ体系化  
✅ 実戦的な実装力  
✅ デバッグ/エラー対応  
✅ 効率的な検証手法
{% endcapture %}
{% include panel.html type="steps" title="この章で得られること（1）" content=learned %}

⏰ 戦略面での成果
{% capture learned2 %}
✅ 時間配分戦略  
✅ 問題優先順位の判断  
✅ 諦めるタイミングの基準  
✅ 継続成長のマインドセット
{% endcapture %}
{% include panel.html type="steps" title="この章で得られること（2）" content=learned2 %}

🎯 実戦での期待成果
{% capture targets %}
🥉 短期: A問題を10分以内で安定正解  
🥈 中期: B問題20分以内の正解率50%  
🥇 長期: A/Bセットを30分以内に正解

📊 レーティング目標  
• A安定正解 → 茶色(400+)  
• A/B安定正解 → 緑(800+)
{% endcapture %}
{% include panel.html type="plan" title="目標設定の目安" content=targets %}
```

**君の競技プログラミング力が確実に向上した**

この章を通じて、君は単にコードを書けるようになっただけでなく、**競技プログラミング特有の問題解決アプローチ**を身につけた。時間制限がある中で、確実に得点する戦略的思考は、競技プログラミング以外の場面でも必ず活かされる。

**次のステップへの準備完了**

```
【図7-19：次章への成長ベクトル】

第7章での達成                第8章での目標
{% capture bridge %}
🏆 A/B理解・実装力・時間配分・マインドセット  →  🧠 体系的解法・デバッグ・品質保証・継続成長
{% endcapture %}
{% include panel.html type="info" title="この章から次章へ" content=bridge %}

🚀 個別の技術から体系的なプロセスへ！
```

第8章では、この章で学んだ技術を更に発展させ、どんな問題にも対応できる体系的な問題解決プロセスを学ぼう。君はもう、競技プログラミングの入り口を確実に通過した。次は、より高度で汎用性のある技術を身につける時だ！

君の成長は止まらない。次の章で、更なる高みを目指そう！
