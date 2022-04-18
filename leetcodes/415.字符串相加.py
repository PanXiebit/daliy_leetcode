#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p = len(num1) - 1
        q = len(num2) - 1
        res = []
        tmp = 0
        while(p>= 0 and q >= 0):
            cur = int(num1[p]) + int(num2[q]) + tmp
            res.insert(0, str(cur % 10))
            if cur >= 10:
                tmp = 1
            else:
                tmp = 0
            p -= 1
            q -= 1
        res = "".join(res)
        if tmp == 0:
            if p < 0 and q >= 0:
                res = num2[:q+1] + res
            if p >= 0 and q < 0:
                res = num1[:p+1] + res
        else:
            if p < 0 and q >= 0:
                res = num2[:q] + str(int(num2[q]) + 1) +  res
            if p >= 0 and q < 0:
                res = num1[:p+1] + str(int(num1[p]) + 1) + res
        return res

            
            

# @lc code=end

