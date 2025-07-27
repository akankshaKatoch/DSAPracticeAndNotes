from typing import List

class Solution:
    def coinChangeRecusion(self, amount: int,coins: List[int]) -> int:
        if amount == 0: return 0
        
        if amount<0: return -1
        minCoin = float('inf')
        for coin in coins:
            remainder = amount - coin
            res = self.coinChangeRecusion(remainder,coins)
            if res>=0:

                minCoin = min(minCoin, res+1)
        
        return minCoin if minCoin != float('inf') else -1
    
    def coinChangeMemoisation(self, amount: int, coins: List[int], memo = None) -> int:
        if memo == None:
            memo = {}
        if amount in memo:
            return memo[amount]
        
        if amount == 0: return 0
        
        if amount<0: return -1
        minCoin = float('inf')
        for coin in coins:
            remainder = amount - coin
            res = self.coinChangeMemoisation(remainder,coins, memo)
            if res>=0:

                minCoin = min(minCoin, res+1)
        memo[amount] = minCoin if minCoin != float('inf') else -1
        
        return minCoin if minCoin != float('inf') else -1
    
    def coinChangeTabulation(self, amount: int, coins: List[int]) -> int:
        table = [float('inf')]*(amount+1)
        table[0] = 0

        for i in range(1,len(table)):
            for n in coins:
                if i-n>= 0:
                    table[i] = min(table[i], table[i-n]+1)

        
        return table[amount] if table[amount] != float('inf') else -1
        
    
sol = Solution()

coins = [1,2,5]
amount = 11
print(sol.coinChangeRecusion(amount, coins))
print(sol.coinChangeMemoisation(amount, coins))
print(sol.coinChangeTabulation(amount, coins))

coins = [2]
amount = 3
print(sol.coinChangeRecusion(amount, coins))
print(sol.coinChangeMemoisation(amount, coins))
print(sol.coinChangeTabulation(amount, coins))

coins = [1]
amount = 0
print(sol.coinChangeRecusion(amount, coins))
print(sol.coinChangeMemoisation(amount, coins))
print(sol.coinChangeTabulation(amount, coins))

   