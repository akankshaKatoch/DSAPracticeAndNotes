# https://leetcode.com/problems/flood-fill/description/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        currentcolor = image[sr][sc]

        if currentcolor == color:
            return image

        def dfs(image, r, c, currentcolor, changeColor):
            if r<0 or c<0 or r>= len(image) or c >= len(image[0]) or image[r][c] != currentcolor :
                return 
            
            image[r][c] = changeColor
            dfs(image, r-1, c, currentcolor, changeColor)
            dfs(image, r+1, c, currentcolor, changeColor)
            dfs(image, r, c-1, currentcolor, changeColor)
            dfs(image, r, c+1, currentcolor, changeColor)
        dfs(image, sr, sc, currentcolor, color)
        return image
            




image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
color = 2