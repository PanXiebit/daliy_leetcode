#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for cur_idx, cur_t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((cur_t, cur_idx))
            elif len(stack) > 0:
                while(len(stack) > 0 and cur_t > stack[-1][0]):
                    top_t, top_idx = stack.pop(-1)
                    res[top_idx] = cur_idx - top_idx
                
                stack.append((cur_t, cur_idx))
        return res





# @lc code=end

