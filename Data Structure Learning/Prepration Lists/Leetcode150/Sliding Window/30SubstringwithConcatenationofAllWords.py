from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # two key points here: Word in words are of same length. 
        # so when they concatenate we are looking for the whole string match in different combination 
        # in string s. 

        if not s or not words:
            return []
        
        word_len = len(words[0])

        total_len = word_len* len(words)
        wordCount = Counter(words)
        print(wordCount)
        result = []

        for i in range(len(s)-total_len+1):
            #currmap = wordCount
            seen = {}
            for j in range(0, total_len, word_len):
                word = s[i+j:i+j+word_len]
                if word in wordCount:
                    seen[word] = seen.get(word, 0) +1
                    if seen[word]>wordCount[word]:
                        break
                else:
                    break
            else: result.append(i)

        return result 
            
sol = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(sol.findSubstring(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(sol.findSubstring(s, words))

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(sol.findSubstring(s, words))

 