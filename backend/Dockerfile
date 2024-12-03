# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY app/ /app/
COPY app/requirements.txt /app/

# 必要なライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのエントリーポイント
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8011"]
