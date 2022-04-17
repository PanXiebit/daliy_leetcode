#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        val_idx = defaultdict(list)
        for i in range(len(nums)):
            val = nums[i]
            val_idx[val].append(i)
            if target - val in val_idx:
                if target - val != val:
                    return i, val_idx[target - val][0]
                elif len(val_idx[target - val]) >= 2:
                    return val_idx[val][:2]
        
        # from collections import defaultdict
        # num_index = defaultdict(list)
        # for i in range(len(nums)):
        #     num_index[nums[i]].append(i)
        #     if (target - nums[i]) in num_index:
        #         if target - nums[i] == nums[i] and len(num_index[nums[i]]) >= 2:
        #             return num_index[target - nums[i]][:2]
        #         if target - nums[i] != nums[i]:
        #             return i, num_index[target - nums[i]][0]

            
                


# @lc code=end

