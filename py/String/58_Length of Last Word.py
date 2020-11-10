class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        length = 0
        end = n-1
        while end-1 >= 0 and s[end] == ' ':
            end -= 1
        for i in range(end, -1, -1):
            if s[i] == ' ':
                return length
            else:
                length += 1
        return length

a = Solution()
print(a.lengthOfLastWord("hell   a  ada  "))