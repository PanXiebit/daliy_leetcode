#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.probs = []
        sum_w = sum(w)
        pre_sum = 0
        for weight in w:
            pre_sum += weight
            self.probs.append(pre_sum / sum_w)



    def pickIndex(self) -> int:
        import random 
        p = random.random()
        for idx, prob in enumerate(self.probs):
            if p < prob:
                return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

