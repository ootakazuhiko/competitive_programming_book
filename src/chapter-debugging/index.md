---
title: "第9章：エラーと上手に付き合おう"
layout: book
order: 9
checklist:
  - 構文/実行/論理エラーを切り分けられる
  - ログ・一時出力で原因特定できる
pitfalls:
  - 例外メッセージを読まない
  - データ境界の未チェック
exercises:
  - { level: A, text: "典型バグの修正", link: "https://atcoder.jp/contests/abc049/tasks/abc049_a" }
---

<!-- 
本章は「中学生向け競技プログラミング入門書」の一部であり、
CC BY-NC-SA 4.0ライセンスの下で提供されます。
商用利用は事前許諾が必要です。
詳細：../../LICENSE.md
-->

# 第9章：エラーと上手に付き合おう

## 9.1 よくあるエラーメッセージを覚えよう

第8章では体系的な問題解決プロセスを学んだね。でも実際にプログラムを書いていると、必ずエラーに遭遇する。エラーは敵ではなく、プログラムを正しくするためのヒントをくれる「味方」なんだ。

【図9-1：エラーメッセージとの正しい関係】

{% include panel.html type="steps" title="初心者の頃の関係" content="エラー→パニック/諦め→なんとなく修正→別のエラー→無限ループ" %}
{% include panel.html type="steps" title="上級者の関係" content="エラー→ヒントと捉える→メッセージ読解→原因特定→的確に修正→解決/スキルアップ" %}

### Python競技プログラミングでの頻出エラー TOP5

```
【図9-2：エラーメッセージ頻出ランキング】

🥇 第1位：SyntaxError（構文エラー）

{% include panel.html type="info" title="発生頻度/原因" content="約40%／文法ミス（コロン/括弧/インデント）" %}

{% capture syn_patterns %}
❌ コロン(:)の忘れ  
if x > 0        # ← : がない  
    print("positive")

❌ 括弧の対応間違い  
print("Hello World"   # ← ) がない

❌ インデントのずれ  
if x > 0:  
print("positive")     # ← インデントなし
{% endcapture %}
{% include panel.html type="steps" title="よくあるパターン" content=syn_patterns %}

{% capture syn_correct %}
✅ 正しい書き方  
if x > 0:              # コロンあり  
    print("positive")  # インデント4空白
{% endcapture %}
{% include panel.html type="steps" title="正しい書き方" content=syn_correct %}

🥈 第2位：NameError（名前エラー）

{% include panel.html type="info" title="発生頻度/原因" content="約25%／変数名の間違い（タイプミス・未定義）」 %}

{% capture name_patterns %}
❌ タイプミス  
number = 5  
print(nubmer)   # ← スペルミス

❌ 定義前の使用  
print(result)   # ← まだ定義していない  
result = 42
{% endcapture %}
{% include panel.html type="steps" title="よくあるパターン" content=name_patterns %}

{% include panel.html type="steps" title="対策" content="短く意味のある変数名／定義してから使う／エディタ補完を活用" %}

🥉 第3位：IndexError（インデックスエラー）

{% include panel.html type="info" title="発生頻度/原因" content="約20%／範囲外アクセス（長さ超過/空リスト）」 %}

{% capture idx_patterns %}
❌ サイズ超過アクセス  
arr = [1, 2, 3]      # 長さ3  
print(arr[3])        # ← 3番は存在しない

❌ 空リストへのアクセス  
empty_list = []  
print(empty_list[0]) # ← 要素なし
{% endcapture %}
{% include panel.html type="steps" title="よくあるパターン" content=idx_patterns %}

{% capture idx_safe %}
✅ 安全なアクセス  
if len(arr) > 3:  
    print(arr[3])  
else:  
    print("インデックス3は存在しません")
{% endcapture %}
{% include panel.html type="steps" title="安全な書き方" content=idx_safe %}
```

### エラーメッセージの読み方をマスターしよう

```
【図9-3：エラーメッセージ解読の技術】

🔍 Traceback（トレースバック）の読み方

{% capture tb_example %}
Traceback (most recent call last):  
  File "solution.py", line 7, in <module>  
    result = 10 / zero_value  
ZeroDivisionError: division by zero
{% endcapture %}
{% include panel.html type="info" title="実際のエラー例" content=tb_example %}

{% include panel.html type="steps" title="読み方ガイド" content="① File/line → どのファイル・何行目か／② 該当行 → どこで起きたか／③ 例外名と説明 → 種類と要因" %}
{% include panel.html type="steps" title="対処のヒント" content="原因値や状態を確認（例: zero_value が0）／再現を最小化して検証／ログや一時出力で前後の値を追跡" %}

🎯 エラーメッセージから原因を特定する手順

{% include panel.html type="steps" title="ステップ" content="1) 例外の種類を確認（Syntax/Name/Index/ZeroDivisionなど）／2) 発生行を特定（line X と前後）／3) 原因を推測（値/条件/式）／4) 仮説→修正→検証を反復" %}
```

## 9.2 実行時エラーを解決しよう

構文エラーはエディタで気づきやすいけれど、実行時エラーは実際にプログラムを動かしてみないと分からない。でも、パターンを覚えれば対処は意外と簡単なんだ。

【図9-4：実行時エラーの体系的対処法】

🔍 実行時エラーの分類と対策

❌ ZeroDivisionError（ゼロ除算エラー）

{% include panel.html type="info" title="原因" content="0で数値を割ろうとした" %}

{% capture z_bad %}
🚨 問題のあるコード  
a = int(input())  
b = int(input())  
print(a / b)      # b が 0 の場合エラー
{% endcapture %}
{% include panel.html type="steps" title="問題例" content=z_bad %}

{% capture z_good %}
✅ 改善されたコード  
a = int(input())  
b = int(input())  
if b != 0:  
    print(a / b)  
else:  
    print("0で割ることはできません")
{% endcapture %}
{% include panel.html type="steps" title="改善例" content=z_good %}

{% include panel.html type="steps" title="対策" content="除算前に分母0をチェック／入力の妥当性を検証する習慣" %}

❌ ValueError（値エラー）

{% include panel.html type="info" title="原因" content="数値に変換できない文字列をintに変換しようとした" %}

{% capture val_bad %}
🚨 問題のあるコード  
text = "abc"  
number = int(text)   # "abc" は数値ではない
{% endcapture %}
{% include panel.html type="steps" title="問題例" content=val_bad %}

{% capture val_good %}
✅ 改善されたコード  
text = input()  
if text.isdigit():      # 数字かチェック  
    number = int(text)  
    print(f"数値: {number}")  
else:  
    print("数値ではありません")
{% endcapture %}
{% include panel.html type="steps" title="改善例" content=val_good %}

{% include panel.html type="steps" title="対策" content="変換前に妥当性を確認／isdigit()などで事前チェック" %}

❌ TypeError（型エラー）

{% include panel.html type="info" title="原因" content="異なる型同士で演算した（数値+文字列など）" %}

{% capture type_bad %}
🚨 問題のあるコード  
number = 5  
text = "3"  
result = number + text   # 数値と文字列を足している
{% endcapture %}
{% include panel.html type="steps" title="問題例" content=type_bad %}

{% capture type_good %}
✅ 改善されたコード  
number = 5  
text = "3"  
result = number + int(text)   # 文字列→数値に変換  
print(result)   # 8
{% endcapture %}
{% include panel.html type="steps" title="改善例" content=type_good %}

{% include panel.html type="steps" title="対策" content="演算前に型を統一／int()/str()/float()で明示的に変換" %}
```

### デバッグの実践的テクニック

【図9-5：print文デバッグの効果的活用法】

🔧 段階的デバッグの手順（例）

```python
# 問題のあるコード例
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

arr = [10, 20, 30]
result = calculate_average(arr)
print(result)

# ↓ デバッグ版に改造
def calculate_average(numbers):
    print(f"Debug: 受け取った配列 = {numbers}")  # ①入力確認

    total = 0
    for i, num in enumerate(numbers):
        total += num
        print(f"Debug: {i+1}回目, num={num}, total={total}")  # ②処理過程確認

    print(f"Debug: 最終的なtotal = {total}")     # ③中間結果確認
    print(f"Debug: 配列の長さ = {len(numbers)}")  # ④計算要素確認

    result = total / len(numbers)
    print(f"Debug: 計算結果 = {result}")         # ⑤最終結果確認

    return result
```

{% include panel.html type="steps" title="良いデバッグprint" content="Debug: を付けて区別／変数名=値 の形で出す／処理ステップを明記（Step 1 など）" %}
{% include panel.html type="warn" title="分かりにくい例" content="print(x) だけ／"ここ" 等の曖昧なメッセージ／意味のない数値だけ" %}
{% include panel.html type="steps" title="コツ" content="本来の出力と混ざらない工夫／最小限で十分な情報を出す／不要になったら削除する" %}

## 9.3 論理エラーを見つけよう

最も厄介なのが論理エラーだ。プログラムは動くけれど、期待した結果にならない。これはプログラマーの考え方とコンピューターの動作にずれがあるときに起こる。

【図9-6：論理エラーの発見・修正プロセス】

{% include panel.html type="info" title="論理エラーの特徴" content="エラーメッセージは出ない／最後まで実行される／出力が期待と違う／発見が難しく時間がかかる" %}

例：「配列の最大値を求める」

{% capture bug_code %}
🚨 バグのあるコード
```python
def find_max(arr):
    max_val = 0        # ⚠️ 初期値が問題
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# テスト
print(find_max([3, 1, 4]))      # 期待:4, 実際:4 ✅
print(find_max([-1, -5, -2]))   # 期待:-1, 実際:0 ❌
```
🐛 問題: 全要素が負数の時に 0 を返してしまう
{% endcapture %}
{% include panel.html type="steps" title="問題例" content=bug_code %}

🔍 手動トレースによる原因発見

{% capture trace_steps %}
📝 find_max([-1, -5, -2]) の追跡  
Step 1: max_val = 0 で初期化  
Step 2: num = -1, -1 > 0? → False  
Step 3: num = -5, -5 > 0? → False  
Step 4: num = -2, -2 > 0? → False  
Step 5: return 0  

💡 発見: 初期値が0だと、負数が全て無視される
{% endcapture %}
{% include panel.html type="steps" title="動作追跡" content=trace_steps %}

{% capture fix_code %}
✅ 修正版
```python
def find_max(arr):
    max_val = arr[0]       # 最初の要素で初期化
    for num in arr[1:]:    # 2番目から開始
        if num > max_val:
            max_val = num
    return max_val
```
{% endcapture %}
{% include panel.html type="steps" title="修正コード" content=fix_code %}

🧪 境界値テストによる検証

{% capture test_design %}
🎯 テストケース設計  

✅ 正常ケース  
• [1, 2, 3, 4, 5] → 5  
• [10, 5, 8] → 10  

✅ 境界ケース  
• [5] → 5（単一要素）  
• [-1, -2, -3] → -1（全負数）  
• [0, 0, 0] → 0（全ゼロ）  

✅ 特殊ケース  
• [100, -50, 200] → 200（正負混在）  
• [5, 5, 5] → 5（同値）  

💡 テストの考え方  
• 期待される動作ケース／想定外の入力／数学的に特別な値
{% endcapture %}
{% include panel.html type="steps" title="テスト設計" content=test_design %}

### 逆算チェックの技法

【図9-7：期待される出力からの逆算検証】

{% include panel.html type="steps" title="逆算チェックの手順" content="1) 期待出力を自分で手計算／2) 問題文を再読し解釈のズレを潰す／3) コードのロジックを手計算と突き合わせ" %}

例題：「配列の合計がKになる部分配列の個数」  入力: arr=[1,2,3,4], K=5  期待出力: 2

{% capture reverse_example %}
📝 手動計算の要約  
• 部分配列と合計を列挙し、K=5 になる組を数える  
• 例: [2,3] → 5 ✅、他は不一致  
• 手計算の結果と「期待出力=2」に差があれば、解釈のズレを疑う

💡 ありがちなズレの例  
• 問題は「連続部分配列」か「部分集合」か  
• 「個数」か「存在判定」か  
• 複数テストケース/入力形式の読み違い
{% endcapture %}
{% include panel.html type="steps" title="例題の検証" content=reverse_example %}

## 9.4 AtCoderでの「Wrong Answer」対策

競技プログラミング特有のエラー「Wrong Answer（WA）」は、プログラムは動くが期待される出力と異なる結果を出力した時に出る。これを解決するコツを覚えよう。

```
【図9-8：Wrong Answer の体系的対処法】

{% include panel.html type="steps" title="WA分析のフロー" content="1) 出力形式の厳密確認／2) サンプルで手動追跡／3) エッジケース検証／4) 解法の見直し" %}

{% capture fmt_mistakes %}
❌ よくある出力形式ミス  
• 余分な改行: 直後の不要な print()  
• 区切り違い: sep=','（本来は空白）  
• 大小文字違い: yes vs Yes  
• 数値の形式: 小数/整数/桁数の不一致
{% endcapture %}
{% include panel.html type="warn" title="出力形式チェック" content=fmt_mistakes %}

{% capture debug_flow %}
🔍 計算ロジック検証（stderr活用）  
• 入力直後に Debug: n, arr を出す  
• 計算直後に Debug: result を出す  
• 提出前にデバッグ文は必ず削除（stderrは影響しないが癖づける）
{% endcapture %}
{% include panel.html type="steps" title="段階的検証" content=debug_flow %}

{% capture edge_cases %}
🔍 エッジケース網羅  
• サイズ: N=1／N=上限（計算量OK?）  
• 値: 全要素同値／最小・最大境界／負数・ゼロ  
• 構造: ソート済み/逆順／重複／空/単一
{% endcapture %}
{% include panel.html type="steps" title="エッジケース" content=edge_cases %}
│                                           │
│ 📝 自作テストケース例：                     │
│ # 最小ケース                               │
│ 1                                          │
│ 5                                          │
│                                           │
│ # 重複ケース                               │
│ 3                                          │
│ 2 2 2                                      │
│                                           │
│ # 境界値ケース                             │
│ 2                                          │
│ 1000000000 1000000000                     │
└─────────────────────────────────────────────┘
```

### AtCoder特有のトラブルシューティング

【図9-9：AtCoder提出時のよくある失敗と対策】

{% include panel.html type="steps" title="提出前チェック" content="言語がPython (CPython 3.x)／デバッグprintを全削除／コード全体を正しく貼付／サンプルで動作確認／出力形式が完全一致" %}

{% capture submit_warn %}
🎯 典型ミス  
• 言語選択: PyPy/Python2.7 を誤選択  
• コピペ: 一部欠落や余分な文字  
• デバッグ文残存: Debug 出力が混入
{% endcapture %}
{% include panel.html type="warn" title="注意" content=submit_warn %}

{% include panel.html type="steps" title="WA時の段階的対処" content="Phase 1: 出力形式の再確認（改行/空白/大小文字）／Phase 2: サンプル手動追跡／Phase 3: エッジケース検証（境界値）／Phase 4: 解法見直し" %}

## 9.5 「Time Limit Exceeded」を解決しよう

TLE（Time Limit Exceeded）は、プログラムの実行時間が制限時間を超えた時に出るエラーだ。正しい答えは出るけれど、計算に時間がかかりすぎるということ。

```
【図9-10：TLE対策の段階的アプローチ】

⏰ TLE（Time Limit Exceeded）の原因分析

🔍 原因1: アルゴリズムの計算量が過大
┌─────────────────────────────────────────────┐
│ よくある問題パターン：                      │
│                                           │
│ ❌ 不要な二重ループ：                       │
│ for i in range(n):                         │
│     for j in range(n):                     │
│         if arr[i] == target:  # 内側で毎回同じチェック│
│             count += 1                     │
│ # 計算量：O(N²) → N=100,000なら100億回計算  │
│                                           │
│ ✅ 改善版：                                │
│ count = 0                                  │
│ for x in arr:                              │
│     if x == target:                        │
│         count += 1                         │
│ # 計算量：O(N) → N=100,000なら10万回計算    │
│                                           │
│ 💡 改善のポイント：                        │
│ • 不要な重複処理を削除                     │
│ • 一度の処理で済ませられることは一度だけ     │
└─────────────────────────────────────────────┘

🔍 原因2: 非効率なデータ構造の使用
┌─────────────────────────────────────────────┐
│ ❌ リストでの検索（O(N)）：                  │
│ def count_occurrences(arr, target):        │
│     count = 0                              │
│     for x in arr:                          │
│         if x == target:                    │
│             count += 1                     │
│     return count                           │
│                                           │
│ # 毎回O(N)の検索が発生                      │
│ for target in queries:                     │
│     result = count_occurrences(arr, target)│
│ # 全体でO(N×M) → 場合によっては数十億回計算  │
│                                           │
│ ✅ 辞書を使った高速化（O(1)）：              │
│ from collections import Counter            │
│ counter = Counter(arr)    # O(N)で前処理   │
│ for target in queries:                     │
│     result = counter[target]  # O(1)で取得 │
│ # 全体でO(N+M) → 大幅な高速化               │
└─────────────────────────────────────────────┘

🔍 原因3: Python特有のパフォーマンス問題
┌─────────────────────────────────────────────┐
│ ❌ 遅い書き方：                            │
│ result = []                                │
│ for i in range(n):                         │
│     result.append(str(arr[i]))             │
│ output = '\n'.join(result)                 │
│                                           │
│ ✅ 高速化テクニック：                       │
│ # リスト内包表記の使用                      │
│ result = [str(x) for x in arr]             │
│ output = '\n'.join(result)                 │
│                                           │
│ # さらに高速化                             │
│ output = '\n'.join(map(str, arr))          │
│                                           │
│ # 大量出力の場合のさらなる最適化             │
│ import sys                                 │
│ for x in arr:                              │
│     sys.stdout.write(str(x) + '\n')       │
└─────────────────────────────────────────────┘
```

### 計算量の見積もりと改善

```
【図9-11：制約から計算量を逆算する技術】

📊 制約と許容される計算量の目安
┌─────────────────────────────────────────────┐
│ N ≤ 10        → あらゆるアルゴリズム使用可能  │
│ N ≤ 20        → O(2^N)の全探索も可能         │
│ N ≤ 100       → O(N^3)まで                 │
│ N ≤ 1,000     → O(N^2)まで                 │
│ N ≤ 100,000   → O(N log N)まで             │
│ N ≤ 1,000,000 → O(N)まで                   │
│                                           │
│ 💡 安全マージンの考え方：                   │
│ • 見積もりの2-3倍の余裕を見る               │
│ • Pythonは他言語より3-5倍遅いことを考慮      │
│ • 実装の複雑さも計算量に影響する            │
│                                           │
│ 🎯 判断例：                               │
│ N≤1000の制約で二重ループ（O(N^2)）は安全    │
│ N≤100000で二重ループはTLEの危険性大        │
└─────────────────────────────────────────────┘

🚀 高速化チェックリスト
┌─────────────────────────────────────────────┐
│ ✅ アルゴリズムの計算量見直し：              │
│ • 全探索 → 二分探索・ハッシュ活用           │
│ • 毎回計算 → 前処理・メモ化                │
│ • 重複処理 → 一度だけの処理に変更           │
│                                           │
│ ✅ データ構造の最適化：                     │
│ • リスト検索 → 辞書・集合活用              │
│ • 文字列結合 → join使用                   │
│ • 動的配列 → 事前サイズ確保                │
│                                           │
│ ✅ Python固有の最適化：                    │
│ • for文 → リスト内包表記                  │
│ • 関数呼び出し回数削減                     │
│ • import文の効率化                        │
│                                           │
│ ✅ 最後の手段：                           │
│ • PyPy での提出（通常の Python より高速）   │
│ • アルゴリズム自体の根本的見直し            │
│ • 問題の制約をもう一度確認                  │
└─────────────────────────────────────────────┘
```

### TLE解決の実践例

```
【図9-12：実際のTLE解決プロセス】

🎯 例題：「N個の数から2つ選んで積がKになるペアの個数」

❌ TLEするコード（O(N²)）：
┌─────────────────────────────────────────────┐
│ n, k = map(int, input().split())             │
│ arr = list(map(int, input().split()))        │
│                                           │
│ count = 0                                  │
│ for i in range(n):                         │
│     for j in range(i+1, n):               │
│         if arr[i] * arr[j] == k:           │
│             count += 1                     │
│ print(count)                               │
│                                           │
│ 問題：N=100,000の場合、約50億回の計算        │
│ → 明らかにTLE                              │
└─────────────────────────────────────────────┘

✅ 高速化されたコード（O(N)）：
┌─────────────────────────────────────────────┐
│ from collections import Counter            │
│ n, k = map(int, input().split())           │
│ arr = list(map(int, input().split()))      │
│                                           │
│ counter = Counter(arr)                     │
│ count = 0                                  │
│                                           │
│ for num in counter:                        │
│     if k % num == 0:      # numで割り切れる場合│
│         partner = k // num                 │
│         if partner in counter:             │
│             if num == partner:             │
│                 # 同じ数同士のペア          │
│                 count += counter[num] * (counter[num] - 1) // 2│
│             elif num < partner:            │
│                 # 異なる数のペア            │
│                 count += counter[num] * counter[partner]│
│ print(count)                               │
│                                           │
│ 改善：N=100,000でも10万回程度の計算で完了    │
└─────────────────────────────────────────────┘
```

## まとめ：エラーは成長への階段

この章では、プログラミングで避けて通れないエラーとの正しい付き合い方を学んだね。

```
【図9-13：この章で身につけたエラー対応力】

🛠️ 習得したスキル
┌─────────────────────────────────────────────┐
│ ✅ エラーメッセージの正確な読解              │
│ ✅ 段階的デバッグによる原因特定              │
│ ✅ 論理エラーの発見と修正技法               │
│ ✅ AtCoder特有の問題への対処法              │
│ ✅ TLE対策と計算量最適化                   │
└─────────────────────────────────────────────┘

🧠 身についた考え方
┌─────────────────────────────────────────────┐
│ • エラーは「敵」ではなく「成長への手がかり」  │
│ • 問題を段階的に分解して解決する習慣        │
│ • 仮説を立てて検証するサイクル              │
│ • あきらめずに原因を追究する粘り強さ        │
└─────────────────────────────────────────────┘

🚀 次のステップ
┌─────────────────────────────────────────────┐
│ 第10章: コンテストに参加してみよう           │
│ • 学んだエラー対応力の実戦での活用           │
│ • 時間制限下での効率的なデバッグ            │
│ • コンテスト特有の環境での問題解決           │
└─────────────────────────────────────────────┘
```

**エラーとの正しい関係を築けた君へ**

エラーに遭遇したとき、もうパニックになることはないはずだ。エラーメッセージを冷静に読み、段階的に原因を特定し、的確に修正する。この技術は、競技プログラミングだけでなく、将来プロのエンジニアになったときにも必ず役立つ。

**実戦での活用に向けて**

次の章では、いよいよ実際のAtCoderコンテストに参加する方法を学ぶよ。君が身につけたエラー対応力を、時間制限のあるコンテストでどう活用するか、実戦的なコツを身につけよう！
