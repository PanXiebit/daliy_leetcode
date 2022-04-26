#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0
        for i in range(length):
            # 奇数
            p = i
            q = i
            while(p >= 0 and q <= length-1):
                if s[p] == s[q]:
                    res += 1
                else:
                    break
                p -= 1
                q += 1

            p = i
            q = i+1
            while( p>= 0 and q <= length-1):
                if s[p] == s[q]:
                    res += 1
                else:
                    break
                p -= 1
                q += 1
        return res

# @lc code=end

