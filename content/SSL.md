---
title: SSL
draft: false
tags: 
aliases:
  - SSL
  - Secure Socket Layer
---
- Secure Socket Layer; SSL
- いわゆるHTTPS通信
- SSL証明書には
	- 所有者の情報
	- 暗号化通信に必要な鍵
	- 発行者の署名データ
- が含まれている
- 認証局が署名の確認を行っている
- ファイル形式
	- よく見るやつのみ
	- .pem：証明書または鍵のbase64保存形式
	- .key：pem鍵の保存形式　いわゆる秘密鍵ファイル
	- .cer .crt：linuxはcrt、windowsはcer
		- csrファイルが正しいかをSSL証明書会社が証明しているもの
		- サーバー証明書
		- cerはcsrとcrtの中間証明書、という仕組みになっているらしい
	- .csr：証明書署名リクエスト
		- 秘密鍵を基に作った公開鍵ファイルにコモンネームなどの情報を付加したもの