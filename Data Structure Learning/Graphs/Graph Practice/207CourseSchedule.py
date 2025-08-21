from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dep_graph = defaultdict(list)
        indegree = [0]*numCourses

        for course, prereqs in prerequisites:
            dep_graph[prereqs].append(course)
            indegree[course] += 1

        print(indegree)
        
        que = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        while que:
            currcor = que.popleft()
            taken += 1

            for v in dep_graph[currcor]:
                #print(v)
                indegree[v] -= 1
                if indegree[v] == 0:
                    que.append(v)
            #print(que)
        
        return taken == numCourses










sol = Solution()
numCourses = 6
prereq = [[1,0],[2,1],[4,2],[3,2],[5,4]]
print(sol.canFinish(numCourses, prereq))