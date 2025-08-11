---
title: .gitignoreに途中から追加
draft: false
tags:
  - git
aliases:
---
- .gitignoreに途中から追加しても、もともと追跡対象で合った場合はそのまま追跡されてしまう

```bash
git rm -r --cached .
```
- そのあとgit add, git commitすれば追跡がされなくなる
