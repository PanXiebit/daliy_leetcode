#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import numpy as np

        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)

        for i in range(1,len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return int(max(dp))

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import numpy as np

        if len(nums) == 0:
            return 0
        
        dp = np.ones(len(nums), dtype=np.int32)

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return int(max(dp))

# @lc code=end

