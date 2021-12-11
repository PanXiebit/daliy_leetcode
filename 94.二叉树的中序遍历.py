#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    
    #    递归法
        res = []

        self.travelsal(root, res)
        return res

    def travelsal(self, cur, res):
        if cur is None:
            return
        self.travelsal(cur.left, res)
        res.append(cur.val)
        self.travelsal(cur.right, res)






# @lc code=end

