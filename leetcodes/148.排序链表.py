#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None): return head

        slow = head
        fast = head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while (l1 and l2):
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        if l1: tail.next = l1
        if l2: tail.next = l2
        return dummy.next
        

        






# @lc code=end

