from collections import deque, defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build the graph and compute indegrees
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        print(graph, "   ", indegree)

        # Initialize queue with courses having no prerequisites (indegree 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        complete = 0
        while queue:
            course = queue.popleft()
            complete += 1

            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return complete == numCourses


    # Learning points or points to keep in mind:
    # When considering incoming nodes, follow Kahn's algorithm.
    # 
    # Steps:
    # 1. Create a dictionary (graph) where each node points to its neighbors.
    # 2. Create an indegree list to count the number of incoming edges for each node.
    #    The starting node(s) will have an indegree of 0.
    # 3. Push all nodes with indegree 0 into a queue. These are the possible starting nodes.
    # 4. While the queue is not empty:
    #    a. Pop a node from the queue.
    #    b. For each neighbor of this node, decrement its indegree by 1.
    #    c. If a neighbor's indegree becomes 0, add it to the queue.
    # 5. Keep a count of the number of nodes processed.
    # 6. At the end, if the count of processed nodes equals the total number of courses (nodes),
    #    it means all courses can be finished (no cycle exists).
    # Otherwise, if not all nodes are processed, there is a cycle and not all courses can be finished.


numCourses = 2
prerequisites = [[1,0]]

sol = Solution()
print(sol.canFinish(numCourses, prerequisites))
        