#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:
            if ch == "(" or ch == "[" or ch=="{":
                stack.append(ch)
            else:
                if len(stack) == 0: return False
                if ch == ")":
                    top = stack[-1]
                    if top != "(": return False
                    else: stack.pop(-1)
                if ch == "}":

                    top = stack[-1]
                    if top != "{": return False
                    else: stack.pop(-1)
                if ch == "]":

                    top = stack[-1]
                    if top != "[": return False
                    else: stack.pop(-1)
        if len(stack) == 0:
            return True
        else:
            return False
                
        
# @lc code=end

