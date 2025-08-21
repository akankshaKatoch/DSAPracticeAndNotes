from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        stack = [0]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for keys in rooms[current]:
                    if keys not in visited:
                        stack.append(keys)
        return len(visited)==len(rooms)


sol = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))    
rooms = [[1],[2],[3],[]]
print(sol.canVisitAllRooms(rooms))  