from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:

        """abccdd
        1 element needs to be odd values and rest elements as even values. 
        dict alphabet count. 
        for each keys i maintain the count for the event element and 1 longest odd element count. """
        char_dict = defaultdict(int)

        for char in s:
            char_dict[char] += 1
        print(char_dict)
        #My code is removing all the odd element but no we need to remove only 1 elemet and total count should be event 
        is_odd = False
        count = 0
        for value in char_dict.values():
            print(value)
            if value%2 == 0:
                print("1. ", value)
                count += value
            else: 
                # if it not event means 1 extra odd element is pesent. remove that extra element.
                count += value - 1
                is_odd = True

        return count +1 if is_odd else count 

s = "bananas"
sol = Solution()
print(sol.longestPalindrome(s))