#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        return self.isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) \
            or self.isSubtree(root.right, subRoot)

    def isSametree(self, a, b):
        if not a and not b: return True
        if not a or not b: return False

        return a.val == b.val and self.isSametree(a.left, b.left) and \
            self.isSametree(a.right, b.right)
        

# @lc code=end

