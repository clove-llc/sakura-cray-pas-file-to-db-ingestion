## 1. セットアップ手順

### 1.1 SQLite のインストール

```bash
sudo apt install sqlite3
```

---

### 1.2 データベースの作成

```bash
mkdir -p data/db
sqlite3 data/db/app.db < data/db/init.sql
```

data/db/app.db が作成されます。

---

### 1.3 Python 仮想環境の作成

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 1.4 依存ライブラリのインストール

```bash
pip install -r requirements.txt
```

---

## 2. 動作確認方法

### 2.1 ファイル変更監視を開始する

以下のコマンドでファイル監視を開始します。

```bash
python3 -m src.eventhandler
```

これにより、`data/incoming/analog_test/raw`フォルダと`data/incoming/instrument_analysis/raw`フォルダの監視が開始されます。

### 2.2 Excel読み込み > データベース保存までを行う

以下いずれかのディレクトリに、指定形式の Excel ファイルを配置してください。

- `data/incoming/analog_test/raw`
- `data/incoming/instrument_analysis/raw`

---

## 3. Excel ファイル形式（例）

| 列名          | 説明          |
| ------------- | ------------- |
| recipe_id     | レシピ識別子  |
| task_id       | 試験タスクID  |
| temperature_c | 試験温度（℃） |
| operator      | 実施者        |
| test_date     | 試験日        |

※ 現在はアナログ試験（`analog_test`）のみ実装済みです。

---

## 4. 処理結果

- Excel ファイルが検知されると自動で読み込まれます
- データは以下のデータベースに挿入されます

```text
data/db/app.db
```
