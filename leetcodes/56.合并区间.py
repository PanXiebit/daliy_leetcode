#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return intervals

        sort_intervals = sorted(intervals, key=lambda item:item[0])
        # print(sort_intervals)

        res = [sort_intervals[0]]
        for vals in sort_intervals[1:]:
            if vals[0] <= res[-1][1]:
                # 合并
                res[-1][1] = max(vals[-1], res[-1][1])
            else:
                res.append(vals)
        return res




# @lc code=end

