#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        radiant = []
        dire = []

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)


        while(True):
            if len(radiant) == 0:
                return "Dire"
            if len(dire) == 0:
                return "Radiant"
            
            if radiant[0] < dire[0]:
                dire.pop(0)
                radiant.append(radiant.pop(0) + len(senate))
            else:
                radiant.pop(0)
                dire.append(dire.pop(0) + len(senate))
        

# @lc code=end

