#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        k = 2
        # import numpy as np

        # dp = np.zeros((len(prices), k, 2))
        dp = [[[0,0] for _ in range(k+1)] for _ in range(len(prices))]

        # 至多0次交易
        # for i in range(len(prices)):
        #     dp[i][0][1] = -float("inf") # 表示至多0次交易时，持有股票
        #     dp[i][0][0] = 0    # 表示至多0次交易时，不持有股票的状态

        # 第0天
        for j in range(1, k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i]) # 不持有股票
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]) # 持有股票
                
        return dp[-1][-1][0]
        

# @lc code=end

