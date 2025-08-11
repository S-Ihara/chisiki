---
title: git stash
draft: false
tags:
  - git
aliases:
---
- ブランチで作業中にほかのブランチをちょっと見たいとき、でもコミットはしたくないときに使える
	- 変更をstash（退避）させておける
```bash
git stash 
git stash -u # --include-untrackedの略で新規作成ファイルも退避できる
```
- stashの確認
```bash
git stash list
```
- stashを元に戻す
```bash
git stash pop
git stash pop stash@{0} # リストから特定のstashを戻せる
```