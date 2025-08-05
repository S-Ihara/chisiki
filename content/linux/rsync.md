---
title: rsyncメモ
draft: false
tags: linux
aliases: 
---
- ファイルのコピー（同期）をするコマンド
  - 通信込みの同期も可能
 
- オプション
  - `-v`: 表示

- 雑多に
- `--exclude="b.txt"`で除外ファイルを指定できる
  - 複数の場合は`--exclude={"a.txt", "b.txt"}`
- テキストファイルでの指定もできるらしい
  - `--exclude-from=ignore_list.txt
