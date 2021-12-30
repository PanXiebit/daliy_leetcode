#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_res = -1

        while(l <= r):
            res = (r -l) * min(height[l], height[r])
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
            if res > max_res:
                max_res = res
        return max_res
            



# @lc code=end

