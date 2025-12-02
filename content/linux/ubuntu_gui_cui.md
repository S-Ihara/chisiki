---
title: UbuntuのGUIモードとCUIモードの切り替え
draft: false
tags:
  - linux
aliases:
---
- ubuntuのGUIモードとCUIモードは簡単に切り替えられる
	- ubuntu serversと言っているものはこのGUIモードがインストールされていないだけ？
	- Ubuntu DesktopでインストールしてもCUIモードで起動すればおそらく？Ubuntu serversと同じくらい軽い


```bash
# デフォルトを CUI に変更する場合
sudo systemctl set-default multi-user.target

# デフォルトを GUI に変更する場合
sudo systemctl set-default graphical.target
```