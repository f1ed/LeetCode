from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        lst1 = None
        lst2 = None
        ans = n
        for idx in range(n):
            if words[idx] == word1:
                lst1 = idx
                if lst2 is not None:
                    ans = min(ans, lst1-lst2)
            if words[idx] == word2:
                lst2 = idx
                if lst1 is not None:
                    ans = min(ans, lst2-lst1)
        return ans