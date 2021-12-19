#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        return self.travelsal(root, key)

    def travelsal(self, cur, key):
        if cur is None:
            return
        if cur.val > key:
            cur.left = self.travelsal(cur.left, key)

        if cur.val < key:
            cur.right = self.travelsal(cur.right, key)

        if cur.val == key:
            if cur.left is None and cur.right is None:
                return
            if cur.left is None and cur.right is not None:
                return cur.right
            if cur.left is not None and cur.right is None:
                return cur.left
            else:
                # 找到右子树的最左侧节点
                node = cur.right
                while(node.left):
                    node = node.left

                node.left = cur.left
                cur = cur.right
                return cur
        return cur
        
# @lc code=end

