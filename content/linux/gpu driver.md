---
title: gpu nvidia-driver 周り
draft: false
tags:
  - linux
aliases:
---
### 確認
既存のものが残っているときの確認とか
- (使用可能な)driverが入っているか
    - `nvidia-smi`
    - 普通に動けばnvidia-driverが入っている
    - バージョン確認もできる
- ubuntuがgpuを認識しているか
	- `lspci | grep -i nvidia`
	- driverが入っていなくてもgpuが繋がっていれば出てくる…はず

### 既存のdirverを消す
```bash
sudo apt-get purge nvidia* 
sudo apt-get purge cuda*
```
- docker使っている人はnvidia-docker2とかnvidia-container-toolkitも一緒に消えるの注意

### driver install
- aptで入れるときはリポジトリを追加する必要がある
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa 
sudo apt update
```
- 対応しているdriverの確認
```bash
ubuntu-drivers devices
```
- あとは普通にaptでinstallできる