#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
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
    def maxDepth(self, root: 'Node') -> int:
        return self.travelsal(root)

    def travelsal(self, cur):
        if cur is None:
            return 0
        cur_depths = []
        if len(cur.children) == 0:
            return 1
        for node in cur.children:
            cur_depths.append(self.travelsal(node))
        return 1 + max(cur_depths)
        
# @lc code=end

