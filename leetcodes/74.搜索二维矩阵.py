#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target and target <= matrix[i][-1]:
                line = i
                break
        
        if line == -1:
            return False

        return self.binary_serach(matrix[line], target)


    def binary_serach(self, nums, target):
        start = 0
        end = len(nums) - 1

        while(start <= end):
            middle = int((end - start) / 2 + start)

            if nums[middle] == target:
                return True
            else:
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
        return False

# @lc code=end

