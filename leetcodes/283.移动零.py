#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return

        # for p in range(len(nums)):
        #     if nums[p] == 0:
        #         for q in range(p+1, len(nums)):
        #             if nums[q] != 0:
        #                 nums[p] = nums[q]
        #                 nums[q] = 0
        #                 break
        q = 0
        for p in range(len(nums)):
            if nums[p] != 0:
                nums[q] = nums[p]
                q += 1
        
        for p in range(q, len(nums)):
            nums[p] = 0

# @lc code=end

