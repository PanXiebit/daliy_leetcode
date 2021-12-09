#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        path = []
        results = []

        def backtracking(startIndex):
            # 终止条件
            if len(path) == k:
                results.append(path.copy())
                return

            # 单层循环
            for i in range(startIndex, n + 1):
                path.append(i)
                backtracking(i+1)
                path.pop()

        backtracking(1)

        return results



# @lc code=end

