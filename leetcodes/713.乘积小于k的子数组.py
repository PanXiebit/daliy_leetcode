#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k ==0 or k ==1: return 0
        prod = 1
        res = 0
        cur = []
        for i in range(len(nums)):
            cur.append(nums[i])
            prod *= nums[i]
            if prod < k:
                res += len(cur)
            else:
                while(prod >= k):
                    h = cur.pop(0)
                    prod /= h
                res += len(cur)
            # print("cur: ", cur, res)
        return res



# @lc code=end

