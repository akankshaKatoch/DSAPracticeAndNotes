class Solution:
    def romanToInt(self, s: str) -> int:

        val_sym = { 'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL':40,
                    'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        sum = 0
        char =0
        while char <len(s):
            #print(char)
            
            if char+1<len(s) and s[char]+s[char+1] in val_sym:
                #print(s[char]+s[char+1] , val_sym[s[char]+s[char+1]])
                sum += val_sym[s[char]+s[char+1]]
                char += 2
                #print(s[char],s[char+1])
            else: 
                #print(s[char], val_sym[s[char]] )
                sum += val_sym[s[char]]
                char +=1          

        return sum
s = "MMMDCCXLIX"

sol = Solution()
print(sol.romanToInt(s))


