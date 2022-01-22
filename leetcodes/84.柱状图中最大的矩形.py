#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # i, j = 0, len(heights)-1
        # res = -1
        # while(i<=j):
        #     leng = j - i + 1
        #     min_h = min(heights[i:j+1])
        #     cur = min_h * leng
        #     if cur > res:
        #         res = cur
        #     print(i, j, cur)
        #     if heights[i] < heights[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return res
        stack = []
        res = 0
        for i in range(len(heights)):
            while(len(stack)>0 and heights[i] < stack[-1][0]):
                top, left = stack.pop(-1)
                # find left boundary
                while(len(stack)>0 and top == stack[-1]):
                    stack.pop(-1)
                
                if len(stack) > 0:
                    left = stack[-1][1]
                    width = i - left - 1
                else:
                    width = i
                cur = top * width
                if cur > res: res = cur

            stack.append((heights[i], i))
        
        while(len(stack) > 0):
            top, left = stack.pop(-1)
            while(len(stack)>0 and top == stack[-1]):
                stack.pop(-1)
            
            if len(stack) > 0:
                left = stack[-1][1]
                width = len(heights) - left - 1
            else:
                width = len(heights)
            cur = top * width
            if cur > res: res = cur
            
        return res

# @lc code=end

