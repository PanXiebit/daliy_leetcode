#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        if len1 == 0: return len2
        if len2 == 0: return len1

        import numpy as np
        map = np.zeros((len1+1, len2+1))

        for i in range(len2+1):
            map[0, i] = i
        for i in range(len1+1):
            map[i, 0] = i

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    map[i, j] = min(map[i-1, j]+1, map[i, j-1]+1, map[i-1, j-1])
                else:
                    map[i, j] = min(map[i-1, j]+1, map[i, j-1]+1, map[i-1, j-1]+1)
        
        return int(map[len1, len2])





        
        
        
        
        
        
        
        
        # import numpy as np
        # map = np.zeros((len(word1) + 1, len(word2) + 1))
        # if len(word1) == 0:
        #     return len(word2)
        # if len(word2) == 0:
        #     return len(word1)
        
        # for i in range(1, len(word2) + 1):
        #     map[0, i] = i
        # for j in range(1, len(word1) + 1):
        #     map[j, 0] = j
        
        # for i in range(1, len(word1) + 1):
        #     for j in range(1, len(word2) + 1):
        #         if word1[i-1] == word2[j-1]:
        #             map[i, j] = min(map[i-1, j]+1, map[i, j-1] + 1, map[i-1, j-1])
        #         else:
        #             map[i, j] = min(map[i-1, j]+1, map[i, j-1] + 1, map[i-1, j-1] + 1)

        # return int(map[len(word1), len(word2)])


    

# @lc code=end

