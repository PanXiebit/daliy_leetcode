#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]

        res = []
        while(queue):
            size = len(queue)
            level_res = []
            for i in range(size):
                node = queue.pop(0)
                level_res.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(level_res)
        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []

        if root is None:
            return []
            
        while(queue):
            level_res = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level_res.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(level_res)

        return res
# @lc code=end

