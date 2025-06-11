# Depth First Search (DFS)

DFS is a graph traversal algorithm that uses a **stack** (either explicitly or via recursion).

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

## DFS Traversal Steps

Start at node **a**.

| Step | Stack         | Current | Output | Action                                      |
|------|--------------|---------|--------|---------------------------------------------|
| 1    | c, b         | a       | a      | Print a, push c and b onto stack            |
| 2    | c            | b       | a, b   | Pop b, print b, push d onto stack           |
| 3    | c, d         | d       | a, b, d| Pop d, print d, push f onto stack           |
| 4    | c, f         | f       | a, b, d, f | Pop f, print f (no neighbors)           |
| 5    | c            | c       | a, b, d, f, c | Pop c, print c, push e onto stack     |
| 6    | e            | e       | a, b, d, f, c, e | Pop e, print e (no neighbors)      |

## DFS Order

The order of visiting nodes:  
**a → b → d → f → c → e**

## Notes

- DFS explores as far as possible along each branch before backtracking.
- The stack keeps track of the next node to visit.
- Can be implemented recursively or with an explicit stack.

## DFS Pseudocode

Here is the pseudocode for DFS using an explicit stack:

```
DFS(graph, start):
    create a stack S
    create a set visited
    push start onto S

    while S is not empty:
        node = S.pop()
        if node not in visited:
            visit(node)
            add node to visited
            for each neighbor in graph[node]:
                if neighbor not in visited:
                    push neighbor onto S
```

## How DFS Works

- **Start at the initial node** (e.g., 'a').
- **Visit the node** and mark it as visited.
- **Push all unvisited neighbors** onto the stack.
- **Pop the top node** from the stack and repeat the process.
- DFS goes deep into the graph, following one branch as far as possible before backtracking to explore other branches.
- The stack ensures you always return to the most recent branching point.

DFS is useful for:
- Finding paths in a maze or puzzle.
- Checking connectivity in a graph.
- Topological sorting and cycle detection in directed graphs.

## DFS in Python (Pseudocode)

```python
def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visit(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

## LeetCode Problems Solvable with DFS

- [Number of Islands (200)](https://leetcode.com/problems/number-of-islands/)
- [Clone Graph (133)](https://leetcode.com/problems/clone-graph/)
- [Word Search (79)](https://leetcode.com/problems/word-search/)
- [Pacific Atlantic Water Flow (417)](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [Course Schedule (207)](https://leetcode.com/problems/course-schedule/)
- [Surrounded Regions (130)](https://leetcode.com/problems/surrounded-regions/)

## DFS Recursive Pseudocode (Python)

```python
def dfs(graph, node, visited):
    if node not in visited:
        visit(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```