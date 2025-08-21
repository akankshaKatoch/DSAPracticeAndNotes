from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], 
                     queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for nodes, value in zip(equations, values):
            graph[nodes[0]].append((nodes[1], value))
            graph[nodes[1]].append((nodes[0], 1/value))
        
        def dfs(curr, target, visited, product):
            if curr == target:
                return product
            visited.add(curr)
            for neighbor, value in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited, product*value)
                    if result != -1.0:
                        return result
            return -1.0


        print(graph)
        #return None
        divLis = []
        for start, end in queries:
            if start not in graph or end not in graph:
                divLis.append(-1)
            else:
                divLis.append(dfs(start, end, set(), 1.0))
                

        return divLis
        
        


sol = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(sol.calcEquation(equations, values, queries))

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
print(sol.calcEquation(equations, values, queries))