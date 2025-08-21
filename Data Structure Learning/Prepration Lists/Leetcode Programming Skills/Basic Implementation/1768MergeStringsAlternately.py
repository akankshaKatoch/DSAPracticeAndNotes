#https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        count = 0
        #if len(word1)>len(word2):
        #    word1, word2 = word2, word1
 
        for a, b in zip(word1, word2):
            print( a, b)  
            res.append(a)
            res.append(b) 
            count += 1 
        if count <= len(word2)-1:
            res.append(word2[count:])    
        if count <= len(word1)-1:
            res.append(word1[count:])   
        return "".join(res)
sol = Solution()

word1 = "abc"; word2 = "pqrst"
print(sol.mergeAlternately(word1, word2))


# PS
"""
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.

given example: word1 and word2 
output a,p,b,q,r

edge case when empty string? return empty. 
when either string is longer return remaining part. 



"""