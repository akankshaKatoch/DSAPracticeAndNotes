class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        int1 = 0
        int2 = 0

        for char in num1:
            int1 = 10*int1 + int(char)

        for char in num2:
            int2 = 10*int2 + int(char)

        return str(int1*int2)

        

num1 = "123"
num2 = "456"

sol = Solution()
print(sol.multiply(num1,num2))