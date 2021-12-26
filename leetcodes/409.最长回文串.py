#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        c_num = defaultdict(int)

        for c in s:
            c_num[c] += 1
        res = 0
        flag = True
        for n in c_num.values():
            if n % 2 == 0:
                res += n
            else:
                res += n-1
                if flag:
                    res += 1
                    flag = False
        return res
        

        
# @lc code=end

