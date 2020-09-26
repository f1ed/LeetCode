class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1 = len(haystack)
        n2 = len(needle)
        for i in range(0, n1-n2+1):
            if haystack[i:i+n2] == needle:
                return i
        return -1