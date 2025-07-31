# Claude Code 作業ガイドライン

このファイルは、Claude Codeが競技プログラミング書籍プロジェクトで作業する際の重要な情報とガイドラインをまとめたものです。

## プロジェクト概要

- **組織**: ITDO Inc.（株式会社アイティードゥ）
- **リポジトリ**: https://github.com/ootakazuhiko/competitive_programming_book.git
- **フォーマット**: book-formatter v3.0
- **執筆方針**: tech-book-writing-6phases.md に準拠

## 重要な前提条件

1. **GitHubプラン**: 有料プラン（Pro/Team/Enterprise）
2. **GitHub Pages**: プライベートリポジトリでも利用可能
3. **デプロイ方式**: 基本的に"Deploy from a branch"を使用
4. **言語**: 日本語の技術書

## 執筆フレームワーク

### 6フェーズ執筆プロセス
1. **フェーズ1**: 企画立案・価値設計 ✅ 完了
2. **フェーズ2**: 構造設計・目次詳細化 🚧 進行中
3. **フェーズ3**: 探索的執筆・内容検証
4. **フェーズ4**: 構造改善・方針確定
5. **フェーズ5**: 本格執筆・内容充実
6. **フェーズ6**: 品質保証・最終調整

### AI支援による執筆戦略
- **ラフ原稿**: Claude 4 Opus（深い分析と創造性）
- **本稿**: Claude 4 Sonnet（効率的な精緻化）
- **共通指針**: 概念と原理の文章説明を優先、コード例は最小限

## 作業時の注意事項

### 必ず確認すること
1. **tech-book-writing-6phases.md**の執筆方針に準拠
2. **book-config.json**の構造との整合性
3. **図解ガイドライン**（docs/diagram/）に従ったSVG作成

### してはいけないこと
- ❌ プライベートリポジトリを勝手にパブリックに変更
- ❌ 設定ファイルの無断変更
- ❌ コード中心の説明（概念・原理を重視）

## よく使うコマンド

```bash
# book-formatter更新
npm start update-book --config book-config.json

# 設定ファイル検証
npm start validate-config --config book-config.json

# GitHub Pages状態確認
gh api repos/ootakazuhiko/competitive_programming_book/pages --jq '{status, html_url, source}'
```

## 書籍の特徴

### 対象読者
- プログラミング基礎知識を持つ方（1年以上の経験）
- 競技プログラミング初学者〜中級者
- 就職・転職で技術力を証明したい方

### 差別化要素
- **実践重視**: 理論より実装パターンに重点
- **段階的学習**: レベル別の詳細ロードマップ
- **メンタルモデル**: 直感的な問題解決思考の構築
- **キャリア活用**: 実務・転職での活用戦略

## ファイル構成

```
competitive_programming_book/
├── BOOK-PROPOSAL.md          # 企画書
├── README.md                 # プロジェクト概要
├── CHANGELOG.md              # 変更履歴
├── book-config.json          # 書籍設定
├── tech-book-writing-6phases.md  # 執筆ガイドライン
├── docs/diagram/             # 図解ガイドライン
├── src/chapter-*/            # 各章コンテンツ
└── assets/                   # 静的リソース
```

## 成果指標（KPI）

### 技術的目標
- AtCoder茶色レーティング（800+）到達率: 30%
- ABC-C問題正答率: 50%以上
- 継続学習率（1年後）: 70%

### 品質指標
- 理解度テスト正答率: 80%以上
- NPS（推奨度）: 50以上
- エラー率: 1%以下

## 連絡先

- Email: knowledge@itdo.jp
- GitHub: @itdojp

---

最終更新: 2025-01-31