#!/bin/bash


git add .
# 英語の日付をコミットメッセージに追加
git commit -m "$(date '+%Y-%m-%d %H:%M:%S')"

git push origin main

