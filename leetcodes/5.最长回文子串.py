#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        leng = len(s)

        dp = [[0 for _ in range(leng)] for _ in range(leng)]
        
        max_palin = ""
        max_num = -1
        
        for i in range(0, leng):
            dp[i][i] = True

        for i in range(leng-1, -1, -1):
            for j in range(i, leng):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j -i <= 2:
                        dp[i][j] = True
                    else:
                        if not dp[i+1][j-1]:
                            dp[i][j] = False
                        else:
                            dp[i][j] = True
                  
                if dp[i][j] and (j-i) > max_num:
                    max_palin = s[i:j+1]
                    max_num = j-i
        
        return max_palin
                
# @lc code=end

   # def is_palindrome(self, s):
    #     if len(s) <= 1:
    #         return True
    #     i = 0
    #     j = len(s) - 1
    #     while(i <= j):
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True
