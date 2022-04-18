#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start



class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s

        import numpy as np
        table = np.zeros((len(s), len(s)))

        for i in range(len(s)):
            table[i, i] = 1

        maxLen = 0
        maxPal = ""
        # for i in range(len(s)):
        #     for j in range(len(s)):
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i <= 2: table[i,j] = j-i+1
                    else:
                        if table[i+1, j-1] != 0:
                            table[i,j] = table[i+1, j-1] + 2
                    if table[i,j] == j-i+1:
                        if j - i + 1 > maxLen:
                            maxLen = j - i + 1
                            maxPal = s[i:j+1]
        return maxPal






class Solution2:
    def longestPalindrome(self, s: str) -> str:
        # leng = len(s)

        # dp = [[0 for _ in range(leng)] for _ in range(leng)]
        
        # max_palin = ""
        # max_num = -1
        
        # for i in range(0, leng):
        #     dp[i][i] = True

        # for i in range(leng-1, -1, -1):
        #     for j in range(i, leng):
        #         if s[i] != s[j]:
        #             dp[i][j] = False
        #         else:
        #             if j -i <= 2:
        #                 dp[i][j] = True
        #             else:
        #                 if not dp[i+1][j-1]:
        #                     dp[i][j] = False
        #                 else:
        #                     dp[i][j] = True
                  
        #         if dp[i][j] and (j-i) > max_num:
        #             max_palin = s[i:j+1]
        #             max_num = j-i
        
        # return max_palin

        leng = len(s)
        if leng <= 1: return s

        dp = [[0 for _ in range(leng)] for _ in range(leng)]

        for i in range(0, leng):
            dp[i][i] = 1

        max_palin = s[0]
        max_num = -1 

        for i in range(len(s)-1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2: 
                        dp[i][j] = j - i + 1
                    elif dp[i+1][j-1]: 
                        dp[i][j] = dp[i+1][j-1] + 2
                        
                if dp[i][j] == j -i +1:
                    if j -i + 1 > max_num:
                        max_num = j -i + 1
                        max_palin = s[i:j+1]
        
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
