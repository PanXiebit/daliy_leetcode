#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        p = head
        q = head.next

        dup_num = 0
        while(q):
            if q.val == p.val:
                dup_num += 1
                q = q.next
            else:
                if dup_num != 0:
                    p.next = q
                    dup_num = 0
                p = p.next
                q = q.next




# @lc code=end

