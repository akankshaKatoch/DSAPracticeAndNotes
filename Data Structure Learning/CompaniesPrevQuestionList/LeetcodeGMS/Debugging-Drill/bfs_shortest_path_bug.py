from collections import deque

def shortest_path(n, edges, src, dst):
    """Unweighted shortest path length using BFS; nodes 0..n-1.
    Bug(s):
    - Marks visited when popping (late), causing duplicates and possible blow-up.
    - Returns wrong default when no path.
    """
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    q = deque([(src, 0)])
    visited = set()
    while q:
        node, d = q.popleft()
        if node in visited:          # too late
            continue
        if node == dst:
            return d
        visited.add(node)
        for nei in g[node]:
            q.append((nei, d+1))     # neighbors enqueued multiple times
    return 0                          # BUG: should be -1 if unreachable
