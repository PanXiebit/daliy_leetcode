#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 超时的方法
        # if root is None:
        #     return True
        # queue = [root]
        # while(len(queue) != 0):
        #     level_val = []
        #     size = len(queue)
        #     flag = 0
        #     for _ in range(size):
        #         node = queue.pop(0)
        #         level_val.append(node.val)
        #         if node.left is not None:
        #             queue.append(node.left)
        #             flag = 1
        #         else:
        #             queue.append(TreeNode(-1))
        #         if node.right is not None:
        #             queue.append(node.right)
        #             flag = 1
        #         else:
        #             queue.append(TreeNode(-1))
        #     if level_val != level_val[::-1]:
        #         return False
        #     if flag == 0:
        #         break
        # return True

        # 迭代法
        # if root is None:
        #     return True
        
        # queue = []
        # queue.append(root.left)
        # queue.append(root.right)

        # while(queue):
        #     print("queue1: ", len(queue))
        #     left_node = queue.pop(0)
        #     right_node = queue.pop(0)
        #     if left_node is None and right_node is None:
        #         continue
            
        #     if left_node is None or right_node is None:
        #         return False
        #     else:
        #         if left_node.val != right_node.val:
        #             return False
        #     queue.append(left_node.left)
        #     queue.append(right_node.right)
        #     queue.append(left_node.right)
        #     queue.append(right_node.left)
        #     print("queue2: ", len(queue))
        # return True

        # 递归法
        if root is None:
            return True
        return self.compare(root.left, root.right)


    def compare(self, left_node, right_node):
        if left_node is None and right_node is None:
            return True
        elif left_node is None or right_node is None:
            return False
        elif left_node.val != right_node.val:
                return False

        outside = self.compare(left_node.left, right_node.right)
        inside = self.compare(left_node.right, right_node.left)
        return outside & inside
     
# @lc code=end

