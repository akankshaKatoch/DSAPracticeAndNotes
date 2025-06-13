from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []
        
        def dfs(node, path):
            if node == target:
                result.append(path.copy())  # Add a copy to avoid reference issues
                return
            
            for neighbor in graph[node]:
                path.append(neighbor)      # Move forward
                dfs(neighbor, path)       # Explore
                path.pop()                 # Backtrack
        
        dfs(0, [0])  # Start from node 0 with initial path [0]
        return result


            





graph = [[4,3,1],[3,2,4],[3],[4],[]]
# o/p = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
sol = Solution()
print(sol.allPathsSourceTarget(graph))     