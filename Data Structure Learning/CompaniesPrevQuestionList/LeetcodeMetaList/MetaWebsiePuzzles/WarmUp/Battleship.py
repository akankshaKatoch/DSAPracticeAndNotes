from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  totalCount = R*C
  onesCount = 0
  for i in range(R):
    for j in range(C):
      print(i,",", j)
      if G[i][j] == 1:
        print(i,",", j)
        onesCount += 1
     
  print(onesCount, totalCount)
  return onesCount/totalCount


R = 2
C = 3
G = [[0, 0, 0],[0, 0, 0]]
print(getHitProbability(R, C, G))