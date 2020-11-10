class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        dic = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        rev = [0] * n
        for index in range(n):
            if s[index] in dic or s[index].lower() in dic:
                rev[index] = 1
        l = 0
        r = n - 1
        while l < r:
            while l < r and rev[l] == 0:
                l += 1
            while l < r and rev[r] == 0:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)

a = Solution()
print(a.reverseVowels("hello"))
