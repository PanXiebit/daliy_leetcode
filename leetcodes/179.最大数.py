#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # sorted_num = sorted(nums, key=lambda num: str(num), reverse=True)

        class mycompare(object):
            def __init__(self, x):
                self.x = str(x)
            
            def __gt__(self, y):
                return int(self.x + y.x) > int(y.x + self.x)
        
        sorted_num = sorted(nums, key=lambda num: mycompare(num), reverse=True)
        

        
        res =  "".join(map(str, sorted_num))
        if "0" == res[0]: return "0"
        else: return res

# @lc code=end

