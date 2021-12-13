#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # if root is None: return
        # if root.left is not None:
        #     if root.left.val >= root.val:
        #         return False
        #     else:
        #         self.isValidBST(root.left)   
        # if root.right is not None:
        #     print("here")
        #     if root.right.val <= root.val:
        #         print("here")
        #         return False
        #     else:            
        #         self.isValidBST(root.right)
        # return True
        def travelsal(node, vec):
            if node is None:
                return
            travelsal(node.left, vec)
            vec.append(node.val)
            travelsal(node.right, vec)

        vec = []
        travelsal(root, vec)
        print(vec)
        for i in range(1, len(vec)):
            if vec[i] <= vec[i-1]:
                return False
        return True
        

# @lc code=end

