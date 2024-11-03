---
title: Deep Q-Network
draft: false
tags:
  - 強化学習
  - Deep_Learning
aliases:
  - 深層Q学習
  - Deep Q Network
---

- [[Q-Learning|Q-学習]]をNNを使って行う手法
	- 行動価値関数をNNによってモデル化

- いくつかのdeep Learningポイントとして
	- 経験再生（Replay Buffer）
		- 得られた経験（trajectory）を順に学習データとして使うのではなくランダムにサンプリングしてNNに通す
	- 2つのNNによる行動価値関数のUpdate
		- $\phi$と$\bar{\phi}$により行動価値関数をモデル化し、TD誤差の学習のとき$\frac{1}{2}\mathbb{E}(R+\gamma \max_{a \prime} Q_{\bar{\phi}}(S \prime, a \prime) - Q_{\phi}(S,A))^2$
		  とターゲットに使う行動価値関数のNNと最適化対象のNNを別のパラメータでモデル化
			- 定期的なステップ数で$\bar{\phi} \leftarrow \phi$とupdateする