#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        import numpy as np
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = np.zeros((m, n), dtype=np.int32)

        if obstacleGrid[0][0] == 1:
            return 0
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        
        dp[0, 0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0, i] = dp[0, i-1]
            else:
                dp[0, i] = 0
        
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i, 0] = dp[i-1, 0]
            else:
                dp[i, 0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i,j] = dp[i-1, j] + dp[i, j-1]
                else:
                    dp[i, j] = 0
        return int(dp[m-1, n-1])
                

# @lc code=end

