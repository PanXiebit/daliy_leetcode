#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        
        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(1, s_len - p_len + 1):
            s_count[ord(s[i-1]) - 97] -= 1
            s_count[ord(s[i+p_len-1]) - 97] += 1
            
            if s_count == p_count:
                ans.append(i)

        return ans

# @lc code=end


              




    #     from collections import defaultdict
    #     p_len = len(p)
    #     p_dict = defaultdict(int)
    #     for c in p:
    #         p_dict[c] += 1

    #     res = []
    #     for i in range(len(s)-p_len+1):
    #         if self.isAnagrams(s[i: i+p_len], p_dict.copy()):
    #             res.append(i)
    #     return res

    # def isAnagrams(self, q, p_dict):
    #     for c in q:
    #         if c not in p_dict:
    #             return False
    #         else:
    #             p_dict[c] -= 1
    #             if p_dict[c] == 0:
    #                 p_dict.pop(c)
    #     if len(p_dict) == 0:
    #         return True
    #     else:
    #         return False
