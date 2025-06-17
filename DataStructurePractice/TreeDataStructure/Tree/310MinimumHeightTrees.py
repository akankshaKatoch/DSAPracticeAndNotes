from collections import defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        adj_graph = defaultdict(set)

        for node in edges:
            adj_graph[node[0]].add(node[1])
            adj_graph[node[1]].add(node[0])
        print(adj_graph)

        # find all the nodes which have only 1 node
        leaves = [node for node in adj_graph if len(adj_graph[node])==1]

        while n >2:
            n -= len(leaves)
            newleave = []

            for leaf in leaves:
                neighbours = adj_graph[leaf].pop()
                adj_graph[neighbours].remove(leaf)

                if len(adj_graph[neighbours]) ==1:
                    newleave.append(neighbours)

            leaves = newleave
        return leaves
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
sol = Solution()
print(sol.findMinHeightTrees(n, edges))