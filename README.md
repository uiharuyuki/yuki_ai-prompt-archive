# AI Prompt Gallery (DaysAI / nanobanana)

画像生成AIのプロンプトを管理・閲覧できるWebアプリケーション（Django製）

## 概要

このプロジェクトは、DaysAI や nanobanana などの画像生成AIで使用したプロンプトを保存し、ギャラリー形式で閲覧できるWebアプリケーションです。投稿した画像に対してコメントを追加することも可能です。

## 注意事項

- **画像ファイルは含まれていません**: リポジトリの軽量化のため、`media/` フォルダ内の画像ファイルはGitHubに含まれていません。
- **データベースファイルは除外されています**: セキュリティ上の理由から、`db.sqlite3` はリポジトリに含まれていません。

## 機能

- 画像生成AIのプロンプト管理
- 生成画像のギャラリー表示
- 投稿へのコメント機能
- 管理画面での投稿管理

## インストール手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/yourusername/yuki_ai-prompt-archive.git
cd yuki_ai-prompt-archive
```

### 2. 仮想環境の作成と有効化

```bash
python -m venv .venv

# Windows の場合
.venv\Scripts\activate

# macOS / Linux の場合
source .venv/bin/activate
```

### 3. 依存ライブラリのインストール

```bash
pip install -r requirements.txt
```

### 4. データベースのマイグレーション

```bash
python manage.py migrate
```

### 5. サンプルデータのロード（オプション）

```bash
python manage.py loaddata gallery/fixtures/initial_data.json
```

### 6. 管理ユーザーの作成

管理画面にアクセスするには、スーパーユーザーの作成が必要です。

```bash
python manage.py createsuperuser
```

### 7. 開発サーバーの起動

```bash
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000/` にアクセスしてください。

## 使用技術

- Python 3.x
- Django 6.0
- SQLite3
- Pillow（画像処理）

## ディレクトリ構造

```
yuki_ai-prompt-archive/
├── gallery/              # メインアプリケーション
│   ├── fixtures/         # サンプルデータ
│   ├── models.py         # データモデル（Post, Comment）
│   ├── views.py          # ビュー
│   └── templates/        # HTMLテンプレート
├── media/                # アップロード画像（Git管理外）
├── db.sqlite3            # データベース（Git管理外）
├── manage.py             # Django管理スクリプト
└── requirements.txt      # 依存ライブラリ
```

## ライセンス

このプロジェクトは個人用プロジェクトです。

## 作成者

Yuki

## 使用ツール

Gemini 3.0 pro（企画書作成＆Claudeへの指示プロンプト作成）
Claude Code（MVP！）

## 制作時間

3時間