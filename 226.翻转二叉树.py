#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
    # 递归法
    #     self.travelsal(root)
    #     return root
    
    # def travelsal(self, cur):
    #     if cur is None:
    #         return
    #     tmp = cur.left
    #     cur.left = cur.right
    #     cur.right = tmp
    #     self.travelsal(cur.left)
    #     self.travelsal(cur.right)

    # 迭代法

        if root is None:
            return None
        queue = [root]
        while(queue):
            cur = queue.pop(0)
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return root


        

# @lc code=end

