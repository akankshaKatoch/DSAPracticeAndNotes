from typing import List
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []
        

        que = deque([beginWord])
        adjacency = defaultdict(list)
        distance = {beginWord:0}
        
        
        while que:
            current_word = que.popleft()
            
            #possible_path = []

            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = current_word[:i] + c + current_word[i+1:]

                    if next_word in wordSet:
                        if next_word not in distance:
                            distance[next_word] = distance[current_word] + 1
                            que.append(next_word)
                        if distance[next_word] == distance[current_word] + 1:
                            adjacency[current_word].append(next_word)
        result = []
        path = [beginWord]

        def dfs(word, path):
            if word == endWord:
                result.append(path.copy())
                return
            for neighbour in adjacency[word]:
                path.append(neighbour)
                dfs(neighbour)
                path.pop()

        dfs(beginWord, [beginWord])
        return result

                



        





beginWord = "hit" 
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]
sol = Solution()
print(sol.ladderLength(beginWord,endWord, wordList))