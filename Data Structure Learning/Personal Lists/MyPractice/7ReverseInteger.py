class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        new_no = 0

        while x!=0:
            #print('x%10: ', x%10)
            digit = x%10
            new_no = new_no*10 + digit
            #print('x/10: ',x/10)
            #print('x//10: ',x//10)
            x = x//10
        
        if new_no*sign > 2**31 -1 or new_no*sign < -2**31:
            return 0
        return new_no*sign
    
x = 123
sl = Solution()
print(sl.reverse(x))