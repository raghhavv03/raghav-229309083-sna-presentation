# raghav-229309083-sna-presentation
# Edmonds–Karp Algorithm (Maximum Flow)

This repository contains a clean and fully documented Python implementation of the **Edmonds–Karp algorithm**, which is a BFS-based variant of the Ford–Fulkerson method used to compute the **maximum flow** in a directed graph.

---

## 📘 Overview

The **Edmonds–Karp algorithm** finds the maximum flow between a source node `s` and a sink node `t` by:

1. Constructing a **residual graph**
2. Repeatedly running **Breadth-First Search (BFS)** to find the shortest augmenting path
3. Augmenting flow along that path
4. Updating residual capacities until no augmenting path exists

This guarantees a polynomial runtime of **O(V × E²)**.

---


