#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:


        results = []
        path = []

        def check(path, col):
            if col in path:
                return False
            m = len(path)
            for i, c in enumerate(path):
                if abs(i-m) == abs(c-col):
                    return False
            return True
            
        def backtracking():
            if len(path) == n:
                results.append(path)
                return

            for col in range(n):
                if check(path, col):
                    path.append(col)
                    print(path)
                    backtracking()
                    path.pop()
        
        backtracking()
        return len(results)


# @lc code=end

