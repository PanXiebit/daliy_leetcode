#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        

class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sum = 0
        return self.traserval(root, targetSum)

    def traserval(self, cur, targetSum):
        if cur is None:
            return False
        self.sum += cur.val

        if cur.left is None and cur.right is None:
            if self.sum == targetSum: return True
            self.sum -= cur.val
            return False
        
        if self.traserval(cur.left, targetSum): return True
        if self.traserval(cur.right, targetSum): return True
        self.sum -= cur.val
        return False
                
# @lc code=end

