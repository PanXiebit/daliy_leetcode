#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # max_len = max(len(text1), len(text2))

        # dp = [0] * max_len
        # longtext = text1 if len(text1) >= len(text2) else text2
        # shorttext = text1 if len(text1) < len(text2) else text2

        # if longtext[0] in shorttext: 
        #     dp[0] = 1
        # else:
        #     dp[0] = 0
        # print("dp: ", dp)

        # for i in range(1, max_len):
        #     if longtext[i] in shorttext:
        #         dp[i] = max(dp[:i]) + 1
        #     else:
        #         dp[i] = 0
        #     print("dp: ", dp)
        # return max(dp)

        import numpy as np

        dp = np.zeros((len(text1)+1, len(text2)+1), dtype=np.int32)

        # for i in range(len(text1)):
        #     if text1[i] == text2[0]:
        #         dp[i, 0] = 0
        #     else:
        #         dp[i, 0] = 0

        # for j in range(len(text2)):
        #     if text2[j] == text1[0]:
        #         dp[0, j] = 1
        #     else:
        #         dp[0, j] = 0

        # print(dp)

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i,j] = max(dp[i-1, j-1] + 1, dp[i-1,j], dp[i, j-1])
                else:
                    dp[i,j] = max(dp[i-1, j-1], dp[i-1,j], dp[i, j-1])
        print("="*5)
        print(dp)
        return int(dp[len(text1), len(text2)])

# @lc code=end
        

