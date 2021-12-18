#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        queue = [root]

        while(queue):
            node = queue.pop(0)
            if node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                if node.right is not None:
                    queue.append(node.right)
                
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                if node.left is not None:
                    queue.append(node.left)
        
        return root
            

# @lc code=end

