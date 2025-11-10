---
title: pipのbreak  system packageの回避
draft: false
tags: 
  - python
aliases:
---
- ubuntu24からデフォルトで入っているpythonにpipでパッケージをインストールしようとすると怒られるようになった
- メッセージの通り --break-system-packages を付けると回避できるが面倒くさい

### 回避方法
- いくつかあるが環境変数を使うのが多分一番手っ取り早い
- `export PIP_BREAK_SYSTEM_PACKAGES=1` するとエラーが出なくなる