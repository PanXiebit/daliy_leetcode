#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.num = 0
        self._traversal(root)
        return self.num

    def _traversal(self, cur):
        if cur is None:
            return
        self.num += 1
        self._traversal(cur.left)
        self._traversal(cur.right)
    
# @lc code=end

