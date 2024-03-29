#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for num in nums:
            if num != val:
                nums[res] = num
                res += 1
        return res


# @lc code=end

