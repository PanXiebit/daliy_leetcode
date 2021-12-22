#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        res = 0
        for p in prices:
            low = min(low, p)
            res = max(res, p - low)
        return res



# @lc code=end

