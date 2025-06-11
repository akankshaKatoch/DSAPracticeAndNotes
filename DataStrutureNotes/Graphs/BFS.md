# Breadth First Search (BFS)

BFS is a graph traversal algorithm that explores all neighbors of a node before moving to the next level. It uses a **Queue** (FIFO: First-In-First-Out).

## Example Graph

```
a ----> c
|       |
|       v
b       e
|
v
d ----> f
```

---

## BFS Traversal Steps

| Step | Queue         | Current | Output           | Action                                         |
|------|--------------|---------|------------------|------------------------------------------------|
| 1    | b, c         | a       | a                | Print a, enqueue b and c                       |
| 2    | c, d         | b       | a, b             | Dequeue b, print b, enqueue d                  |
| 3    | d, e         | c       | a, b, c          | Dequeue c, print c, enqueue e                  |
| 4    | e, f         | d       | a, b, c, d       | Dequeue d, print d, enqueue f                  |
| 5    | f            | e       | a, b, c, d, e    | Dequeue e, print e (no neighbors)              |
| 6    |              | f       | a, b, c, d, e, f | Dequeue f, print f (no neighbors)              |

**BFS Order:**  
`a → b → c → d → e → f`

---

## Notes

- BFS is ideal for finding the shortest path in unweighted graphs.
- It visits nodes level by level.
- Use a queue to keep track of nodes to visit next.
- Mark nodes as visited when enqueuing to avoid cycles.

---

## LeetCode Examples

- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

---

---

## Pseudocode

```python
def bfs(graph, start):
    visited = set()
    queue = []
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node)  # or process(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
```

---
## Recursive BFS Pseudocode

While BFS is typically implemented iteratively, a recursive approach is possible by passing the queue and visited set as arguments:

```python
def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    node = queue.pop(0)
    print(node)  # or process(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
    bfs_recursive(graph, queue, visited)

# Usage:
# visited = set([start])
# bfs_recursive(graph, [start], visited)
```