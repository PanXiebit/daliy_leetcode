#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        sum = 0

        cur = []
        flag = False
        for i in range(len(nums)):
            cur.append(nums[i])
            sum += nums[i]
            if sum >= target:
                flag = True
                head = cur[0]
                while(sum-head >= target):
                    cur.pop(0)
                    sum -= head
                    head = cur[0]
    
                if len(cur) < res:
                    res = len(cur)
        if flag:
            return res
        else:
            return 0


# @lc code=end

