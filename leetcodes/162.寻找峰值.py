#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while(left < right):
            mid = (left + right) // 2
            # print(left, right, mid)
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        # print(left, right, mid)
        return left


# @lc code=end

