#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        matrix = self.build_matrix(beginWord, wordList)
        flag = [1 for _ in range(len(wordList)+1)]

        for i, word in enumerate(wordList):
            if endWord == word:
                target = i + 1
                break
        
        res = 0
        queue = [0]
        flag[0] = 0
        while(queue):
            size = len(queue)
            for i in range(size):
                row = queue.pop(0)
                # flag[row] = 0
                for col in range(len(matrix)):
                    if flag[col] == 0: continue
                    if matrix[row][col] == 1:
                        queue.append(col)
                        flag[col] = 0
                        if col == target: return res + 2
            res += 1
        return 0


    def build_matrix(self, beginWord, wordList):
        wordList = [beginWord] + wordList
        mat_len = len(wordList)
        matrix = [[0 for _ in range(mat_len)] for _ in range(mat_len)]

        def convert(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                    if diff >= 2: return False
            if diff == 1: return True
            else: return False

        for i in range(mat_len):
            for j in range(i+1, mat_len):
                if convert(wordList[i], wordList[j]):
                    matrix[i][j] = 1
                    matrix[j][i] = 1
        return matrix


# @lc code=end

