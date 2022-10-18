#!/usr/bin/env sh

# エラー時は停止
set -e

# ビルド出力ディレクトリに移動
cd build

# カスタムドメインにデプロイする場合
# echo 'www.example.com' > CNAME

git init
git checkout -B main
git add -A
git commit -m 'deploy'

# https://<USERNAME>.github.io にデプロイする場合
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git main

git push -f git@github.com:oha-Ohashi/spring-keeb-search.git main:gh-pages

cd -