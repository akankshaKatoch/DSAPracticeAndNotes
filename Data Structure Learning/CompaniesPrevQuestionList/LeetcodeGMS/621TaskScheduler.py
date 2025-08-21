from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #taskDic = defaultdict()
        freq = Counter(tasks)
        maxfrq = max(freq.values())
        maxcount = sum(1 for v in freq.values() if v == maxfrq)

        return max(len(tasks), (maxfrq - 1) * (n+1) + maxcount)
     


