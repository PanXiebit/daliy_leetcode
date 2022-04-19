#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        return self.findlen(nums2, nums1) if len1 > len2 else  self.findlen(nums1, nums2)


    def findlen(self, nums1, nums2):
        total_len = len(nums1) * 2 -2 + len(nums2)
        maxLen = 0
        for i in range(1, total_len + 1):
            cur_nums1 = nums1[:i]
            cur_nums2 = nums2[-i:]
            print("cur_nums1: ", cur_nums1, cur_nums2)
            cur_len = 0
            for j in range(i):
                if cur_nums1[j] == cur_nums2[j]: cur_len += 1
            if cur_len > maxLen: 
                maxLen = cur_len
        return maxLen

# @lc code=end

