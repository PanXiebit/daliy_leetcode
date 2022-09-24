#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from hashlib import new


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = []
        length = len(nums1) + len(nums2)
        i = j = 0

        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                new_nums.append(nums1[i])
                i += 1
            else:
                new_nums.append(nums2[j])
                j += 1
        if i == len(nums1):
            new_nums = new_nums + nums2[j:]
        else:
            new_nums = new_nums + nums1[i:]
        
        # print(new_nums)

        if length % 2 != 0:
            return new_nums[length//2]
        else:
            return (new_nums[length//2] + new_nums[length//2-1])/2

        

        

# @lc code=end

