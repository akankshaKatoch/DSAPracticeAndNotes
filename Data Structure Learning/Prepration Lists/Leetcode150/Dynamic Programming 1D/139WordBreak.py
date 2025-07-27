from typing import List
class Solution:
    def wordBreakRecusrsive(self, s: str, wordDict: List[str]) -> bool:
        if s == '': return True
        for word in wordDict:
            #match first inex value of both strings
            if s.find(word) == 0:
                target = s.replace(word, '', 1)
                if self.wordBreakRecusrsive(target, wordDict) == True:
                    return True
        return False
    
    def wordBreakMemoisation(self, s: str, wordDict: List[str], memo = None) -> bool:
        if memo is None:
            memo = {}
        if s == '': return True
        if s in memo:
            return memo[s]
        for word in wordDict:
            #match first inex value of both strings
            if s.find(word) == 0:
                target = s.replace(word, '', 1)
                if self.wordBreakMemoisation(target, wordDict, memo) == True:
                    memo[target] = True
                    return True
        return False
    
    def wordBreakTabulation(self, s: str, wordDict: List[str]) -> bool:
        table = [False]*(len(s)+1)
        table[0] = True

        for i in range(len(s)):
            if table[i]:
                for word in wordDict:
                    if i+len(word)<= len(s) and s[i:i+len(word)] == word:
                        table[i+len(word)] = True
        #print(table)
        return table[len(s)]
        
        
sol = Solution()
s = "leetcode"
wordDict = ["leet","code"]
print(sol.wordBreakRecusrsive(s, wordDict))
print(sol.wordBreakMemoisation(s, wordDict))
print(sol.wordBreakTabulation(s, wordDict))


s = "applepenapple" 
wordDict = ["apple","pen"]
print(sol.wordBreakRecusrsive(s, wordDict))
print(sol.wordBreakMemoisation(s, wordDict))
print(sol.wordBreakTabulation(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(sol.wordBreakRecusrsive(s, wordDict))
print(sol.wordBreakMemoisation(s, wordDict))
print(sol.wordBreakTabulation(s, wordDict))