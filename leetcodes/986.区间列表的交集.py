#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f, s = 0, 0

        res = []
        while(f < len(firstList) and s< len(secondList)):
            cur1 = firstList[f]
            cur2 = secondList[s]
            print(f,s, cur1, cur2)

            # 无交集
            if cur1[1] < cur2[0]:
                f += 1
            elif cur2[1] < cur1[0]:
                s += 1
            else:
                if cur1[1] >= cur2[1]:
                    res.append([max(cur2[0], cur1[0]), cur2[1]])
                    s += 1
                else:
                    res.append([max(cur2[0], cur1[0]), cur1[1]])
                    f += 1
        return res



# @lc code=end

