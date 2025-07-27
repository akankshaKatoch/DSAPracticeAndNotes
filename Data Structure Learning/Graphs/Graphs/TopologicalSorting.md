# What is Topological Sort?

Topological Sort is a linear ordering of nodes in a **Directed Acyclic Graph (DAG)** such that for every directed edge `u → v`, node `u` comes before `v` in the ordering.

---

## Key Conditions

1. Only valid on **Directed** graphs  
2. Must be **Acyclic** (no cycles)

---

## Real-World Use Cases (Amazon-relevant)

| Use Case                  | Example                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| Task Scheduling           | Building tasks that depend on other tasks finishing (e.g., compiling a codebase) |
| Package Dependency Resolution | Installing libraries in the correct order                                 |
| CI/CD Pipelines           | Steps in deployment that depend on each other                            |
| Build Order               | Microservices with deployment dependencies                               |
| Course Scheduling         | Completing courses with prerequisites (LeetCode classic)                 |

---

## How to Implement Topological Sort

You can implement it using:

- **DFS-based approach (recursive)**
- **Kahn’s Algorithm (BFS-based using in-degrees)**

---

### ✍️ 1. DFS-Based Topological Sort (Recursive)

**Steps:**

1. Visit each unvisited node.
2. On each visit:
    - Mark node as "visiting"
    - Recursively visit all its neighbors
    - After all neighbors are processed, mark it "visited" and push to result stack
3. Reverse the result stack

```python
def topo_sort_dfs(graph):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    result.reverse()
    return result
```

---

### ✍️ 2. Kahn’s Algorithm (BFS using in-degree)

**Steps:**

1. Calculate in-degree (number of incoming edges) for all nodes.
2. Add all nodes with `in-degree == 0` to a queue.
3. While the queue is not empty:
    - Pop node → add to result
    - Reduce in-degree of neighbors
    - If in-degree of a neighbor becomes 0 → add to queue

```python
from collections import deque, defaultdict

def topo_sort_kahn(graph):
    indegree = defaultdict(int)
    result = []
    
    # Build in-degree
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])

    while queue:
        curr = queue.popleft()
        result.append(curr)

        for neighbor in graph[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return "Cycle Detected"
    
    return result
```

---

## ✅ Keywords to Spot

- “Given prerequisites”
- “Dependency resolution”
- “Task execution order”
- “Build order”
- “Cycle detection in directed graph”