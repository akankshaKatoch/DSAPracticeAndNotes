from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()

        stack = [0]

        adjtmap  = defaultdict(list)
        edges = set()

        for a, b in connections:
            adjtmap[a].append(b)
            adjtmap[b].append(a)
            edges.add((a,b))
        print(adjtmap, edges)
        count = 0
        while stack:
            curr = stack.pop()
            visited.add(curr) 
            for node in adjtmap[curr]:
                    if node not in visited:
                        # check fro edges from curr to node and vice versa. 
                        stack.append(node)
                        edge = (curr, node)
                        if edge in edges:
                            count +=1
        return count

sol = Solution()

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(sol.minReorder(n, connections))

        