from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        # 1 step at a time ahead and we need shortest time to do this. 
        # hit -> hot -> dot -> dog -> cog

        que = deque([(beginWord, 1)])

        visited = set()

        visited.add(beginWord)

        while que:
            current_word, steps = que.popleft()
            #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            for i in range(len(current_word)):
                #print("===========================================================================")
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]

                    #print(f"current_word[:{i}] + {c} + current_word[{i+1}:] = {current_word[:i] + c + current_word[i+1:]}")
                    #print("next_word -> ", next_word)
                
                    if next_word == endWord:
                        print("END WORD FOUND : ", next_word)
                        return steps + 1
                    
                    if next_word in wordList and next_word not in visited:
                        print('word found : ', next_word)
                        que.append((next_word, steps+1))
                        visited.add(next_word)
                #print("===========================================================================")

            #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return 0





beginWord = "hit" 
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
sol = Solution()
print(sol.ladderLength(beginWord,endWord, wordList))