#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.travelsal(root, val)
        

    def travelsal(self, node, val):
        if node is None:
            return None
        if node.val == val:
            return node
        left_node = self.travelsal(node.left, val)
        right_node = self.travelsal(node.right, val)

        if left_node is not None:
            return left_node
        if right_node is not None:
            return right_node


class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root
        
        if root.val > val: return self.searchBST(root.left, val)
        if root.val < val: return self.searchBST(root.right, val)

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """因为是二叉搜索树，所以搜索路径其实是确定的。不需要遍历整棵树
        """
        while(root is not None):
            if root.val == val: return root
            elif root.val > val: root = root.left  
            else: root = root.right 
        return None
# @lc code=end

