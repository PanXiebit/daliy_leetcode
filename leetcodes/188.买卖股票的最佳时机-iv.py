#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[[0,0] for _ in range(k+1)] for _ in range(len(prices))]

        # 第0天
        for j in range(1, k+1):
            dp[0][j][0] = 0 # 不持有股票
            dp[0][j][1] = -prices[0] # 持有股票

        for i in range(1, len(prices)):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[-1][-1][0]
# @lc code=end

