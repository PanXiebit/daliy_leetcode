#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        # hold = -prices[0]
        # unhold = 0

        # for i in range(1, len(prices)):
        #     hold = max(hold, unhold - prices[i])
        #     unhold = max(unhold, hold + prices[i])
        # return unhold 

        # dp = [[0,0] for _ in range(len(prices))]

        # dp[0][0] = 0
        # dp[0][1] = -prices[0]

        # dp[1][0] = max(0, -prices[0] + prices[1])
        # dp[1][1] = max(-prices[0], 0 - prices[1])

        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) # 不持有股票
        #     dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]) # 持有股票

        # return dp[-1][0]

        # dp = [[0,0] for _ in range(len(prices))]

        hold = -prices[0]
        unhold = 0

        pre_unhold = 0

        for i in range(len(prices)):
            tmp = unhold
            unhold = max(unhold, hold + prices[i])
            hold = max(hold, pre_unhold - prices[i])
            pre_unhold = tmp

        return unhold

# @lc code=end

