#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [root]
        res = []

        if root is None:
            return []
            
        while(queue):
            level_res = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level_res.append(node.val)
                if node.children is not None:
                    queue.extend(node.children)
            res.append(level_res)
        return res
# @lc code=end

