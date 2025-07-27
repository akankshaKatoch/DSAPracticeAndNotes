class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Tabulation
        table = [[0 for _ in range(n+1)] for _ in range(m+1)]

        table[0][0] = 0
        table [1][1] = 1

        for i in range(m+1):
            for j in range(n+1):
                current = table[i][j]
                if j+1<=n:
                    table[i][j+1] += current
                if i+1<=m:
                    table[i+1][j] += current
        return table[m][n]



        '''
        key = (m, n)
        # memoised Way
        if memo == None:
            memo = {}
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        if key in memo:
            return memo[key]
        memo[key] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)

        return memo[key]
        '''


        # recursive Way
        '''
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        '''
         