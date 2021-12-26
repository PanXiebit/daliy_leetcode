#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        unhold = 0

        for i in range(len(prices)):
            unhold = max(unhold, hold + prices[i]- fee)
            hold = max(hold, unhold - prices[i])

        return unhold
# @lc code=end

