class Solution:
    def intToRoman(self, num: int) -> str:
        val_sym = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        romlist = []
        
        for value, symbol in val_sym:
            while num >= value:
                romlist.append(symbol)
                num -= value
            if num == 0:
                break
        return ''.join(romlist)

      
   

num = 3749
#output = "MMMDCCXLIX"
sol = Solution()
print(sol.intToRoman(num))