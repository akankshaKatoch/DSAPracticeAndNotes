class Solution:
    def uniquePaths(self, m: int, n: int, memo = None) -> int:
        key = (m,n)
        if memo == None:
            memo = {}

        if key in memo: return memo[key]
        if m==1 or n==1:
            return 1
        if m==0 or n==0:
            return 0
        
        
        memo[key] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)

        return memo[key]

    def uniquePathsTab(self, m: int, n: int, memo = None) -> int:
        table = [[0 for _ in range(n+1)] for _ in range(m+1)]

        table[0][0] = 0
        table[1][1] = 1

        for i in range(m+1):
            for j in range(n+1):
                curr = table[i][j]
                if j+1<m:
                    table[i][j+1] += curr
                if i+1<n:
                    table[i+1][j] += curr
        return table[m+1][n+1]




sol = Solution()   
m = 3
n = 7
print(sol.uniquePaths(m,n))
