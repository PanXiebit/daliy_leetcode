#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        right = left = up = down = 0
        for chr in moves:
            if chr == "R":
                right += 1
            elif chr == "L":
                left += 1
            elif chr == "U":
                up += 1
            else:
                down += 1
        if right == left and up == down:
            return True
        else:
            return False

# @lc code=end

