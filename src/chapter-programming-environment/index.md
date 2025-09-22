---
title: "第3章：プログラミング環境を整えよう"
layout: book
order: 3
---

<!-- 
本章は「中学生向け競技プログラミング入門書」の一部であり、
CC BY-NC-SA 4.0ライセンスの下で提供されます。
商用利用は事前許諾が必要です。
詳細：/LICENSE.md
<!--
  ※ 上記のリンクはプロジェクトルートからの絶対パスを想定しています。ディレクトリ構成を変更する場合はご注意ください。
-->

# 第3章：プログラミング環境を整えよう

## 章の学習目標

この章を読み終わることで、以下ができるようになります：
- Pythonを選ぶ理由を理解し、適切にインストールできる
- 競技プログラミングに適したエディタを設定できる
- AtCoderで実際にコードを提出できる
- 基本的なデバッグ技術を使って問題を解決できる

第2章でAtCoderの世界を理解したね。今度は実際に競技プログラミングを始めるための「道具」を準備しよう。料理人にとっての包丁や、画家にとっての筆のように、プログラマーにとって開発環境は成果を大きく左右する重要な要素なんだ。

## 3.1 なぜPythonを選ぶの？

### Scratchからの自然なステップアップ

[図3-1：ScratchからPythonへの自然な進化]

君がScratchを使っていた時を思い出してみよう。「もし〜なら」のブロックを使って条件分岐を作ったり、「〜回繰り返す」のブロックでループを作ったりしていたよね。Pythonは、そのScratchの考え方をそのまま文字で表現できる言語なんだ。

```python
# Scratchの「もし x > 0 なら」は
if x > 0:
    print("正の数です")

# Scratchの「10回繰り返す」は  
for i in range(10):
    print(i)
```

### 競技プログラミングでのPythonの優位性

![図3-2：競技プログラミング言語比較表]({{ site.baseurl }}/assets/diagrams/chapter3/figure3-2-programming-language-comparison.svg)

**なぜPythonが初心者に最適なのか**

1. **読みやすさ第一の設計**
   - コードが英語の文章のように読める
   - インデント（字下げ）で構造が一目で分かる
   - 余計な記号が少なく、本質に集中できる

2. **豊富な標準ライブラリ**
   - 数学計算、文字列処理、データ構造など基本的な機能が充実
   - 車輪の再発明をする必要がない
   - より高レベルな問題解決に集中できる

3. **エラーメッセージの親切さ**
   - 何が間違っているか具体的に教えてくれる
   - 初心者がつまづきやすいポイントを明確に指摘
   - デバッグが他の言語より格段に楽

4. **AtCoderでの実績**
   - 多くの日本人競技プログラマーが使用
   - 実行時間制限も十分（ほとんどの問題で間に合う）
   - 豊富な解説記事とサンプルコード

### 将来性も考慮した言語選択

![図3-3：Pythonの将来性と応用分野]({{ site.baseurl }}/assets/diagrams/chapter3/figure3-3-python-future-applications.svg)

Pythonを学ぶことは、単に競技プログラミングのためだけではない。将来、どの技術分野に進んでも活用できる、投資価値の高いスキルなんだ。

## 3.2 Pythonをインストールしよう

### インストール前の準備確認

まず、君のパソコンの状況を確認しよう：

【図3-4：事前確認チェックリスト】

{% capture precheck_hw %}
✅ ハードウェア要件  
• Windows 10/11、macOS 10.9以降、または Linux  
• 空き容量: 最低100MB（推奨1GB以上）  
• メモリ: 最低512MB（推奨2GB以上）
{% endcapture %}
{% include panel.html type="steps" title="ハードウェア" content=precheck_hw %}

{% capture precheck_perm %}
✅ 権限の確認  
• 管理者権限（または保護者の許可）  
• インターネット接続  
• セキュリティソフト設定の確認
{% endcapture %}
{% include panel.html type="info" title="権限/ネットワーク" content=precheck_perm %}

{% capture precheck_env %}
✅ 学習環境  
• 集中できる時間（30分〜1時間）  
• メモの準備（紙/デジタル）
{% endcapture %}
{% include panel.html type="steps" title="学習環境" content=precheck_env %}

### Windows版インストール手順（詳細版）

Windowsユーザーが最も多いため、詳しく説明するね。

![図3-5：Windows Pythonインストールガイド]({{ site.baseurl }}/assets/diagrams/chapter3/figure3-5-windows-python-install.svg)

### macOS版インストール手順

【図3-6：macOS Python インストールガイド】

{% capture macos_installer %}
方法1（推奨）: 公式インストーラー  
1) https://python.org から macOS 版をダウンロード  
2) .pkg を実行  
3) 管理者パスワード入力→インストール  
4) `python3 --version` で確認
{% endcapture %}
{% include panel.html type="steps" title="公式インストーラー" content=macos_installer %}

{% capture macos_brew %}
方法2（上級者）: Homebrew  
• `brew install python` で最新版を管理
{% endcapture %}
{% include panel.html type="info" title="Homebrew" content=macos_brew %}

{% capture macos_check %}
確認  
• ターミナルを開く  
• `python3 --version` を実行  
• `python3 -c "print('macOS OK')"`
{% endcapture %}
{% include panel.html type="steps" title="動作確認" content=macos_check %}

### トラブルシューティング

インストールでよくあるトラブルと解決方法：

【図3-7：よくあるトラブルと解決方法】

{% capture tr_path %}
❌ 問題: "python が認識されません"  
原因: PATH 設定漏れ  
対処: 1) 再インストール  2) 「Add Python to PATH」にチェック  3) 端末を再起動
{% endcapture %}
{% include panel.html type="warn" title="PATHエラー" content=tr_path %}

{% capture tr_admin %}
❌ 問題: 管理者権限がない  
対処: 1) 保護者に依頼  2) 学校PCは先生に相談  3) ポータブル版Pythonを検討
{% endcapture %}
{% include panel.html type="warn" title="権限エラー" content=tr_admin %}

{% capture tr_versions %}
❌ 問題: 古いバージョンが起動する  
原因: 複数Pythonの混在  
対処: 1) macOS/Linux: `python3` を使用  2) Windows: `py -3` を使用  3) フルパス指定
{% endcapture %}
{% include panel.html type="warn" title="複数バージョン衝突" content=tr_versions %}

{% capture tr_flow %}
🔧 総合手順  
1) 管理者権限で再実行  
2) セキュリティソフト一時無効  
3) 公式ドキュメント確認  
4) コミュニティで質問
{% endcapture %}
{% include panel.html type="steps" title="困ったときの流れ" content=tr_flow %}

## 3.3 エディタを選んで設定しよう

### エディタ選択の重要性

プログラミングエディタは、君がこれから長時間向き合うことになる重要なパートナーだ。良いエディタを選ぶことで、学習効率が大幅に向上する。

```
【図3-8：初心者向けエディタ選択マトリックス】

          使いやすさ  高機能  軽量性  学習コスト  総合評価
Thonny      ★★★★★   ★★☆   ★★★     ★★★★★    ★★★★★
VSCode      ★★★★☆   ★★★★★ ★★☆     ★★★☆☆    ★★★★☆
IDLE        ★★★☆☆   ★★☆   ★★★★☆   ★★★★★    ★★★☆☆
PyCharm     ★★☆☆☆   ★★★★★ ★☆☆     ★★☆☆☆    ★★★☆☆
Sublime     ★★★☆☆   ★★★☆☆ ★★★★☆   ★★★☆☆    ★★★☆☆

🎯 初心者には Thonny を最推奨
🎯 少し慣れたら VSCode への移行を検討
```

### Thonny：完璧な初心者向けエディタ

Thonnyは、プログラミング教育のために特別に設計されたエディタだ。

![図3-9：Thonnyの特徴と利点]({{ site.baseurl }}/assets/diagrams/chapter3/figure3-9-thonny-features.svg)

### VSCode：成長とともに使える高機能エディタ

Thonnyに慣れてきたら、VSCodeへの移行を検討しよう。世界中のプロのプログラマーが使っている本格的なエディタだ。

【図3-10：VSCode セットアップ完全ガイド】

{% capture vs_install %}
📥 基本インストール  
1) https://code.visualstudio.com にアクセス  
2) Download をクリック  
3) インストーラーを実行  
4) 初回起動時に日本語化
{% endcapture %}
{% include panel.html type="steps" title="インストール" content=vs_install %}

{% capture vs_ext %}
🔌 必須拡張機能  
• Python Extension Pack（言語/補完/Lint/デバッグ）  
• 便利: Bracket Pair Colorizer, indent-rainbow, Code Runner
{% endcapture %}
{% include panel.html type="info" title="拡張機能" content=vs_ext %}

{% capture vs_settings %}
⚙️ 推奨設定  
• 自動保存: 有効  
• フォント: 14px  
• テーマ: Dark+  
• 行番号: 有効／ミニマップ: 無効  
• ショートカット: F5 実行, Ctrl+S 保存, Ctrl+/ コメント
{% endcapture %}
{% include panel.html type="steps" title="競プロ向け設定" content=vs_settings %}

### 開発環境の基本操作

どのエディタを選んでも、基本的な操作は共通している：

【図3-11：プログラミングエディタ基本操作】

{% capture edit_files %}
📂 ファイル操作  
• 新規: Ctrl+N  
• 保存: Ctrl+S  
• 拡張子: .py（例: abc001_a.py, practice.py）
{% endcapture %}
{% include panel.html type="steps" title="ファイル操作" content=edit_files %}

{% capture edit_code %}
⌨️ コード編集  
• コピー/切り取り: Ctrl+C/Ctrl+X  
• 貼り付け/元に戻す: Ctrl+V/Ctrl+Z  
• 行選択: 行番号クリック  
• 検索/置換: Ctrl+F / Ctrl+H  
• 複数行コメント: Ctrl+/
{% endcapture %}
{% include panel.html type="steps" title="コード編集" content=edit_code %}

{% capture run_debug %}
🚀 実行/デバッグ  
• 実行: F5 または実行ボタン  
• 停止: Ctrl+C  
• ターミナル: Ctrl+`  
• エラー箇所ジャンプ: メッセージをクリック
{% endcapture %}
{% include panel.html type="steps" title="実行とデバッグ" content=run_debug %}

## 3.4 AtCoderでコードを提出してみよう

### 初回提出の完全ガイド

いよいよ、実際にAtCoderでコードを提出してみよう！最初は緊張するかもしれないが、一度やってみれば意外と簡単だよ。

![図3-12：AtCoder初回提出フローチャート]({{ site.baseurl }}/assets/diagrams/chapter3/figure3-12-atcoder-first-submission.svg)

### 練習問題での実習

まずは「practice contest」で練習してみよう：

【図3-13：Practice Contest 参加手順】

{% capture step1 %}
Step 1: アクセス  
1) AtCoderにログイン  
2) Contests から practice contest を検索  
3) Practice Contest を開く  
4) 「A - Welcome to AtCoder」を選択
{% endcapture %}
{% include panel.html type="steps" title="アクセス手順" content=step1 %}

{% capture step2 %}
Step 2: 問題文  
整数 a、整数 b、文字列 s が与えられる。a+b と s を出力しなさい。  
入力例: (1) / (2 3) / (test) → 出力例: 6 test
{% endcapture %}
{% include panel.html type="info" title="問題文と例" content=step2 %}

<figure class="pseudocode">
  <figcaption>Step 3: 解答例</figcaption>
  <pre><code class="language-python">a = int(input())
b, c = map(int, input().split())
s = input()
print(a + b + c, s)</code></pre>
</figure>

### 提出画面の詳細操作

【図3-14：AtCoder提出画面ガイド】

{% include panel.html type="steps" title="提出前チェックポイント" content="言語がPythonか／文法エラーなし／インデント正しい／inputの数一致／出力形式正しい" %}

{% include panel.html type="info" title="入力例と解答コード（再掲）" content="上のStep 3の解答例をそのまま貼り付けて提出」 %}

{% capture result_notes %}
結果表示の見方  
• ✅ AC (Accepted): 正解  
• ❌ WA (Wrong Answer): 不正解  
• ❌ TLE (Time Limit Exceeded): 時間切れ  
• ❌ RE (Runtime Error): 実行時エラー  
• ❌ CE (Compilation Error): 文法エラー
{% endcapture %}
{% include panel.html type="info" title="提出結果の見方" content=result_notes %}

提出後の結果表示：
✅ AC (Accepted): 正解！
❌ WA (Wrong Answer): 不正解
❌ TLE (Time Limit Exceeded): 時間切れ
❌ RE (Runtime Error): 実行時エラー
❌ CE (Compilation Error): 文法エラー
```

### よくある提出ミスと対策

```
【図3-15：初心者の典型的な提出ミス】

❌ ミス1: 出力形式の間違い
{% include panel.html type="steps" title="出力の空白と結合" content="print(a, b) は空白区切り（例: 1 2）／文字列連結なら '12' になるので問題文に合わせる" %}

❌ ミス2: 不要な出力
{% include panel.html type="steps" title="提出時の出力は答えのみ" content="余計な説明文を出力しない／期待されるフォーマットに厳密に合わせる" %}
```python
# 間違い
a = int(input())
print("aの値は", a)
print(a * 2)

# 正しい
a = int(input())
print(a * 2)  # 答えのみ
```

❌ ミス3: input()の数の間違い
{% include panel.html type="steps" title="複数行入力の基本" content="1行ずつ input() を読む／split() は1行の多値入力に使う" %}
```python
# 2行で N と M が与えられる例
n = int(input())
m = int(input())
<<<<<<< HEAD
=======
```

🛡️ ミス防止のチェックリスト：
1. サンプル入出力で必ずテスト
2. 出力に余計な文字が含まれていないか確認
3. 改行・スペースが問題文通りか確認
4. デバッグ用のprint文を削除したか確認
>>>>>>> origin/main
```

{% capture submit_check %}
1) サンプルで必ずテスト  
2) 余計な文字がないか  
3) 改行・スペースが指示通りか  
4) デバッグ用 print を消したか
{% endcapture %}
{% include panel.html type="steps" title="提出前チェックリスト" content=submit_check %}

## 3.5 デバッグの基本を覚えよう

### デバッグマインドセット

「バグ（プログラムの間違い）は敵ではなく、成長のための大切な先生だ」という考え方を身につけよう。

【図3-16：デバッグの心構え】

{% capture mindset %}
避けるべき考え方 → 推奨される考え方  
• 「また間違えた…」 → 「新しい発見のチャンス！」  
• 「向いていない」 → 「経験が実力向上につながる」  
• 「すぐ答えを見る」 → 「まず自分で原因を探す」
{% endcapture %}
{% include panel.html type="info" title="前向きマインド" content=mindset %}

{% include panel.html type="info" title="デバッグは探偵ゲーム" content="なぜ期待通りに動かない？という謎解きを楽しもう" %}

### print文を使ったデバッグ技法

最も基本的で効果的なデバッグ方法は、`print`文を使って変数の値を確認することだ。

```
【図3-17：print文デバッグの実践例】

問題のあるコード例：
```python
n = int(input())
total = 0
for i in range(n):
    x = int(input())
    total += x
print(total // 2)  # なぜか答えが違う...
```

デバッグ版（print文追加）：
```python
n = int(input())
print(f"🔍 n = {n}")  # 👈 確認用
total = 0
for i in range(n):
    x = int(input())
    print(f"🔍 i={i}, x={x}")  # 👈 確認用
    total += x
    print(f"🔍 total={total}")  # 👈 確認用
print(f"🔍 最終total = {total}")  # 👈 確認用
print(total // 2)
```

デバッグ実行例：
🔍 n = 3
🔍 i=0, x=10
🔍 total=10
🔍 i=1, x=20
🔍 total=30
🔍 i=2, x=30
🔍 total=60
🔍 最終total = 60
30

💡 分析結果：
totalの計算は正しい。問題は「total // 2」の部分。
問題文を再確認すると、平均値ではなく合計値を求める問題だった！
```

### エラーメッセージの読み方

Pythonのエラーメッセージは実は非常に親切だ。正しく読み方を覚えれば、問題の場所がすぐに分かる。

```
【図3-18：エラーメッセージ解読ガイド】

典型的なエラーメッセージ：
```text
Traceback (most recent call last):
  File "abc001_a.py", line 4, in <module>
    result = x / y
ZeroDivisionError: division by zero
```

📖 読み方：
{% capture tb_howto %}
1) エラー種別: ZeroDivisionError → 0 で割った  
2) 場所: abc001_a.py の 4 行目  
3) 該当コード: result = x / y  
4) 具体的原因: division by zero（ゼロによる除算）
{% endcapture %}
{% include panel.html type="steps" title="エラーメッセージの読み方" content=tb_howto %}

🔧 解決方法：
```python
# エラー回避版
if y != 0:
    result = x / y
else:
    print("エラー：ゼロで割ることはできません")
```
```

### 頻出エラーと解決法

```
【図3-19：Python初心者の頻出エラー辞典】

{% include panel.html type="info" title="SyntaxError（文法エラー）" content=": の付け忘れ／括弧の対応ミス／インデント幅不統一／全角混入。エディタの文法チェック活用" %}

{% include panel.html type="info" title="NameError（未定義名）" content="タイプミス／定義前参照／大文字小文字。短く分かりやすい命名で統一" %}

{% include panel.html type="warn" title="IndexError（範囲外）" content="arr[5] だが 0..3 まで／空リスト。len()で境界確認を習慣化" %}
```

### ステップ実行によるデバッグ

より高度なデバッグ技法として、ステップ実行がある。ThonnyとVSCodeの両方で使える。

```
【図3-20：ステップ実行デバッグ手順】

🔍 Thonnyでのステップ実行
{% capture thonny_steps %}
1) Debug メニュー → Step by step  
2) Step into で1行ずつ実行  
3) Variables で値を確認  
4) 問題箇所で何が起きているか分析
{% endcapture %}
{% include panel.html type="steps" title="Thonny ステップ実行" content=thonny_steps %}

🔍 VSCodeでのステップ実行
{% capture vscode_steps %}
1) 行番号左をクリックしてブレークポイント  
2) F5 でデバッグ開始／F10 で次の行へ  
3) VARIABLES で変数確認／CALL STACK で呼び出し確認
{% endcapture %}
{% include panel.html type="steps" title="VSCode ステップ実行" content=vscode_steps %}

💡 ステップ実行の利点：
• 変数の値の変化を追跡できる
• どの行で問題が起きるか特定できる
• プログラムの動作を深く理解できる
• 複雑なロジックも段階的に検証できる
```

## まとめ：環境構築完了！次のステップへ

この章では、競技プログラミングを始めるための実践的な環境を整えた。

{% capture ch3_done %}
• Python をインストール・確認  
• エディタ設定と基本操作の習得  
• AtCoder で提出体験  
• print デバッグの実践  
• よくあるエラーの対処法
{% endcapture %}
{% include panel.html type="info" title="この章で身につけたスキル" content=ch3_done %}

{% capture next_steps %}
第4章: 入出力処理の完全マスター  
• もっとも重要な基本技術  
• 様々な入力形式の扱い方  
• 効率的な出力のコツ
{% endcapture %}
{% include panel.html type="steps" title="次のステップ" content=next_steps %}

君はもう競技プログラミングを始める準備が整った！Pythonがインストールされ、使いやすいエディタが設定され、AtCoderでの提出方法も分かった。そして何より重要なのは、エラーを恐れずにデバッグする技術を身につけたことだ。

プログラミングにおいて、エラーは敵ではなく成長のための重要な教師だ。今後もたくさんのエラーに出会うだろうが、この章で学んだデバッグ技術があれば、必ず解決できる。

次の章では、競技プログラミングの基本中の基本である「入出力処理」を詳しく学んでいこう。これをマスターすれば、AtCoderの問題に本格的に挑戦できるようになるよ！
