from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0]*(n+1)

        offset = 1
        for i in range(1, n):
            if offset*2 == i:
                offset = i
            table[i] = table[i-offset] + 1
        
        return table