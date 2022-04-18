#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0

        maxH = 0
        a = []

        for i in range(len(height)):
            if height[i] > maxH:
                maxH = height[i]
            a.append(maxH - height[i])
        
        maxH = 0
        b = []
        for i in range(len(height)-1, -1, -1):
            if height[i] > maxH:
                maxH = height[i]
            b.insert(0, maxH - height[i])

        res = 0
        for i in range(len(height)):
            res += min(a[i], b[i])
        return res

# @lc code=end

