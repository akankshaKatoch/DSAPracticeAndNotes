class Solution:
    #I will try to solve using tabulation.
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n== 1 or n ==2:
            return 1
        table = [0]*(n+1)
        #seedvalue
        table[0] = 0
        table[1] = 1
        table[2] = 1
        print(table)

        for i in range(3,n+1):
            #print(i)
            table[i] = table[i-1]+ table[i-2]+ table[i-3]
        print(table)
        return table[n]
    
    def tribonacciRecursive(self, n) -> int:

        if n == 0:
            return 0
        if n== 1 or n ==2:
            return 1
        
        trifib = self.tribonacciRecursive(n-1) + self.tribonacciRecursive(n-2) + self.tribonacciRecursive(n-3)

        return trifib

    def tribonacciDPMemo(self, n, memo = None) -> int:
        if memo == None:
            memo = {} 
        
          
        if n == 0:
            return 0
        if n== 1 or n ==2:
            return 1
        if n in memo:
            return memo[n] 
        
        memo[n] = self.tribonacciDPMemo(n-1, memo) + self.tribonacciDPMemo(n-2, memo) + self.tribonacciDPMemo(n-3, memo)

        return memo[n]




sol = Solution()
n = 7
print(sol.tribonacci(n))
print(sol.tribonacciRecursive(n))
print(sol.tribonacciDPMemo(n))
        