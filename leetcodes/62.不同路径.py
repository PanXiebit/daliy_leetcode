#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m ==0 or n == 0: return 0

        import numpy as np

        dp = np.zeros((m, n))
        dp[0, :] = 1
        dp[:, 0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i, j] = dp[i-1, j] + dp[i, j-1]
        
        return int(dp[-1, -1])
# @lc code=end

