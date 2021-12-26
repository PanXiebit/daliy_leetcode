#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    #     t_right = t
    #     for sc in s:
    #         if sc not in t_right: return False
    #         else: t_right = self.get_rightpart(t_right, sc)
    #     return True

    # def get_rightpart(self, t, sc):
    #     for i in range(len(t)):
    #         if t[i] == sc:
    #             return t[i+1:]
        import numpy as np

        dp =  np.zeros((len(s) + 1, len(t) + 1))

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i, j] = dp[i-1, j-1] + 1
                else:
                    dp[i, j] = max(dp[i-1, j], dp[i, j-1])
        # print(dp)

        if dp[len(s), len(t)] == len(s):
            return True
        else:
            return False
            
# @lc code=end

