class Solution:
    def addNoInString(self, s: str): 
        total = 0
        cur = 0
        for char in s:
            if char.isdigit():
                cur = cur*10 + int(char)
            else:
                total += cur
                cur = 0
        return total

        """
        temp = []
        sum = 0

        for char in s:
            
            if char.isdigit():
                print(char)
                temp.append(int(char))
            else:
                a = 0
                unit = 1
                if temp:
                    for i in temp[::-1]:
                        a += i*unit
                        unit *= 10
                sum += a
                temp = []
        if temp:
            num = 0
            unit = 1
            for i in temp[::-1]:
                num += i * unit
                unit *= 10
            total += num
                
        return sum 
    """
            
sol = Solution()
s = 'Gl123a045ssd0908oo6r'

print(sol.addNoInString(s))
