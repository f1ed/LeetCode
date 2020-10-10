class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        li1 = version1.split('.')
        li2 = version2.split('.')
        n_1 = len(li1)
        n_2 = len(li2)
        n = max(n_1, n_2)
        for i in range(n):
            a = int(li1[i]) if i < n_1 else 0
            b = int(li2[i]) if i < n_2 else 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

a = Solution()
v1 = "7.5.3.001"
v2 = "7.5.3"
print(a.compareVersion(v1, v2))
