#
# @lc app=leetcode.cn id=1300 lang=python3
#
# [1300] 转变数组后最接近目标值的数组和
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        # print(arr)

        pre_sum = 0
        for idx in range(len(arr)):
            cur_val = pre_sum + (len(arr)-idx) * arr[idx]
            
            if cur_val == target:
                return arr[idx]

            if cur_val > target:
                left_sum = target - pre_sum
                ans = left_sum // (len(arr)-idx)
                if (ans * (len(arr)-idx) + pre_sum -target) + ((ans+1) * (len(arr)-idx) + pre_sum -target) <0:
                    return (ans+1)
                else:
                    return ans

            pre_sum += arr[idx]
        return arr[-1]  

# @lc code=end

