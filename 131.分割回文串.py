#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        path = []

        def backtrack(s, startIndex):
            if len("".join(path)) == len(s):
                results.append(path.copy())
                print("results: ", results)
                return

            for i in range(startIndex, len(s)):
                cur_s = s[startIndex: i + 1]
                print("cur_s: ",cur_s, startIndex, i)
                if self.is_palindrome(cur_s):
                    path.append(cur_s)
                    print("path: ", path)
                    backtrack(s, i+1)
                    pop_s = path.pop()
                    print("pop: ", pop_s)

                
        backtrack(s, 0)
        return results

    def is_palindrome(self, s):
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

# @lc code=end


        
        
