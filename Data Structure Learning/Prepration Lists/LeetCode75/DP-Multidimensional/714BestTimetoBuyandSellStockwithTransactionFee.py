from typing import List 

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for p in prices[1:]:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)

        return cash
    

sol = Solution()
prices = [1,3,2,8,4,9]
fee = 2
print(sol.maxProfit(prices, fee))