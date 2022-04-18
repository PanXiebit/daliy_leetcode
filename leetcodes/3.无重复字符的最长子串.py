#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_len = 0

        left = 0
        cur_string = dict()
        for i in range(len(s)):
            cur_len += 1
            while(s[i] in cur_string):
                cur_string.pop(s[left]) # 重点在这里，出现重复时，不断删除最左边的，知道不重复。
                left += 1
                cur_len -= 1
            cur_string[s[i]] = 0
            if cur_len > max_len: max_len = cur_len
        return max_len

                

# @lc code=end

# max_len = 0
#         cur_len = 0
#         left = 0
#         slen = len(s)
#         seen = set()
#         for i in range(slen):
#             cur_len += 1
#             while(s[i] in seen):
#                 seen.remove(s[left])
#                 left += 1
#                 cur_len -= 1
#             seen.add(s[i])
#             if cur_len > max_len: max_len = cur_len
        # return max_len