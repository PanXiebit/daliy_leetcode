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
        # 迭代法
        # queue = [root]
        # if root is None:
        #     return 0

        # max_detph = 1
        # while(queue):
        #     flag = 0
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         print("cur_node: ", node.val)
        #         if node.left is not None:
        #             queue.append(node.left)
        #             flag = 1
        #         if node.right is not None:
        #             queue.append(node.right)
        #             flag = 1
        #     if flag == 0:
        #         return max_detph
        #     max_detph += 1
        # return max_detph

        # 递归法
        depth = self.traversal(root)
        return depth

    def traversal(self, cur):
        if cur is None: return 0
        ldepth = self.traversal(cur.left)
        rdepth = self.traversal(cur.right)
        depth =  1 + max(ldepth, rdepth)
        return depth

# @lc code=end

