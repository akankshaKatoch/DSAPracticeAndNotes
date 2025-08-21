class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1=="0" or num2=='0':
            return "0"
        """
        123
        123
        ---
        369
        2460
        """
        m,n= len(num1), len(num2)
        res = [0] *(m+n)
        for i in range(m-1, -1, -1):
            d1 = ord(num1[i]) - 48
            for j in range(n-1, -1, -1):
                d2 = ord(num2[j]) - 48
                mul = d1*d2
                p1, p2 = i+j, i+j+1

                s = mul + res[p2]
                res[p2] = s % 10
                res[p1] += s// 10

        i = 0
        while i<len(res) and res[i] == 0:
            i += 1
        
        return "".join(map(str, res[:])) if i < len(res) else "0"

sol = Solution()
num1 = "123"
num2 = "456"
print(sol.multiply(num1, num2))