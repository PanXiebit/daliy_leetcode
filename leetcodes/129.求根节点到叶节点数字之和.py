#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None: return 0
        return self.sum(root, 0)

    def sum(self, root, val):
        if root is None: return 0
        tmp = val * 10 + root.val

        if root.left is None and root.right is None:
            return tmp
        left = self.sum(root.left, tmp)
        right = self.sum(root.right, tmp)
        return left + right

# @lc code=end

