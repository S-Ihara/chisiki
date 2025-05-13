---
title: SSH鍵のフィンガープリントの確認方法
draft: true
tags: [linux, ssh]
aliases:
---
- ssh鍵のfingerprintを確認したいことがある？
- 確認方法
    ```bash
    ssh-keygen -l -f ~/.ssh/id_rsa
    ssh-keygen -l -f ~/.ssh/id_rsa -E md5
    ssh-keygen -l -f ~/.ssh/id_rsa -E md5 -t ed25519
    ```
    - l がshow fingerprint オプション
    - fはファイルネーム
    - eでハッシュ関数の指定
    - tで暗号アルゴリズムの指定（何も指定しなくても勝手にやってくれる）
