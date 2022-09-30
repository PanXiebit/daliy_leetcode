#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        nums = cardPoints[-k:] + cardPoints[:k]

        # print(nums, sum(cardPoints[:k]))

        res = cur_sum = sum(nums[:k])
        for i in range(1, k+1):
            cur_sum = cur_sum + nums[i+k-1] - nums[i-1]
            # print(cur_sum)
            if cur_sum > res:
                res = cur_sum
        return res



# @lc code=end

