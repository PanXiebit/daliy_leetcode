#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [(root, True)]
        res = -1
        while(len(queue) != 0):
            size = len(queue)
            print("size: ", size)
            for i in range(size):
                node, is_left = queue.pop(0)
                if i == 0 and is_left:
                    res = node.val
                if node.left is not None: queue.append((node.left, True))
                if node.right is not None: queue.append((node.right, True))
        
        return res
# @lc code=end

