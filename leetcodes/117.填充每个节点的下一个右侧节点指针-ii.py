#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        queue = [root]
        while(queue):
            size = len(queue)
            level_node = []
            for _ in range(size):
                node = queue.pop(0)
                level_node.append(node)
                if node.left is not None: queue.append(node.left)
                if node.right is not None: queue.append(node.right)
            for i in range(len(level_node)-1):
                level_node[i].next = level_node[i+1]
            level_node[-1].next = None
        return root
# @lc code=end

