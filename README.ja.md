<div align="center">
<p><a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <b>日本語</b></p>
<img src="assets/logo.svg" alt="Ludo Atlas logo" width="150">
<h1>Ludo Atlas · ゲーム開発全景ハンドブック</h1>
<p><strong>中国語を優先し、体系的に整理した、オープンソースのゲーム開発ナレッジベース。</strong>学習・失敗回避・法務・リリースから、設計・技術・アート・制作・運営・AI ワークフローまで：「ゲームを作る」を <strong>139 本のドキュメント（約 98.2 万字）</strong>に分解。外部リンクは一本ずつ確認し、継続的なコントリビュートを前提に設計しています。</p>
<p><strong>📖 オンラインで読む：<a href="https://huanmoovo.github.io/ludo-atlas/">https://huanmoovo.github.io/ludo-atlas/</a>（简体中文 / English / 日本語 切り替え対応 · GitHub Pages、CI で自動デプロイ）</strong></p>
<p><a href="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/lint.yml"><img src="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/lint.yml/badge.svg" alt="Lint"></a> <a href="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/links.yml"><img src="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/links.yml/badge.svg" alt="Link Check"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY--SA%204.0%20%2B%20MIT-blue.svg" alt="License: CC BY-SA 4.0 + MIT"></a> <a href="https://github.com/HuanMoovo/ludo-atlas/stargazers"><img src="https://img.shields.io/github/stars/HuanMoovo/ludo-atlas?style=flat&label=Stars&color=48D64F" alt="Stars"></a></p>
</div>

## はじめに

ゲーム開発に関する中国語の資料は、昔から不足していません。チュートリアル、動画、ブックリスト、リンク集——一度検索すれば何百件も出てきます。足りないのは、それらを整理する骨組みと、「ゲームを作りたい」から「リリースする」までの一本の完全なルートです。

このリポジトリは、その骨組みを補うために作られました。4つの長期的な問題に向き合います：

- **学習に順序がない**：初心者に足りないのは単発のチュートリアルではなく、順番と「どこまでできれば次に進めるか」という基準です。入門エリアと学習パスは目標別に3つのルートを提示し、各ステップにクリア基準を明記しています。
- **制作工程の資料が乏しい**：中国語コンテンツの多くはコードと画面で止まっており、企画立ち上げ、スコープ管理、プレイテスト、ローカライズ、リリース、コンプライアンス、運営——プロジェクトを完遂できるかを本当に左右する工程の、体系的な公開資料はほとんどありません。リポジトリは「パイプラインとワークフロー」「リリースと商業化」「実践ハンドブック」の3ブロックで補い、各工程の最小チェックリストを提供します。
- **資料は古くなる**：エンジンのバージョン、プラットフォームポリシー、料金、コンプライアンス要件は毎年変わります。ブログや動画は数世代遅れがちです。リポジトリはポリシー系コンテンツに確認時点を明記し、外部リンクを一本ずつ検証し、CI による継続的な再確認を行います。
- **AI 時代にはまだ標準解がない**：コーディングエージェントや生成アート・オーディオは実際のプロジェクトに入り始めています。AI ワークフローの章では、再利用可能なワークフロー、ツールマトリクス、コンプライアンスの境界をまとめ、プロジェクト規模に応じて使えるようにしています。

名前はラテン語の ludo（私は遊ぶ）と atlas（地図帳）に由来します。「ゲームを作る」ための、できる限り完全な地図を描くためです。構成原則はただ一つ：実際の開発順に知識を配置すること。コンテンツは中国語優先で、各ドキュメントは具体的な問い一つに答え、相互参照し重複しません。

これは継続的にメンテナンスされるオープンソースプロジェクトで、誤りは避けられません。Issue や PR での修正・追加を歓迎します。誤りの修正を最優先とします。

魔法が使えないなら、ホグワーツに修行に行くしかないですね。

## これは何か

ゲーム開発の全工程をカバーする、中国語のオープンソースハンドブック集です：

- **「どう作るか」と「なぜそうするか」を明確に**——空論は書きません。数値・ポリシー・料金には検証可能な出典と確認時点を添えます。
- **外部リンクを一本ずつ検証**（公開前に全数チェック＋CI が毎週自動で再確認）。リンク切れには対処の仕組みがあります。
- **構造を科学的に設計**：139 本のドキュメントがそれぞれ役割を持ち、重複せず相互参照。構成と長期計画は[設計ドキュメント](docs/meta/design.md)をご覧ください。

コンテンツは中国語中心で、英語版をセクション単位で順次追加しています（まず本 README、サイトのホーム、はじめに）。

## コンテンツマップ

### 基礎分野（docs/fundamentals/）

| ハンドブック | 内容 |
| --- | --- |
| [ゲームデザインハンドブック](docs/fundamentals/game-design/README.md) | プロセス、コアループ、システム、数値、手触り、UX、ナラティブ |
| [技術実装ハンドブック](docs/fundamentals/programming/README.md) | アーキテクチャ選定、コアシステム、パフォーマンス、マルチプラットフォーム、ネットワーク、インフラ |
| [アート＆オーディオハンドブック](docs/fundamentals/art-audio/README.md) | アートバイブル、2D/3D、UI、テクニカルアート、オーディオ設計と納品 |
| [制作管理ハンドブック](docs/fundamentals/production/README.md) | 立ち上げ、見積り、フェーズモデル、スコープ管理、QA、振り返り |
| [レベルデザインハンドブック](docs/fundamentals/level-design/README.md) | メトリクス、誘導、テンポ、ホワイトボックス、定番10作の分解 |
| [エンジンソース読解ロードマップ](docs/fundamentals/engine-internals/README.md) | Godot / Bevy / 小型エンジン、方法論と週次プラン |
| [レンダラ自作ロードマップ](docs/fundamentals/graphics/README.md) | ソフトウェアラスタライザ → リアルタイムAPI → レイトレーシング |

### リスクと法務

| [失敗回避大全](docs/pitfalls/README.md) | 頻出の落とし穴（分野別・重要度別） |
| [法務・特許・競合ハンドブック](docs/publishing/legal/README.md) | 著作権、商標、特許、契約、越境コンプライアンス、競合分析 |

### リリースとプラットフォーム（docs/publishing/）

- [全プラットフォーム配信ハンドブック（オンラインゲーム特化を含む）](playbooks/platform-launch/README.md)
- [運営とグロースハンドブック](docs/publishing/live-ops/README.md)
- [ミニゲーム開発ハンドブック](docs/publishing/minigame/README.md)（WeChat / 抖音 / ハードウェアチャネル）
- [コンソール開発ハンドブック](docs/publishing/console/README.md)（ID@Xbox / PlayStation / Nintendo）
- [VR/AR 開発ハンドブック](docs/publishing/xr/README.md)
- [eスポーツと競技デザインハンドブック](docs/publishing/esports/README.md)

### パイプラインと深掘り（docs/pipelines/）

- [ModとUGCハンドブック](docs/pipelines/modding/README.md)
- [マルチプレイヤー＆バックエンド詳説](docs/pipelines/multiplayer-backend/README.md)

### AI とケーススタディ

- [AI ワークフロー](docs/ai/README.md)：コーディングエージェント、エンジン MCP、アート＆オーディオパイプライン、8つのエンドツーエンドワークフロー、コンプライアンスの境界線
- [ケーススタディ集](docs/postmortems/README.md)：公開事例24本を4段構成で分解

### 歴史と人物（docs/meta/）

- [ゲーム史](docs/meta/history/README.md)
- [インディー開発者と企業](docs/meta/people/README.md)
- [インディー開発者名鑑](docs/meta/people/indie/README.md)（44組のプロフィール）
- [設計ドキュメント](docs/meta/design.md)：リポジトリの設計と改訂記録

### 実戦とリソース

- [インディー生存ハンドブック](playbooks/indie-survival/README.md)
- [ゲーム開発リソース大全](resources/README.md)（リンク521本）
- [OSS厳選と書籍ガイド](resources/books-and-repos.md)（GitHubプロジェクト103件＋書籍60冊以上）

## おすすめの学習ルート3つ

- **ゼロから始める**：[リソース大全](resources/README.md) → [ゲームデザインハンドブック](docs/fundamentals/game-design/README.md) → [技術実装ハンドブック](docs/fundamentals/programming/README.md) → [AI ワークフロー](docs/ai/README.md)
- **はじめての一本を作る**：[一枚企画書](templates/gdd-mini.md) → [制作管理ハンドブック](docs/fundamentals/production/README.md) → [失敗回避大全](docs/pitfalls/README.md) → [インディー生存ハンドブック](playbooks/indie-survival/README.md) → [全プラットフォーム配信](playbooks/platform-launch/README.md)
- **さらに深く**：[エンジンソース読解ロードマップ](docs/fundamentals/engine-internals/README.md) → [レンダラ自作ロードマップ](docs/fundamentals/graphics/README.md) → [マルチプレイヤー＆バックエンド](docs/pipelines/multiplayer-backend/README.md)

## リポジトリ構成

```text
docs/           ハンドブック本文（テーマ別）
catalog/        機械可読エントリ（YAML + schema、単一の情報源）
resources/      リンクディレクトリと書籍リスト
playbooks/      エンドツーエンド実践（リリース、生存）
templates/      再利用テンプレート（企画書、振り返り）
scripts/        ツールスクリプト（リンク検証）
```

## リンクとファクトチェック

- 公開前に全外部リンクを一本ずつ検証し、CI が毎週再確認します。
- ポリシー・料金・プラットフォーム規則などの内容には確認時点を明記しています。行動の際は必ず公式の最新情報を確認してください。

## コントリビュート

誤りの指摘、新しいコンテンツ、エンジニアリング改善を歓迎します。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)をご覧ください。

## Star 推移

[![Star History Chart](https://api.star-history.com/svg?repos=huanmoovo%2Fludo-atlas&type=Date)](https://star-history.com/#HuanMoovo/ludo-atlas&Date)

## ライセンス

ドキュメントは [CC BY-SA 4.0](LICENSE)、コードは [MIT](LICENSE-CODE)。

## 補足

ハンドブックの内容は多数の公開資料、プラットフォーム公式ドキュメント、開発者インタビューを参考にしており、著作権は各作者に帰属します。数値とポリシーは行動時点の公式最新情報に従ってください。
