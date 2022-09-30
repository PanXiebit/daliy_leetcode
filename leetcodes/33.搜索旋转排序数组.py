#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while(left <= right):
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] >= nums[left]: # 左边是有序的，右边是无序的
                if target < nums[middle] and target >= nums[left]:
                    right = middle -1
                else:
                    left = middle + 1
            else: # middle < left, 右边有序
                if target > nums[middle] and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle -1
            
        # if left == right and nums[left] == target:
        return -1
                    

# @lc code=end

