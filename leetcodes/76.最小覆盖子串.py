#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need  = defaultdict(int)
        for c in t:
            need[c] += 1
        print("need: ", need)
        total = need.copy()

        i = j = 0
        for c in s:
            print("c: ", c)
            if c in total:
                total[c] -= 1
                print(c, need, total)
            if c in need:
                need[c] -= 1
                if need[c] == 0:
                    need.pop(c)
                if len(need) == 0:
                    break
            j += 1


        for c in t:
            if total[c] == 0:
                total.pop(c)

        for c in s:
            if len(total) == 0:
                break
            if c in total:
                total[c] += 1
                if total[c] == 0:
                    total.pop(c)
            i += 1
                
        return s[i:j+1]
        
# @lc code=end

