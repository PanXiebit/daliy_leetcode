#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        import numpy as np

        results = []
        path = []

        def _can_site(path, col):
            if col in path: # 如果第i列已经放了，那么这一列就不能放了
                return False
            m = len(path) # 现在需要放在第m行了
            for j in range(m):
                if abs(j - m) == abs(path[j] - col):
                    return False
            return True           


        def backtracking():
            print("backtracking-------")
            if len(path) == n:
                results.append(path.copy())
                return

            for col in range(n):
                """每一行只能放一个，所以只需要考虑每一行放在哪一列就好了
                   所以这里的for循环是对每一行都遍历一遍其所有的列
                """
                if _can_site(path, col):
                    path.append(col)
                    print(path)
                    backtracking() 
                    # 这里的回溯是指的，对这一行找到了可以放的列，然后探索下一行的所有列。
                    # 如果达到了终止条件，那就返回结果了
                    # 如果没达到，就是把n行

                    a = path.pop()
                    print("pop: ", a)

        backtracking()

        def int2str(id):
            tmp = ["."]*n
            tmp[id] = "Q"
            return "".join(tmp)

        def convert_to_string(results):
            str_res = []
            for res in results:
                str_res.append([int2str(id) for id in res])
            return str_res

        return convert_to_string(results)

"""有一个疑问，就是我这里每次backtracking是遍历所有的列，但是这个棋盘的行数怎么确定的呢？
   backtracking一直探索下去，就是行数，也就是 path 的长度。但是这个长度一定不会超过n，
   原因就是符合n皇后规则的情况下，不可能超过n，所以到了某一行之后，
   下一个backtracking一定是所有的n列都不符合，所以会依次把他们全部pop出来。


   所以n皇后总结下来就是：
   1. 进入 backtracking
   2. 有条件的循环所有的列（注意这里的有条件，在组合问题里是startindex,在这题里是_can_site）
        2.0 处理节点
        2.1 bachtracking，也就是递归查找下一行的列
        2.2 回溯，撤销处理

    所以回溯问题是：一个for循环下，嵌套了很多for循环。
    类似于那个树状结构，第一层循环就是所有的元素，也就是宽度，深度就是backtracking的次数，
    - 在n皇后的问题里这个因为规则限制了不会超过n
    - 在组合问题里，for(startIndex, n + 1), startindex 是增加的，所以也不会超过n
"""
        
# @lc code=end
        