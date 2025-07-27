from typing import List
from collections import deque
class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        adj_lst = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] ==1 and i!=j:
                    adj_lst[i].append(j)
        print(adj_lst)

        que = deque()
        provinces = 0

        for city in range(n):
            if not visited[city]:
                provinces += 1
                que = deque([city])
                visited[city] = True

                while que:
                    curr = que.popleft()
                    for neighbours in adj_lst[curr]:
                        if not visited[neighbours]:
                            visited[neighbours] = True
                            que.append(neighbours)
        return provinces
            



isConnected = [[1,1,0],[1,1,0],[0,0,1]]
sl = Solution()
print(sl.findCircleNum(isConnected))

""" 0 -> 1 -> 2
[[1,1,0],
 [1,1,1],
 [0,1,1]]

 AdjLst = [[1], [0,2], [1]]

 queue = [1]
 visted[True, ] or visted.append(0)

 while queue:
 cuur = queue.popleft()  # curr 1 we will check visited true and push 02 in queu 
 
 visted[curr] = true or visted 1 and append in queue. Now my visited =  [0, 1] 0r [t, t] queue = [0,2] 

 2nd iteration:
  pop.left 






 

 location where i == j ignore. 
 if ji = ij they are connected directly. 

 if 

"""