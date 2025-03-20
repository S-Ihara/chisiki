---
title: Union-Find木
draft: false
tags:
  - kyopuro
aliases:
---
- あるいはDSU; Disjoint Set Unionなどとも呼ぶ
- グループ分けを管理するデータ構造
	- 併合はできるが分割はできないことに注意
- 次の操作が効率的に行える
	- 要素a,bが同じグループに属しているかを調べる
	- 要素aと要素bのグループを併合する
- 操作は$O(\alpha(n))$であることが知られている
	- ただし、ならし計算量


### 実装
```rust
pub struct UnionFind {
    parent: Vec<usize>, // parent[i] = parent of i or itself if i is a root
    rank: Vec<usize>, // rank[i] = approximate depth of the tree if i is a root
    size: Vec<usize>, // size[i] = number of elements in the set if i is a root
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        UnionFind {
            parent: (0..n).collect(),  // Each element is its own parent initially
            rank: vec![0; n],          // Initial rank of 0 for all elements
            size: vec![1; n],          // Each set starts with size 1
        }
    }
    
    /// Find the root of the set containing x (with path compression)
    pub fn find(&mut self, x: usize) -> usize {
        if self.parent[x] == x {
            x  // x is the root
        } else {
            // Path compression: set parent to the root
            self.parent[x] = self.find(self.parent[x]);
            self.parent[x]
        }
    }
    
    /// Union the sets containing x and y (with rank optimization)
    pub fn union(&mut self, x: usize, y: usize) -> bool {
        let root_x = self.find(x);
        let root_y = self.find(y);
        
        // Already in the same set
        if root_x == root_y {
            return false;
        }
        
        // Union by rank: attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y] {
            self.parent[root_x] = root_y;
            self.size[root_y] += self.size[root_x];
        } else {
            self.parent[root_y] = root_x;
            self.size[root_x] += self.size[root_y];
            
            // If ranks are same, increment the rank of root_x
            if self.rank[root_x] == self.rank[root_y] {
                self.rank[root_x] += 1;
            }
        }
        true
    }

    /// Check if x and y are in the same set
    pub fn same(&mut self, x: usize, y: usize) -> bool {
        self.find(x) == self.find(y)
    }
    
    /// Get the size of the set containing x
    pub fn size(&mut self, x: usize) -> usize {
        let root = self.find(x);
        self.size[root]
    }
}
```


- Reference
	- 忘れた