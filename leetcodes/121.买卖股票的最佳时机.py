#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # low = float("inf")
        # res = 0
        # for p in prices:
        #     low = min(low, p)
        #     res = max(res, p - low)
        # return res

        # dp
        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][0] = max(dp[i-1][0], 0 - prices[i]) # 只能买入一次
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return max(dp[-1][0], dp[-1][1])

# @lc code=end

