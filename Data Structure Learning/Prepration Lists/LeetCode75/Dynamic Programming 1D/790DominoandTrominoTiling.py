class Solution:
    
    def numTilingsRecusrsive(self, n: int) -> int:
        """
        now try to understand how dominoes and tromios tiling fill the squares. 

        f(n-1) with 1 vertical domino

        f(n-2) with two horzontal domino

        we need two tromino 

        to resolve this problem imaging function 
        if n = 0 no tiles only 1 way to do it. 
        if n = 1 only 1 way to do it. 
        
        """
        # recusrsive solution
        
        MOD = 10**9 + 7
        def dp(k):
            if k == 0:
                return 1
            if k == 1:
                return 1
            if k == 2:
                return 2
            
            return (dp(n-1) + dp(n-2) + 2*dp(n-3)) % MOD
        return dp(n)
        
    def numTilingsMemoisation(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        def dp(k):
            if k<0:
                return 0 
            if k in memo:
                return memo[k]
            
            if k == 0:
                return 1
            if k == 1:
                return 1
            if k == 2:
                return 2
            
            memo[k] = (2*dp(k-1) + dp(k-3)) % MOD
            return memo[k]
        return dp(n)


    def numTilingsTabulation(self, n: int) -> int:
        table = [0]*(n+1)
        MOD = 10**9 + 7
        table[0] = 1
        table[1] = 1
        table[2] = 2
        
        for i in range(3, n+1):
            table[i] = (2*table[i-1] + table[i-3]) % MOD
            
        #print(table)
        return table[n]
    
sol = Solution()
n = 30
#print(sol.numTilingsRecusrsive(n))
print(sol.numTilingsMemoisation(n))
print(sol.numTilingsTabulation(n))

n = 4
#print(sol.numTilingsRecusrsive(n))
print(sol.numTilingsMemoisation(n))
print(sol.numTilingsTabulation(n))
