class Solution:
    def fibmemo(self, n: int, memo = None) -> int:
        if memo == None:
            memo = {}
        if n in memo:
            return memo[n]
        if n ==0:
            return 0
        if n == 1:
            return 1
        
        return self.fibmemo(n-1, memo) + self.fibmemo(n-2, memo)
    
    def fibTab(self, n: int) -> int:
        if n==0:
            return 0
        if n == 1:
            return 1
        table = [0]*(n+1)
        table[0] = 0
        table[1] = 1

        for i in range(2, n+1):
            table[i] = table[i-1]+ table[i-2]
        
        return table[n]
    
sol = Solution()

n = 6
print(sol.fibmemo(n))
print(sol.fibTab(n))



        