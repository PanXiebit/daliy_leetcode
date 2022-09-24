#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums, 0, len(nums)-1)
        # return sorted(nums)

    def quick_sort(self, list, i, j):
        if i >= j: return list
        pivot = list[i]
        low = i
        high = j

        while(i < j):
            while(i<j and list[j] >= pivot):
                j -= 1
            list[i] = list[j]
            while(i <j and list[i] <= pivot):
                i += 1
            list[j] = list[i]
        # print(i, j)
        list[i] = pivot
        self.quick_sort(list, low, i-1)
        self.quick_sort(list, i+1, high)
        return list


# @lc code=end

