#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.travelsal(root, p, q)

    def travelsal(self, cur, p, q):
        if cur is None:
            return
        
        if cur is p or cur is q:
            return cur

        if cur.val > p.val or cur.val > q.val:
            left = self.travelsal(cur.left, p, q)
        else:
            left = None

        if cur.val < p.val or cur.val < q.val:
            right = self.travelsal(cur.right, p, q)
        else:
            right = None
        # left = self.travelsal(cur.left, p, q)
        # right = self.travelsal(cur.right, p, q)

        
        if left is not None and right is not None:
            return cur
        if left is not None:
            return left
        if right is not None:
            return right
        


# @lc code=end

