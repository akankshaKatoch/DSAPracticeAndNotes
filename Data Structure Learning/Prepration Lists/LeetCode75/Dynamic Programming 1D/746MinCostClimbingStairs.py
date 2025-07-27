from typing import List
class Solution:
    #recusrsive solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def mincost(i):
            if i>= len(cost):
                return 0
            return cost[i] + min(mincost(i+1), mincost(i+2))

        return min(mincost(0), mincost(1))
    
    #recusrsive solution
    def minCostClimbingStairsMemo(self, cost: List[int]) -> int:

        def mincost(i, memo = None):
            if memo == None:
                memo = {}
            if i in memo:
                return memo[i]
            if i>= len(cost):
                return 0
            memo[i] = cost[i] + min(mincost(i+1), mincost(i+2))
            return memo[i]

        return min(mincost(0), mincost(1))
    
    # Lets try with tabulation:

    def minCostClimbingStairstabu(self, cost: List[int]) -> int:

        table = [0]*(len(cost))

        #table[0] = 0
        table[0] = cost[0]
        table[1] = cost[1]
        #print(table)
        for i in range(2, len(table)):
            #print(min(cost[i-1], cost[i-2]))
            table[i] = cost[i]+ min(table[i-1], table[i-2])
            #print(table)
        return min(table[-1], table[-2])
    

    #more optimized solution:
    #using variable instead of list
     
    def minCostClimbingStairstabuOpti(self, cost: List[int]) -> int:

        if len(cost) == 2:
            return min(cost[0], cost[1])

        #table[0] = 0
        prev2step = cost[0]
        prev1step = cost[1]
        #print(table)
        for i in range(2, len(cost)):
            #print(min(cost[i-1], cost[i-2]))
            curr = cost[i]+ min(prev1step, prev2step)
            prev2step = prev1step
            prev1step = curr
        return min(prev1step, prev2step)

sol = Solution()

cost1 = [10,15,20]
print(sol.minCostClimbingStairs(cost1))    
print(sol.minCostClimbingStairsMemo(cost1))  
print(sol.minCostClimbingStairstabu(cost1))  
print(sol.minCostClimbingStairstabuOpti(cost1))  
cost2 = [1,100,1,1,1,100,1,1,100,1]      
print(sol.minCostClimbingStairs(cost2))   
print(sol.minCostClimbingStairsMemo(cost2)) 
print(sol.minCostClimbingStairstabu(cost2))  
print(sol.minCostClimbingStairstabuOpti(cost2))  