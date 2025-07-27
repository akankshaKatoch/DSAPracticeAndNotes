from collections import deque, defaultdict

def kahn_topo_sort(graph):
    indegre = defaultdict(int)
    result = []

    for node in graph:
        for neighbor in graph[node]:
            indegre[neighbor] += 1

    queue = deque([node for node in graph if indegre[node]==0])

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            indegre[neighbor] -=1
            if indegre[neighbor] == 0:
                queue.append(neighbor)
    
    if len(graph) != len(result):
        return "cycle"
    
    return result 


"""
A → C  
B → C  
C → D  
"""






#graph representation of this is

graph = { 'A' : ['C'], 'B' : ['C'], 'C': ['D'], 'D': []}
"""
 Indegree of each node is
 A : 0
 B : 0
 C : 2 (from A and B)
 D : 1
 """

print(kahn_topo_sort(graph))