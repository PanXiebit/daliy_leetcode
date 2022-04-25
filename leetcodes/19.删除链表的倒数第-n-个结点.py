#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None: return None

        q = head
        p = head
        for i in range(n):
            q = q.next
        if q == None: return head.next

        while(q.next):
            q = q.next
            p = p.next
        p.next = p.next.next
        return head

        
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nums = 0
        p = head
        while(p):
            nums += 1
            if p.next == None: break
            p = p.next
        m = nums - n + 1
        if m == 1: return head.next

        q = head
        for i in range(1, m-1):
            q = q.next
        q.next = q.next.next
    
        return head
        
# @lc code=end

