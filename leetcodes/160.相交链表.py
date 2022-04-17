#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        map = dict()
        p = headA
        q = headB
        while(p != None or q!= None):
            if p:
                if p in map: return p
                else:
                    map[p] = 0
                    p = p.next
            if q:
                if q in map: return q
                else:
                    map[q] = 0
                    q = q.next
        return None
        
# @lc code=end

