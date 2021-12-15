#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
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
#         self.max_val, self.max_num = [], -1
#         self.prev_val = float("-inf")
#         self.cur_num = 0

#     def findMode(self, root: TreeNode) -> List[int]:
        
#         def travelsal(node):
#             if node is None:
#                 return
#             travelsal(node.left)
            
#             if node.val == self.prev_val:
#                 self.cur_num += 1
#             elif node.val > self.prev_val:
#                 self.cur_num = 1
#                 self.prev_val = node.val

#             if self.cur_num > self.max_num:
#                 self.max_num = self.cur_num
#                 self.max_val.clear()
#                 self.max_val.append(node.val)
#             elif self.cur_num == self.max_num:
#                 self.max_num = self.cur_num
#                 self.max_val.append(node.val)

#             travelsal(node.right)

#         travelsal(root)
#         return self.max_val


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        stack = []
        cur = root

        prev_val = float("-inf")
        cur_num = 0
        max_val = []
        max_num = -1

        while(cur is not None or stack):
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                if cur.val > prev_val:
                    prev_val = cur.val
                    cur_num = 1
                elif cur.val == prev_val:
                    cur_num += 1

                if cur_num > max_num:
                    max_num = cur_num
                    max_val.clear()
                    max_val.append(cur.val)
                elif cur_num == max_num:
                    max_val.append(cur.val)

                cur = cur.right

        return max_val


# @lc code=end

