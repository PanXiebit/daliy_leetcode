#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp2
        on = -prices[0]
        out = 0

        for i in range(1, len(prices)):
            on = max(on, 0-prices[i])
            out = max(out, on + prices[i])

        return out

# @lc code=end

