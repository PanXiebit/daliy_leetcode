#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        # 方法 1 
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        while(left <= right):
            print(left, right, middle)
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                if nums[left] < target:
                    left = left + 1
                if nums[right] > target:
                    right = right - 1
                if nums[left] == nums[right]:
                    return [left, right]
            
            middle = (left + right) // 2
        if left == right and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]
        
        # 方法 2
        def getLeftBoard(nums, target):
            left, right = 0, len(nums) - 1
            while(left <= right):
                middle = (left + right) // 2
                if nums[middle] >= target:
                    right = middle - 1
                else:
                    left = middle + 1
            
            if left == len(nums):
                return -1
            if nums[left] != target:
                return -1
            return left

        def getRightBoard(nums, target):
            left, right = 0, len(nums) - 1
            while(left <= right):
                middle = (left + right) // 2
                if nums[middle] <= target:
                    left = middle + 1
                else:
                    right = middle - 1
            if right == -1:
                return -1
            if nums[right] != target:
                return -1
            else:
                return right
        
        leftboard = getLeftBoard(nums, target)
        rightboard = getRightBoard(nums, target)

        print("leftboard: ", leftboard)
        print("rightboard: ", rightboard)
     
        return [leftboard, rightboard]


# solution 3
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        flag = -1
        while(start <= end):
            middle = (end - start) // 2 + start
            if nums[middle] == target:
                flag = 1
                break
            elif nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
        if flag == -1: return [-1, -1]
        else:
            left = self.find_left(nums, 0, middle, target)
            right = self.find_right(nums, middle, len(nums)-1, target)
            return [left, right]  

    def find_left(self, nums, start, end, target):
        while(start <= end):
            middle = (end - start) // 2 + start
            if nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return start 

    
    def find_right(self, nums, start, end, target):
        
        while(start <= end):
            middle = (end - start) // 2 + start
            if nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return end


"""
- 二分查找：**循环不变量**，保持区间的定义不变，比如 [left, right], 那么 while(left <= right), 且nums[middle] > target时，middle肯定不可能等于target,则 right = middle - 1. 

寻找target在数组里的左右边界，有如下三种情况：

* 情况一：target 在数组范围的右边或者左边，例如数组{3, 4, 5}，target为2或者数组{3, 4, 5},target为6，此时应该返回{-1, -1}
* 情况二：target 在数组范围中，且数组中不存在target，例如数组{3,6,7},target为5，此时应该返回{-1, -1}
* 情况三：target 在数组范围中，且数组中存在target，例如数组{3,6,7},target为6，此时应该返回{1, 1}

这三种情况都考虑到，说明就想的很清楚了。
"""
            
# @lc code=end

