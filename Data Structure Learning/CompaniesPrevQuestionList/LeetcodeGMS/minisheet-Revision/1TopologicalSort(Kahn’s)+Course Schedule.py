#1) Topological Sort (Kahn’s) + Course Schedule
from collections import deque, defaultdict

def topo_order(n, edges):
    """Return topological order or [] if cycle. O(V+E)."""
    g = defaultdict(list)
    indeg = [0]*n
    for u,v in edges:
        g[u].append(v); indeg[v]+=1
    q = deque([i for i in range(n) if indeg[i]==0])
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for w in g[u]:
            indeg[w]-=1
            if indeg[w]==0: q.append(w)
    return order if len(order)==n else []

def can_finish(numCourses, prerequisites):
    """LeetCode 207. O(V+E)."""
    return len(topo_order(numCourses, prerequisites)) == numCourses
