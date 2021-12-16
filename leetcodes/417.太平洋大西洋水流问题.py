#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        res = []
        for i in range(row):
            for j in range(col):
                self.flag = [[0]*col for i in range(row)]
                self.pacif, self.atlan = False, False
                self.dfs(heights, i, j)
                if self.pacif and self.atlan:
                    res.append([i,j])
        return res


    def dfs(self, heights, i, j):
        if i == 0 or j == 0: 
            self.pacif = True
            
        if i == len(heights)-1 or j==len(heights[0])-1: 
            self.atlan = True


        if not (0 <= i < len(heights) and 0 <= j < len(heights[0])):
            return
        
        if self.flag[i][j] == -1:
            return

        self.flag[i][j] = -1

        if j-1 >= 0 and heights[i][j] >= heights[i][j-1]: self.dfs(heights, i, j-1)
        if j+1 < len(heights[0]) and heights[i][j] >= heights[i][j+1]: self.dfs(heights, i, j+1)
        if i-1 >= 0 and heights[i][j] >= heights[i-1][j]: self.dfs(heights, i-1, j)
        if i+1 < len(heights) and heights[i][j] >= heights[i+1][j]: self.dfs(heights, i+1, j)
        
        
# @lc code=end

