#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
    
    # 递归法
        res = []
        self.travelsal(root, res)
        return res

    def travelsal(self, cur, res):
        if cur is None:
            return
        self.travelsal(cur.left, res)
        self.travelsal(cur.right, res)
        res.append(cur.val)

 


# @lc code=end

