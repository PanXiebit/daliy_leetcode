#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if row == 0 or col == 0: return 0

        max_area = 0
        for i in range(row):
            for j in range(col):
                self.cur_area = 0
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    if self.cur_area > max_area:
                        max_area = self.cur_area
        return max_area

    def dfs(self, grid, i, j):
        if grid[i][j] == 1:
            self.cur_area += 1
            grid[i][j] = 2
            if i+1 < len(grid): self.dfs(grid, i+1, j)
            if i >= 1: self.dfs(grid, i-1, j)
            if j+1 < len(grid[0]): self.dfs(grid, i, j+1)
            if j >= 1: self.dfs(grid, i, j-1)
        else:
            return



# @lc code=end

