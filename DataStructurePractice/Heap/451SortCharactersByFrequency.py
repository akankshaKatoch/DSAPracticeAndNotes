from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict = defaultdict(int)
        for char in s:
            freq_dict[char] +=1
        
        result = []
        heap =[]
        for char, freq in freq_dict.items():
            heapq.heappush(heap, (-freq, char))
        
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char*-freq)
        print(result)
        return "".join(result)
        

        


        


        
s = "tree"
sol = Solution()
print(sol.frequencySort(s))