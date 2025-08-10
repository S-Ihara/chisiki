---
title: ssh鍵を作るときのやつ
draft: false
tags: linux
aliases:
---
- ssh_keygen

```bash
ssh-keygen -t ed25519
ssh-keygen -t ed25519 -f "$HOME/.ssh/github-sihara"
```
- オプション
  - t: 鍵のアルゴリズムの指定とかだったはず、今はed25519か丸い
  - C: コメントがつけられる`-C "mofu"`
  - f: ファイル名の指定、パスの指定がめんどくさい
