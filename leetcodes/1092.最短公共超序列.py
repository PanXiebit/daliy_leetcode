#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str1) >= len(str2):
            res = self.include(str1, str2)

        if len(str1) < len(str2):
            res = self.include(str2, str1)

        if res is not None:
            return res

        share_len = min(len(str1), len(str2))

        str1str2 = str2str1 = 0
        for i in range(share_len):
            if str1[-(i+1):] == str2[:i+1]:
                str1str2 = i + 1
            else:
                continue

        for i in range(share_len):
            if str2[-(i+1):] == str1[:i+1]:
                str2str1 = i+1
            else:
                continue
        
        if str1str2 >= str2str1:
            return str1 + str2[str1str2:]
        else:
            return str2 + str1[str2str1:]

    def include(self, str1, str2):
        for i in range(len(str1)):
            if str1[i:i+len(str2)] == str2:
                return str1
        return None


# @lc code=end

