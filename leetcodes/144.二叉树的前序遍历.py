#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
    # 迭代法，使用栈的原因是，栈是后进先出，所以可以做到深度优先
        res = []
        stack = [root]
        if root is None:
            return []
        while(stack):
            cur = stack.pop(-1)
            res.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)
        return res 

# @lc code=end

