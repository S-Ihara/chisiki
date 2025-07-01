---
title: git管理下のファイルをrenameするとき
draft: false
tags: git
aliases: git mv
---
- git管理下にあるファイルをrenameすると、ファイルの全削除と新規ファイルの追加になる
  - これまでの変更記録などがすっとんでいく

### 対処法
- `git mv`を使う
```bash
git mv neko.txt nyaa.txt
```
