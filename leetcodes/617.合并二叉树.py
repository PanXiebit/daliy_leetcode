#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        
        
        p1 = root1
        p2 = root2
        res = TreeNote(0)
        while(p1.)
            

            
        # return root


# @lc code=end

