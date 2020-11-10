from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LCP = 0
        n = len(strs)
        if n == 0:
            return ""
        while True:
            for i in range(0, n):
                if LCP < len(strs[i]) and strs[i][LCP] == strs[0][LCP]:
                    continue
                else:
                    return strs[0][0: LCP]
            LCP += 1


a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))