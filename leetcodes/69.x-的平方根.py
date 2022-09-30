#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        left = 0
        right = x//2
        while(left <= right):
            mid = (left + right) // 2
            if mid ** 2 == x: return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right  
        

class Solution2:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        l = 0
        h = x
        while( l < h):
            middle = (l + h) // 2
            if middle ** 2 > x:
                h = middle
            else:
                if (middle+1)**2 > x:
                    return middle
                else:
                    l = middle
        return middle
        
# @lc code=end

