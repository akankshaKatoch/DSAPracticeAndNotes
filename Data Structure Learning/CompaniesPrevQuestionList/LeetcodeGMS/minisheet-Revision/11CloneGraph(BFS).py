from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []

def cloneGraph(node: 'Node') -> 'Node':
    """LeetCode 133. O(V+E)."""
    if not node: return None
    clones = {node: Node(node.val)}
    q = deque([node])
    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei not in clones:
                clones[nei] = Node(nei.val)
                q.append(nei)
            clones[cur].neighbors.append(clones[nei])
    return clones[node]
