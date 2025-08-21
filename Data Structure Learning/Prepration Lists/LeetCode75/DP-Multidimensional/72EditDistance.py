class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) > len(word1):
            word1, word2 = word2, word1

        m = len(word1)
        n = len(word2)

        prev = list(range(n+1))

        for i in range(1, m+1):
            curr = [i] + [0]*n
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
            prev = curr
        return prev[n]
        
        """
        #using recursion
        def f(i, j):
            if i == m: return n-j
            if j == n: return m - i

            if word1[i] == word2[j]:
                return f(i+1, j+1)
            
            return 1 + min(f(i+1, j), f(i, j+1), f(i+1, j+1))
        
        return f(0,0)
        """
