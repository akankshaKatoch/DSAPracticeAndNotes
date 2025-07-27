from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        course_dict = defaultdict(list)
        indegree = [0]*numCourses

        for course, pre in prerequisites:
            course_dict[pre].append(course)
            indegree[course] += 1

        
        print(course_dict)
        print(indegree)
        path = []

        queue = deque([i for i in range(numCourses) if indegree[i]==0])
        print(queue)
        while queue:
            course = queue.popleft()
            path.append(course)

            for neighbours in course_dict[course]:
                indegree[neighbours] -=1
                if indegree[neighbours] ==0:
                    queue.append(neighbours)
                    
            

        return path if len(course_dict) == len(path) else [] 



        




numCourses = 4

prerequisites = [[1,0],[2,0],[3,1],[3,2]]

sol = Solution()
print(sol.findOrder(numCourses, prerequisites))
"""
dict  = {
    0 : [1, 2]
    1 : [3]
    2 : [3]
    3 : []
}

indegree [0, 1, 1, 2]"""