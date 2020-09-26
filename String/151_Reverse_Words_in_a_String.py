class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        li = []
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            l = i
            while i < n and s[i] != ' ':
                i += 1
            r = i
            if r != l:
                li.append(s[l:r])

        ans = ' '.join(li[-1::-1])
        return ans

a = Solution()
print(a.reverseWords("a good   example"))
