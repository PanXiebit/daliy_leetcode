#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        import numpy as np

        map = np.zeros((n, n), dtype=np.int32)
        cycle_num = n // 2 + 1
        start, end = 1, 1
        for i in range(cycle_num):
            end += (n-i*2)
            map[i, i:n-i] = list(range(start, end))
            start = end

            if end == n**2:
                break

            end += (n-i*2-1) 
            map[i+1:n-i, n-1-i] = list(range(start, end))
            start = end


            end += (n-i*2-1)
            map[n-1-i, i:n-(i+1)] = list(range(end-1, start-1, -1))
            start = end
            
            end += (n-i*2-2)
            map[i+1:n-(i+1), i] = list(range(end-1, start-1, -1))
            start = end

        return map.tolist()
        # res = []

        # for i in range(map.shape[0]):
        #     res.append(map[i].tolist())

            


# @lc code=end

