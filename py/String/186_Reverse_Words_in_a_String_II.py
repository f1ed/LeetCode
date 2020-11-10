from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = s[-1::-1]
        n = len(temp)
        i = 0
        while i < n:
            l = i
            while i < n and temp[i] != ' ':
                i += 1
            r = i
            temp[l:r] = list(reversed(temp[l:r]))

            i += 1
        for index in range(n):
            s[index] = temp[index]


a = Solution()
a.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])

