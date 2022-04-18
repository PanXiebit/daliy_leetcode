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
        res = []
        stack = []
        cur = root
        while (cur is not None or len(stack) > 0):
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                res.append(cur.val)
                cur = cur.right
        return res


        
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traversal(root, res)
        return res
    
    def traversal(self, root, res):
        if root is None: return
        self.traversal(root.left, res)
        res.append(root.val)
        self.traversal(root.right, res)

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    
    #    递归法
    #     res = []

    #     self.travelsal(root, res)
    #     return res

    # def travelsal(self, cur, res):
    #     if cur is None:
    #         return
    #     self.travelsal(cur.left, res)
    #     res.append(cur.val)
    #     self.travelsal(cur.right, res)

        res = []
        stack = []
        cur = root
        while(cur is not None or stack):
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                res.append(cur.val)
                cur = cur.right
        return res

# @lc code=end

