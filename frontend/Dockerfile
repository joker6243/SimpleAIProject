# ベースイメージ
FROM node:18

# 作業ディレクトリを設定
WORKDIR /app

# package.json と package-lock.json を先にコピー
COPY package*.json /app/

# 依存関係をインストール
RUN npm install

# ソースコードとその他の必要ファイルをコピー
COPY . /app/

# コンテナの公開ポートを設定
EXPOSE 3000

# 開発用サーバーを起動
CMD ["npm", "start"]
