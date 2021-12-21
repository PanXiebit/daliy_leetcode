#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start

from typing import DefaultDict


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for (cur_idx, cur_n) in enumerate(nums*2):
            cur_idx %= len(nums)
            if len(stack) == 0:
                stack.append((cur_n, cur_idx))
            else:
                while(len(stack) > 0 and cur_n > stack[-1][0]):
                    top_n, top_idx = stack.pop(-1)
                    res[top_idx] = cur_n
                stack.append((cur_n, cur_idx))
        return res
    

# @lc code=end

