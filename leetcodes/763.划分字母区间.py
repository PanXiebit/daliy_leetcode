#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict
        c_num = defaultdict(int)
        for c in s:
            c_num[c] += 1

        res = []
        cur_dict = {}
        start_id, end_id = 0, 0
        for id, c in enumerate(s):
            c_num[c] -= 1
            cur_dict[c] = c_num[c]
            if cur_dict[c] == 0:
                cur_dict.pop(c)
            if len(cur_dict) == 0:
                end_id = id + 1
                res.append(end_id - start_id)
                start_id = end_id
        return res

# @lc code=end

