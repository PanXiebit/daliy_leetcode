#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        cur = head
        while(cur):
            nums.append(cur.val)
            cur = cur.next
        
        return self.isPalindromenum(nums)

    def isPalindromenum(self, nums):
        i, j = 0, len(nums) -1
        while(i <= j):
            if nums[i] != nums[j]:
                return False
            else:
                i += 1
                j -= 1
        return True     

# @lc code=end

