
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a new node.
        # insert into 
        newnode = Node(node.val)
        visited = {node : newnode}
        stack = [(node, newnode)]

        while stack: 
            oldnode, currnode = stack.pop()

            for neighbor in oldnode.neighbors:

                if neighbor not in visited:
                    newcurrnode = Node(neighbor.val)
                    stack.append((neighbor, newcurrnode))
                    visited[neighbor] = newcurrnode
                newnode.neighbors.append[visited[neighbor]]
        return newnode

        


        return 

adjList = [[2,4],[1,3],[2,4],[1,3]]
sol = Solution()
print(sol.cloneGraph(adjList))