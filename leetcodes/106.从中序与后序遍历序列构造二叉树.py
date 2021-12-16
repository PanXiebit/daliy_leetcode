#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        return self.travelsal(inorder, postorder)

    def travelsal(self, inorder, postorder):
        if len(inorder) == 0: return None
        root_val = postorder[-1]
        root = TreeNode(root_val)

        for id in range(len(inorder)):
            if inorder[id] == root_val:
                break
        
        leftInorder = inorder[:id]
        rightInorder = inorder[id+1:]

        leftPostorder = postorder[:len(leftInorder)]
        rightPostorder = postorder[len(leftInorder):-1]

        root.left = self.travelsal(leftInorder, leftPostorder)
        root.right = self.travelsal(rightInorder, rightPostorder)
        return root

# @lc code=end

