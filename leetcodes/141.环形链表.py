#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None or head.next.next == None: return False
        p = q = head
        while(q!= None and q.next != None):
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False


        
# @lc code=end

