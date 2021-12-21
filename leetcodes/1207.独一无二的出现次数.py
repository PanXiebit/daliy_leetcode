#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict

        ht = defaultdict(int)
        for n in arr:
            ht[n] += 1
        
        nums = ht.values()
        dedup_nums = set(nums)
        if len(nums) > len(dedup_nums):
            return False
        else:
            return True

        
# @lc code=end

