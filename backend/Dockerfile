# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY app/ /app/
COPY app/requirements.txt /app/

# 必要なライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# PYTHONPATH を設定してモジュール検索パスを追加
ENV PYTHONPATH=/app

# 初期化スクリプトを実行してからアプリケーションを起動
CMD ["sh", "-c", "python utils/init_db.py && uvicorn main:app --host 0.0.0.0 --port 8011"]


