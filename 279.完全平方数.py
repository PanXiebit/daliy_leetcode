#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        import math
        queue = [n]
        depth = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                sqrt = math.floor(math.sqrt(cur))
                # print("cur, sqrt: ", cur, sqrt)
                for j in range(sqrt, 0, -1):
                    nx_num = cur - j**2
                    if nx_num == 0:
                        return depth + 1
                    queue.append(nx_num)
                    # print("j, nx_num: ", j, nx_num)
            depth += 1
 



# @lc code=end

