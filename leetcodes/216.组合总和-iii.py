#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.nums = []
        self.res = []
        self.backtrace(n, k, 1)
        return self.res

    def backtrace(self, n, k, start):
        if len(self.nums) == k and sum(self.nums) == n:
            self.res.append(self.nums.copy())
            return


        for i in range(start, 10):
            if len(self.nums) < k and sum(self.nums) < n:
                self.nums.append(i)
                # print(self.nums)
                self.backtrace(n, k, i+1) 
                self.nums.pop(-1)
            else:
                return




# @lc code=end

