#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        ip = []
        def backtracing(idx, ip, results):
            if len("".join(ip)) == len(s) and len(ip) == 4:
                results.append(".".join(ip.copy()))
                return

            if idx > len(s)-1 or len(ip) >= 4:
                return

            if int(s[idx]) >= 0:
                ip.append(s[idx])
                backtracing(idx+1, ip, results)
                ip.pop()
            if int(s[idx]) != 0 and idx+2 <= len(s) and int(s[idx:idx+2]) > 0 and int(s[idx:idx+2]) < 256:
                ip.append(s[idx:idx+2])
                backtracing(idx+2, ip, results)
                ip.pop()
            if int(s[idx]) != 0 and idx+3 <= len(s) and int(s[idx:idx+3]) > 0 and int(s[idx:idx+3]) <256:
                ip.append(s[idx:idx+3])
                backtracing(idx+3, ip, results)
                ip.pop()


        backtracing(0, ip, results)

        return results


# @lc code=end

