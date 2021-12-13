#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        min_depth = 1
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return min_depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            min_depth += 1
        
            


                


# @lc code=end

