from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        #left = 0 
        result = []
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1
        

        for i in range(len(s)- total_len + 1):
            seen = defaultdict(int)
            for j in range(i, i + total_len, word_len):
                current_word = s[j:j + word_len]
                if current_word in word_count:
                    seen[current_word] += 1
                    if seen[current_word] > word_count[current_word]:
                        break
                else:
                    break
            if seen == word_count:
                result.append(i)


        return result 
        


s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

sol = Solution()
print(sol.findSubstring(s, words))