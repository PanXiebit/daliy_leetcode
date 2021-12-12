#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self) -> None:
#         self.res = 0

#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
#         self.travelsal(root, False)
#         return self.res
    
#     def travelsal(self, cur, is_left):
#         if cur is None:
#             return
#         if cur.left is None and cur.right is None and is_left:
#             self.res += cur.val
#         self.travelsal(cur.left, True)
#         self.travelsal(cur.right, False)

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue = [(root, False)]
        res = 0

        while(len(queue)!= 0):
            node, is_left = queue.pop(0)

            if node.left is None and node.right is None and is_left:
                res += node.val
            if node.left is not None: queue.append((node.left, True))
            if node.right is not None: queue.append((node.right, False))

        return res

# @lc code=end

