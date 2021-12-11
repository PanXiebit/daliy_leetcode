#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = [root]
        if root is None:
            return 0

        max_detph = 1
        while(queue):
            flag = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                print("cur_node: ", node.val)
                if node.left is not None:
                    queue.append(node.left)
                    flag = 1
                if node.right is not None:
                    queue.append(node.right)
                    flag = 1
            if flag == 0:
                return max_detph
            max_detph += 1
        return max_detph

# @lc code=end

