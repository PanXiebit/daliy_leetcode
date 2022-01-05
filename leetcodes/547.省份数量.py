#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        n = len(isConnected)
        cities = [0] * n

        res = 0

        for i in range(n):
            if cities[i] != 1: 
                res += 1
            cities[i] = 1
            isConnected[i][i] = -2
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    self.dfs(i, j, isConnected, cities)
        return res

    def dfs(self, i, j, isConnected, cities):
        cities[j] = 1
        isConnected[j][j] = -2
        isConnected[i][j] = -2
        isConnected[j][i] = -2

        if max(isConnected[j]) == 0: return

        for k in range(len(isConnected)):
            if isConnected[j][k] == 1:
                self.dfs(j, k, isConnected, cities)





# @lc code=end

