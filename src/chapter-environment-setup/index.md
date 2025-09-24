---
title: "第2章：AtCoderへの第一歩"
layout: book
order: 2
---

<!-- 
本章は「中学生向け競技プログラミング入門書」の一部であり、
CC BY-NC-SA 4.0ライセンスの下で提供されます。
商用利用は事前許諾が必要です。
詳細：../../LICENSE.md
-->

# 第2章：AtCoderへの第一歩

## 2.1 AtCoderってどんなサイト？

第1章では競技プログラミングの楽しさや価値について学んだね。今度は実際に、日本最大級の競技プログラミングサイト「AtCoder」を探検してみよう！

![図2-1：AtCoderの全体像]({{ site.baseurl }}/assets/diagrams/chapter2/figure2-1-atcoder-overview.svg)

**AtCoderの特別なところ**

AtCoderは他の競技プログラミングサイトと比べて、中学生の君にとって特に優れた特徴がある：

![図2-2：AtCoderの中学生にとってのメリット]({{ site.baseurl }}/assets/diagrams/chapter2/figure2-2-middle-school-benefits.svg)

**世界の中でのAtCoderの位置づけ**

【図2-3：世界の競技プログラミングサイト比較】

{% capture world_sites_left %}
🌍 世界規模（例: Codeforces）  
• 世界最高峰・上級者向け  
• 英語UI  
• 高速な判定／多彩なラウンド
{% endcapture %}
{% include panel.html type="info" title="世界規模サイト" content=world_sites_left %}

{% capture world_sites_right %}
🇯🇵 日本特化（AtCoder）  
• 教育重視・初心者歓迎  
• 日本語UI  
• 公式解説が充実
{% endcapture %}
{% include panel.html type="info" title="日本特化サイト" content=world_sites_right %}

{% capture learning_flow %}
🔄 学習の流れ  
AtCoderで基礎固め → 実力向上 → Codeforcesに挑戦（将来の目標）
{% endcapture %}
{% include panel.html type="steps" title="学習パス（推奨）" content=learning_flow %}

**AtCoderで何ができる？**

【図2-4：AtCoderでできることマップ】

{% capture atcoder_map_contest %}
🏆 コンテスト  
• 土日に開催／リアルタイム  
• 他の参加者と競争／成績反映
{% endcapture %}
{% include panel.html type="info" title="コンテスト" content=atcoder_map_contest %}

{% capture atcoder_map_practice %}
📚 過去問練習  
• いつでも利用可能／自分のペース  
• 苦手分野を集中的に練習
{% endcapture %}
{% include panel.html type="info" title="過去問練習" content=atcoder_map_practice %}

{% capture atcoder_map_comm %}
👥 コミュニティ  
• 情報交換／解法の議論  
• 仲間作り・ネットワーキング
{% endcapture %}
{% include panel.html type="info" title="コミュニティ" content=atcoder_map_comm %}

{% capture atcoder_map_outcomes %}
📈 レーティング上昇／💪 スキルアップ／🤝 ネットワーキング
{% endcapture %}
{% include panel.html type="steps" title="得られるもの" content=atcoder_map_outcomes %}

## 2.2 アカウントを作ってみよう

いよいよAtCoderのアカウントを作成しよう！手順は簡単だけど、将来のことを考えて慎重に設定していこう。

**準備するもの**
- パソコンまたはスマートフォン
- インターネット接続
- メールアドレス（Gmail、Yahoo!メールなど）

![図2-5：アカウント作成の全体の流れ]({{ site.baseurl }}/assets/diagrams/chapter2/figure2-5-account-creation-flow.svg)

### Step 1: AtCoderサイトにアクセス

【図2-6：AtCoderトップページへのアクセス】

{% capture access_steps %}
1) ブラウザで `https://atcoder.jp/` を開く  
2) トップ右上の「新規登録」または「ログイン」をクリック  
3) 最新コンテスト情報や過去問にアクセス可能
{% endcapture %}
{% include panel.html type="steps" title="アクセス手順" content=access_steps %}

### Step 2-3: 新規登録とユーザー名設定

【図2-7：新規登録画面とユーザー名の考え方】

📝 新規登録フォーム
{% include panel.html type="steps" title="入力項目（例）" content="ユーザー名／メールアドレス／パスワード／パスワード確認／利用規約への同意" %}

💡 ユーザー名選択の重要ポイント

{% capture good_names %}
良いユーザー名の例  
• programming_taro（分かりやすい）  
• student2024（年度入り）  
• coder_hanako（趣味が伝わる）  
• algorithm_lover（興味の方向性）
{% endcapture %}
{% include panel.html type="steps" title="✅ 良いユーザー名の例" content=good_names %}

{% capture bad_names %}
避けるべきユーザー名  
• 本名フルネーム（プライバシー）  
• 学校名＋本名（個人特定リスク）  
• 生年月日を含む（セキュリティ）  
• 意味不明な文字列（覚えにくい）
{% endcapture %}
{% include panel.html type="warn" title="❌ 避けるべきユーザー名" content=bad_names %}

{% capture name_tips %}
ユーザー名選びのコツ  
• 将来の就活利用も想定  
• 覚えやすくタイプしやすい  
• 興味が伝わる表現  
• 5–15文字程度を目安
{% endcapture %}
{% include panel.html type="info" title="🎯 ユーザー名選択のコツ" content=name_tips %}

### Step 4-5: メールアドレスとパスワード設定

【図2-8：安全な設定のための注意点】

{% capture mail_settings %}
推奨メールサービス  
• Gmail（@gmail.com）  
• Yahoo!メール（@yahoo.co.jp）  
• Outlook（@outlook.com）

注意点  
• 長期間使うアドレスを選ぶ  
• 迷惑メール設定を確認  
• パスワード再設定に必要
{% endcapture %}
{% include panel.html type="info" title="📧 メールアドレス設定" content=mail_settings %}

{% capture pw_good %}
良いパスワードの条件  
• 8文字以上  
• 大小文字・数字・記号を含む  
• 辞書にない単語の組合せ  
例: MyAtCoder2024!
{% endcapture %}
{% include panel.html type="steps" title="🔐 安全なパスワード作成" content=pw_good %}

{% capture pw_bad %}
危険なパスワード  
• 誕生日や電話番号  
• 辞書にある単語のみ  
• 短すぎる（7文字以下）  
• 他サイトと共通
{% endcapture %}
{% include panel.html type="warn" title="❌ 避けるべきパスワード" content=pw_bad %}

### Step 6-7: 利用規約確認と登録完了

【図2-9：登録完了までの最終ステップ】

{% capture terms_points %}
主な内容  
• アカウントは1人1つまで  
• 不正行為の禁止  
• 迷惑行為の禁止  
• コンテスト中のルール遵守

中学生として特に注意  
• 保護者の同意が前提  
• 個人情報の取り扱いに注意  
• 健全な利用を心がける
{% endcapture %}
{% include panel.html type="info" title="📋 利用規約のポイント" content=terms_points %}

🎉 登録完了画面
{% include panel.html type="info" title="登録完了" content="認証メールを送信しました。メール内のリンクをクリックして認証を完了してください。" %}

**トラブルシューティング**

{% capture t1 %}
原因: 他の人が同じユーザー名を使用済み  
解決: 数字や記号を追加して変更  
例: coder_taro → coder_taro2024
{% endcapture %}
{% include panel.html type="warn" title="❌ 問題1: 「このユーザー名は使用済みです」" content=t1 %}

{% capture t2 %}
確認事項  
1. 迷惑メールフォルダをチェック  
2. メールアドレスの入力ミス確認  
3. 5–10分待ってから再確認  
4. 再送信ボタンを押す
{% endcapture %}
{% include panel.html type="steps" title="❌ 問題2: 認証メールが届かない" content=t2 %}

{% capture t3 %}
チェック項目  
• 8文字以上か  
• 大文字・小文字・数字を含むか  
• 確認用と一致しているか  
• 空白文字が入っていないか
{% endcapture %}
{% include panel.html type="steps" title="❌ 問題3: パスワードが通らない" content=t3 %}
{% include panel.html type="steps" title="パスワード確認チェック" content="8文字以上／大小英字・数字（＋記号推奨）／確認入力と一致／空白なし" %}

## 2.3 AtCoderの画面を探検しよう

アカウントが作成できたら、AtCoderの画面を詳しく見てみよう。最初は情報が多くて戸惑うかもしれないが、慣れればとても使いやすいサイトなんだ。

【図2-11：AtCoderメイン画面の構成】

{% capture top_blocks %}
上部バー: サイト名／検索／ユーザー名  
メニュー: ホーム／コンテスト／問題／ランキング  
カード例: 今後のコンテスト／自分の成績／おすすめ問題
{% endcapture %}
{% include panel.html type="info" title="メイン画面の見どころ" content=top_blocks %}

### ナビゲーションメニューの使い方

【図2-12：各メニューの役割と使い方】

{% capture menu_home %}
🏠 ホーム  
• 最新コンテスト／成績サマリー／おすすめ問題／お知らせ
{% endcapture %}
{% include panel.html type="steps" title="ホーム" content=menu_home %}

{% capture menu_contest %}
🏆 コンテスト  
• 今後の予定／過去回／結果・順位／問題一覧
{% endcapture %}
{% include panel.html type="steps" title="コンテスト" content=menu_contest %}

{% capture menu_tasks %}
📚 問題  
• 過去問検索／難易度別／分野別／提出状況
{% endcapture %}
{% include panel.html type="steps" title="問題" content=menu_tasks %}

{% capture menu_rank %}
👥 ランキング  
• 全体／国別／学校別／フレンド比較
{% endcapture %}
{% include panel.html type="steps" title="ランキング" content=menu_rank %}

### マイページの見方

【図2-13：マイページの重要な情報】

{% capture mypage %}
プロフィール／レーティング／最高レート／参加回数／最高順位  
レーティング推移グラフ／最近の提出 など
{% endcapture %}
{% include panel.html type="info" title="マイページの構成" content=mypage %}

{% capture words %}
AC: Accepted（正解）  
WA: Wrong Answer（不正解）  
TLE: Time Limit Exceeded（時間超過）
{% endcapture %}
{% include panel.html type="steps" title="用語説明" content=words %}

## 2.4 レーティングシステムを理解しよう

AtCoderの大きな特徴の一つが「レーティングシステム」だ。これは君の実力を数値で表すシステムで、継続的な成長を実感できる仕組みになっている。

![図2-14：AtCoderレーティングシステム]({{ site.baseurl }}/assets/diagrams/chapter2/figure2-14-rating-system.svg)

### レーティングの変動の仕組み

【図2-15：レーティング変動のメカニズム】

📊 コンテスト参加前
{% include panel.html type="info" title="レーティングの見方（例）" content="現在: 420（茶）／期待順位: 800位（同レベルの想定順位）" %}
         ↓ コンテスト参加
         
🏆 コンテスト結果による変動

ケース1: 期待より良い成績
{% include panel.html type="steps" title="ケース1: 実際順位が期待より良い" content="例: 実際600位（期待800位より上）→ レーティング上昇（420→450）" %}

ケース2: 期待通りの成績  
{% include panel.html type="info" title="ケース2: 実際順位が期待通り" content="例: 実際800位 → レーティング変動なし（420→420）" %}

ケース3: 期待より悪い成績
{% include panel.html type="warn" title="ケース3: 実際順位が期待より悪い" content="例: 実際1000位（期待800位より下）→ レーティング下降（420→390）" %}

💡 ポイント：
• 実力より上の成績 → レーティング上昇
• 実力通りの成績 → レーティング維持  
• 実力より下の成績 → レーティング下降

### 中学生の目標設定

【図2-16：中学生のための現実的なレーティング目標】

🎯 1年目の目標: 茶色達成 (400以上)
{% include panel.html type="steps" title="最初の6–12ヶ月（目安）" content="Python基本文法／ABC A問題の安定化／基本アルゴリズム。目安: 月1–2回参加／A正答率80%／Bに時々挑戦" %}

🎯 2年目の目標: 緑色達成 (800以上)  
{% include panel.html type="steps" title="2年目（目安）" content="データ構造の理解／ABC B安定／Cに挑戦。目安: A,Bをセットで解答／C正答率30%／解法の幅が拡大" %}

🎯 3年目の目標: 水色達成 (1200以上)
{% include panel.html type="steps" title="3年目（目安）" content="高度なアルゴリズムの習得／ABC C安定／Dに挑戦。目安: A,B,Cをセットで解答／JOI予選通過レベル" %}

## 2.5 コンテストってどんな感じ？

最後に、AtCoderのメインイベントである「コンテスト」について詳しく見てみよう。最初は緊張するかもしれないが、慣れればとても楽しい体験になるよ！

![図2-17：ABCの構成]({{ site.baseurl }}/assets/diagrams/chapter2/figure2-17-abc-structure.svg)

### コンテストの流れ

【図2-18：コンテスト当日のタイムライン】

{% capture pre_start %}
🕒 開始前（20:45–21:00）  
やること: 環境/回線確認・エディタ起動・ログイン・水分補給  
心の準備: 深呼吸／楽しむ気持ち／完璧より確実
{% endcapture %}
{% include panel.html type="steps" title="開始前" content=pre_start %}

{% capture start_now %}
🕘 開始直後（21:00–21:05）  
A問題: 問題文→サンプル確認→実装→提出  
提出前の最終チェックを忘れない
{% endcapture %}
{% include panel.html type="steps" title="開始直後" content=start_now %}

{% comment %}Removed legacy ASCII for 開始直後 (already panelized above){% endcomment %}

{% capture mid_phase %}
🕘 中盤（21:05–21:30）  
B問題に挑戦: 解けそうなものを優先／時間配分を意識／焦らない
{% endcapture %}
{% include panel.html type="steps" title="中盤" content=mid_phase %}

{% capture last_phase %}
🕘 終盤（21:30–22:40）  
見直しと追加挑戦: 提出の再確認／未解決に再挑戦／C問題は無理せず  
学習ノート: 解法メモ／未理解の洗い出し／次回の改善点
{% endcapture %}
{% include panel.html type="steps" title="終盤" content=last_phase %}

### 初回参加時の心構え

【図2-19：初回参加の心理的ハードルを下げるコツ】

{% capture anx %}
😰 よくある不安  
• 1問も解けなかったら恥ずかしい…  
• 他の人と比べてレベルが低すぎる…  
• 時間内に解き切れないプレッシャー…
{% endcapture %}
{% include panel.html type="warn" title="不安の正体" content=anx %}

{% capture reality %}
🤗 現実と対処  
• 多くの初心者はA問題を解ける／完璧を求めなくてOK  
• 同世代も最初は同じレベル／成長過程を楽しむ  
• 全問完答は上級者でも難しい／1問でも解けたら成功
{% endcapture %}
{% include panel.html type="info" title="現実と対処" content=reality %}

{% capture success_criteria %}
✅ A問題を1問でも解けた → 大成功  
✅ 問題文を理解できた → 良いスタート  
✅ 最後まで諦めない → 継続力の証明  
✅ 楽しめた → 最重要の成功
{% endcapture %}
{% include panel.html type="steps" title="初回参加の成功基準" content=success_criteria %}

**次回への準備**

【図2-20：コンテスト後の効果的な振り返り方法】

{% capture analyze %}
📊 結果分析（30分以内）  
記録: 解けた数/時間・詰まった点・学び・次回改善  
シート例: A=15分/○、B=未完→文字列処理を強化
{% endcapture %}
{% include panel.html type="steps" title="結果分析" content=analyze %}

{% capture editorial %}
📚 解説活用（翌日〜3日）  
• 解けた: 他解法も確認  
• 解けなかった: 解説理解＋類題で練習  
• 手が出なかった: 今は飛ばす  
実践: 写経→数値変更→類題練習
{% endcapture %}
{% include panel.html type="info" title="解説の使い方" content=editorial %}

## まとめ：AtCoderデビューの準備完了！

この章では、AtCoderの世界について詳しく学んだね。

【図2-21：この章で身につけたスキル】

{% capture achieved %}
達成: AtCoder理解／アカウント作成／サイトの使い方  
レーティング概要／コンテストの流れと心構え
{% endcapture %}
{% include panel.html type="steps" title="達成したこと" content=achieved %}

{% capture next_steps %}
次のステップ（第3章）  
• Pythonインストール  
• エディタ設定  
• 提出練習  
• デバッグ基礎
{% endcapture %}
{% include panel.html type="plan" title="次の章へ" content=next_steps %}

君はもうAtCoderの世界に足を踏み入れる準備ができた！アカウントを作成し、サイトの使い方を理解し、コンテストがどのようなものかも分かった。

最初は緊張するかもしれないが、AtCoderは初心者に優しいサイトだ。焦らず、自分のペースで楽しみながら成長していこう。

次の章では、実際にプログラムを書いて提出するための環境を整える方法を学ぶよ。いよいよ、君の競技プログラミングライフが本格的に始まる！
