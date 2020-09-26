class Solution:
    def firstUniqChar(self, s: str) -> int:
        a_ascii = ord('a')
        cnt = [0]*(26+5)
        for i in s:
            cnt[ord(i)-a_ascii] += 1
        for idx in s:
            if cnt[ord(i)-a_ascii] == 1:
                return s.index(i)
        return -1

a = Solution()
print(a.firstUniqChar("llu"))