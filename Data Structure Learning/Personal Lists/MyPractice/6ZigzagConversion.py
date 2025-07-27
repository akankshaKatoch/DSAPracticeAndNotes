class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row_map = [[] for _ in range(numRows)]
        current_row = 0
        columndir = 1

        for char in s:
            row_map[current_row].append(char)
            current_row += columndir
            if current_row == 0 or current_row == numRows -1:
                columndir *= -1
        result = []

        for row in row_map:
            result.extend(row) 
        return "".join(result)
            






s = "PAYPALISHIRING"
numRows = 3
sl= Solution()
print(sl.convert(s, numRows))
#Output: "PAHNAPLSIIGYIR"
"""
[P,  , A,  , H]
[A, P, L, S, I]
[y,  , I,  , R]"""