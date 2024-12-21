---
title: docker tips
draft: false
tags:
  - linux
aliases:
---
- docker container 全削除
	```bash
	docker rm -f `docker ps -a -q` # 動いていても全部消す
	docker rm `docker ps -a -q` # forceオプション外すと動いているものは消えない
	```
	- きれいな方がいいよね
- docker cache 全削除
	```bash
	docker image prune # 使ってないimage全削除
	docker rmi $(docker images -q) # image 全削除 (使ってるやつは残るかも？)
	docker system prune # 使ってないimage container networkを全削除
	docker system prune -f # 確認のyを押す奴が出てこない
	docker builder prune -f # ビルドキャッシュ削除
	```
	- yオプションはないのでyを打ちましょう
- docker が使っている容量確認
	```bash
	docker system df
	```
	
