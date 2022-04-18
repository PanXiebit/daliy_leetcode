#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        
        row = len(grid)
        col = len(grid[0])
        
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    res += 1
                    self.dfs(grid, r, c)
        return res
  
    def dfs(self, grid, r, c): 
        if grid[r][c] == "1":
            grid[r][c] = "2"
            if r > 0: self.dfs(grid, r-1, c)
            if r < len(grid)-1: self.dfs(grid, r+1, c)
            if c > 0: self.dfs(grid, r, c-1)
            if c < len(grid[0]) -1: self.dfs(grid, r, c+1)
        
        else:
            return
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         count = 0 
#         row = len(grid)
#         col = len(grid[0])

#         for r in range(row):
#             for c in range(col):
#                 if (grid[r][c] == '1'):
#                     self.dfs(grid, r, c)
#                     count=count+1
#         return count

#     def dfs(self,grid,r,c):
#         if not (0<= r <len(grid) and 0<= c <len(grid[0])):
#             return 
#         if grid[r][c] != '1':
#             return

#         grid[r][c] = '2'; 
#         self.dfs(grid, r - 1, c)
#         self.dfs(grid, r + 1, c)
#         self.dfs(grid, r, c - 1)
#         self.dfs(grid, r, c + 1)
        

# @lc code=end

