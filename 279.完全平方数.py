#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # bfs 方法
        # import math
        # queue = [n]
        # depth = 0
        # while queue:
        #     for i in range(len(queue)):
        #         cur = queue.pop(0)
        #         sqrt = math.floor(math.sqrt(cur))
        #         # print("cur, sqrt: ", cur, sqrt)
        #         for j in range(sqrt, 0, -1):
        #             nx_num = cur - j**2
        #             if nx_num == 0:
        #                 return depth + 1
        #             queue.append(nx_num)
        #             # print("j, nx_num: ", j, nx_num)
        #     depth += 1
        
        # dp 方法
        dp = [n] * (n + 1)
        dp[0] = 0
        # 遍历背包
        for j in range(1, n+1):
            for i in range(1, n):
                num = i ** 2
                if num > j: break
                # 遍历物品
                if j - num >= 0:
                    dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]


 



# @lc code=end

