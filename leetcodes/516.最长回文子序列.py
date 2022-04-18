#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
# 解题思路：
# 状态
# f[i][j] 表示 s 的第 i 个字符到第 j 个字符组成的子串中，最长的回文序列长度是多少。

# 转移方程
# 如果 s 的第 i 个字符和第 j 个字符相同的话

# f[i][j] = f[i + 1][j - 1] + 2

# 如果 s 的第 i 个字符和第 j 个字符不同的话

# f[i][j] = max(f[i + 1][j], f[i][j - 1])

# 然后注意遍历顺序，i 从最后一个字符开始往前遍历，j 从 i + 1 开始往后遍历，这样可以保证每个子问题都已经算好了。

# 初始化
# f[i][i] = 1 单个字符的最长回文序列是 1

# 结果
# f[0][n - 1]
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]

# @lc code=end

