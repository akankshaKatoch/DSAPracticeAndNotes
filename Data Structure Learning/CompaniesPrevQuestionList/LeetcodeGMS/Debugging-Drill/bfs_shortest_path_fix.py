from collections import deque

def shortest_path(n, edges, src, dst):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    q = deque([(src, 0)])
    visited = {src}
    while q:
        node, d = q.popleft()
        if node == dst:
            return d
        for nei in g[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, d+1))
    return -1
