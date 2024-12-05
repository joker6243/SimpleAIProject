# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /workspace

# 必要なファイルをコピー
COPY ./app/ /workspace/app/  
COPY ./requirements.txt /workspace/

# 必要なライブラリをインストール
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# PYTHONPATH を設定してモジュール検索パスを追加
ENV PYTHONPATH=/workspace

# 初期化スクリプトを実行してからアプリケーションを起動
WORKDIR /workspace/app
CMD ["sh", "-c", "python utils/init_db.py && uvicorn main:app --host 0.0.0.0 --port 8011"]
