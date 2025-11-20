from collections import deque, defaultdict
from typing import Dict, List, Tuple

def bfs(residual: Dict[int, Dict[int, int]], s: int, t: int, parent: Dict[int, int]) -> int:
    for v in residual:
        parent[v] = -1
    queue = deque()
    queue.append(s)
    parent[s] = -2  
    path_cap = {s: float('inf')}
    while queue:
        u = queue.popleft()
        for v, cap in residual[u].items():
            if cap > 0 and parent.get(v, -1) == -1:
                parent[v] = u
                path_cap[v] = min(path_cap[u], cap)
                if v == t:
                    return path_cap[t]
                queue.append(v)
    return 0

def edmonds_karp(n_nodes: int, edges: List[Tuple[int,int,int]], s: int, t: int) -> Tuple[int, Dict[int, Dict[int, int]]]:
    residual = {i: defaultdict(int) for i in range(n_nodes)}
    for u, v, cap in edges:
        residual[u][v] += cap 
        _ = residual[v]  

    max_flow = 0
    parent = {i: -1 for i in range(n_nodes)}
    while True:
        bottleneck = bfs(residual, s, t, parent)
        if bottleneck == 0:
            break 
        v = t
        path_nodes = []
        while v != s:
            u = parent[v]
            path_nodes.append((u, v))
            residual[u][v] -= bottleneck
            residual[v][u] += bottleneck
            v = u
        max_flow += bottleneck
        print(f"Augmented by {bottleneck} along path: {list(reversed(path_nodes))}")
    return max_flow, residual

if __name__ == "__main__":
    edges = [
        (0,1,16), (0,2,13),
        (1,2,10), (1,3,12),
        (2,1,4),  (2,4,14),
        (3,2,9),  (3,5,20),
        (4,3,7),  (4,5,4)
    ]
    n = 6
    source = 0
    sink = 5
    maxflow, residual = edmonds_karp(n, edges, source, sink)
    print("\nMax flow:", maxflow)

    print("\nFinal residual graph (non-zero capacities):")
    for u in range(n):
        for v, cap in residual[u].items():
            if cap != 0:
                print(f"{u} -> {v} : {cap}")
