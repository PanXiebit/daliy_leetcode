#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # sort_nums = sorted(nums, reverse=True)

        # return sort_nums[k-1]

        self.quick_sort(nums, 0, len(nums)-1)
        return nums[len(nums)-k]

    def quick_sort(self, list, low, high):
        if low >= high: return list
        i = low
        j = high
        pivot = list[low]
        while(low < high):
            while(low < high and pivot <= list[high]):
                high -= 1
            list[low] = list[high]
            while(low < high and pivot >= list[low]):
                low += 1
            list[high] = list[low]
        list[low] = pivot

        self.quick_sort(list, i, low-1)
        self.quick_sort(list, low+1, j) 



    

# @lc code=end

