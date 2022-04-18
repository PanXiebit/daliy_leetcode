#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while(cur):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


class Solution1:
    # def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        pre = None
        cur = head

        while(cur is not None):
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        return pre
            
        

# @lc code=end

