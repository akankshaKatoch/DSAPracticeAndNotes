from typing import List 

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # Intution I have to visit all nodes. I can have BFS or DFS. 
        # here lets got with DFS. 

        # we have some value at index 0 as it is only opened up I will add this on top 
        # of my stack. #stack will have keys which we have but not visited yet.
        stack = [0]
        visited = set([0])

        while stack:

            curr_room = stack.pop()
            keys = rooms[curr_room]
            
            for k in keys:
                if k not in visited:
                    #print(k)
                    stack.append(k)
                    visited.add(k)
        print(len(visited), len(rooms))
        return len(visited) == len(rooms)

sol = Solution()
rooms = [[1],[2],[3],[]]
print(sol.canVisitAllRooms(rooms))

rooms = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))

        