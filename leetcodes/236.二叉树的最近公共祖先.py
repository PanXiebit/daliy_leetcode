#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
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

        left = self.travelsal(cur.left, p, q)
        right = self.travelsal(cur.right, p, q)

        if left is not None and right is not None:
            return cur

        if left is not None:
            return left
        
        if right is not None:
            return right
    #     return self.travelsal(root, p, q)


    # def travelsal(self, cur, p, q):
        
    #     if cur is None:
    #         return None
    #     print("before: ", cur.val)
    #     if cur is p or cur is q:
    #         print("stop: ", cur.val)
    #         return cur

    #     left = self.travelsal(cur.left, p, q)
    #     right = self.travelsal(cur.right, q, q)

    #     print("after: ", cur.val)
    #     if left is not None and right is not None:
    #         return cur
    #     if left is not None:
    #         return left
    #     if right is not None:
    #         return right
    #     else:
    #         return None


# @lc code=end

