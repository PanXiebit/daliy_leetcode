#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []

        for c in s:
            if c == "#":
                if len(stack_s) == 0:
                    continue
                else:
                    stack_s.pop(-1)
            else:
                stack_s.append(c)

        for c in t:
            if c == "#":
                if len(stack_t) == 0:
                    continue
                else:
                    stack_t.pop(-1)
            else:
                stack_t.append(c)

        return stack_s == stack_t

        
# @lc code=end

