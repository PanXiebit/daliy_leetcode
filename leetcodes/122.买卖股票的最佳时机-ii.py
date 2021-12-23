#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        # res = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         res += prices[i] - prices[i-1]
        # return res

        # dp
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return max(dp[-1][0], dp[-1][1])

        ## 这里有个误区就是，我在考虑dp[i][0]，会去考虑 dp[i-2], dp[i-3]，导致递推公式写不出来
        # 但其实上述代码考虑了这个情况的。比如 i=1时卖入，i=2接着买入,他俩的值是不变的 dp[i][0] = max(dp[i-1][0]。

# @lc code=end

