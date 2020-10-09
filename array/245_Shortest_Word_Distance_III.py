from typing import List


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        ptr1 = None
        ptr2 = None
        ans = n
        if word1 == word2:
            for idx in range(n):
                if words[idx] == word1:
                    ptr1, ptr2 = idx, ptr1
                if (ptr1 is not None) and (ptr2 is not None):
                    ans = min(ans, ptr1-ptr2)
        else:
            for idx in range(n):
                if words[idx] == word1:
                    ptr1 = idx
                if words[idx] == word2:
                    ptr2 = idx
                if (ptr1 is not None) and (ptr2 is not None):
                    ans = min(ans, abs(ptr1-ptr2))
        return ans

words = ["b", "a", "b", "c"]
word1 = "b"
word2 = "b"
a = Solution()
print(a.shortestWordDistance(words, word1, word2))
