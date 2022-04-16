#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.travelsal(root, low, high)

    def travelsal(self, root, low, high):
        if root is None:
            return
        print(root.val)
        if root.val >= low and root.val <= high:
            root.left = self.travelsal(root.left, low, high)
            root.right = self.travelsal(root.right, low, high)

        if root.val < low or root.val > high:
            if root.left is None and root.right is None:
                return
            if root.left is None and root.right is not None: 
                return root.right
            if root.right is None and root.left is not None:
                return root.left
            else:
                cur = root.right
                while(cur.left):
                    cur = cur.left

                cur.left = root.left
                root = cur
        return root

# @lc code=end

