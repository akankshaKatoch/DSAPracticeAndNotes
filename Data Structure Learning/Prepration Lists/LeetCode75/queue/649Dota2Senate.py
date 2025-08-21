from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
            
        print(dire , " and ", radiant)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r<d:
                radiant.append(r+n)
            else:
                dire.append(d+n)
            print(dire , " and ", radiant)

        return "Radiant" if radiant else "Dire"        


sol = Solution()
s = "RRRSSRSRS"
print(sol.predictPartyVictory(s))
