---
title: Q-学習
draft: false
tags: 
aliases:
  - Q-学習
  - Q学習
---
- [[行動価値]]を$Q(S_t, A_t) \leftarrow (1-\alpha) Q(S_t,A_t) + \alpha(R_{t+1} + \gamma \max_{a \prime}Q(S_{t+1}, a \prime))$ によって更新する学習方法
	- $\alpha$は学習率
- 式変形すると$Q(S_t, A_t) \leftarrow Q(S_t,A_t) + \alpha(R_{t+1} + \gamma \max_{a \prime}Q(S_{t+1}, a \prime) - Q(S_t,A_t))$
	- 実装上はこっちを使うことが多いかな