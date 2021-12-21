#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        num_dict = defaultdict(int)
        for n in nums:
            num_dict[n] += 1

        sort_dist = sorted(num_dict.items(), key=lambda item:item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sort_dist[i][0])
        return res
# @lc code=end

