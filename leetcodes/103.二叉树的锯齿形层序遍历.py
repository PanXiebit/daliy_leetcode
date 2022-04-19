#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

1
                    
        

class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        queue = [root]
        if root is None: return []

        count = 0
        while(queue):
            level_res = []
            size = len(queue)
            for i in range(size):
                if count % 2 == 0:
                    node = queue.pop(0)
                    level_res.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                else:
                    node = queue.pop(-1)
                    level_res.append(node.val)
                    if node.right: queue.insert(0, node.right)
                    if node.left: queue.insert(0, node.left)
            count += 1
            res.append(level_res.copy())
        return res
        

# @lc code=end

