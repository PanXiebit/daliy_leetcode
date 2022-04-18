#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float("-inf")
        self.curMax(root)
        return self.max_val
    
    def curMax(self, root):
        if root is None: return 0

        
        left = max(self.curMax(root.left), 0)
        right = max(self.curMax(root.right), 0)
        
        self.max_val = max(left + right + root.val, self.max_val)
        return max(left, right) + root.val

# @lc code=end

