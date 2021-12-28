#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None: return 
        fast = slow = head

        while (fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
            if fast  == slow:
                break
        
        if fast.next is None or fast.next.next is None:
            return 
        else:
            slow2 = head
            step = 0
            while(slow2 != slow):
                slow2 = slow2.next
                slow = slow.next
                step += 1
            print(slow.val)
            return slow


# @lc code=end

