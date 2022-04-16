#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        result = []
        n = len(nums)
        for i in range(n):
            if (i != 0) and (nums[i] == nums[i - 1]):
                continue
            l = i + 1
            r = n - 1
            while(l < r):
                if (nums[i] > 0): break
                target = nums[i] + nums[l] + nums[r]
                if (target== 0):
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif (target < 0):
                    l += 1
                else:
                    r -= 1
            
        return result

# @lc code=end

