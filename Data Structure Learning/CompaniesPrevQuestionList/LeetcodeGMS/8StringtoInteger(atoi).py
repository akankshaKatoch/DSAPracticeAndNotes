class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        num = 0

        INT_MAX = 2**31 -1
        INT_MIN = -2**31

        while i< n and s[i] == " ":
            i += 1
        
        sign = 1
        if i<n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and s[i].isdigit():
            d = ord(s[i]) - 48

            if num > INT_MAX//10 or (num == INT_MAX // 10 and d > (7 if sign == 1 else 8)):
                return INT_MAX if sign == 1 else INT_MIN

            num = num*10 + d
            i +=1
        return sign * num

        # my intial solution

        """
        curr = 0
        solList = []

        for c in s:
            if c=='-':
                solList.append(c)
            elif c.isdigit():
                print(c)
                curr = curr*10 + int(c)
            else:
                if curr > 0:
                    break
        solList.append(str(curr))
        print(solList)
        
        return "".join(solList)
        """

sol = Solution()
s = "42"
print(sol.myAtoi(s))
s = "1337c0d3"
print(sol.myAtoi(s))
s = " -042"
print(sol.myAtoi(s))
