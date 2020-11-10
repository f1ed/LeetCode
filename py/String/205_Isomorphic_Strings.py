class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        dic = {}
        vSet = set()  # satisfy single map
        for idx in range(n):
            ch = s[idx]
            # single map
            if ch not in dic and t[idx] not in vSet:
                dic[ch] = t[idx]
                vSet.add(t[idx])
                continue
            if ch in dic and dic[ch] == t[idx]:
                continue
            return False
        return True

a = Solution()
if a.isIsomorphic("ab", "aa"):
    print("true")
else:
    print("false")