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
    # def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        pre = None
        cur = head
        # nxt = head

        # while(cur != None):
        #     nxt = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = nxt
        # return pre
        while(cur is not None):
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        return pre
            
        

# @lc code=end

