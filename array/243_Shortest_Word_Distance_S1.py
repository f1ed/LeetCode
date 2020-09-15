from typing import List


def lower_bound(a: list, x: int) -> int:
    n = len(a)
    begin = 0
    end = n - 1
    while begin <= end:
        mid = (begin + end) >> 1
        if a[mid] >= x:
            end = mid
            if begin == end:
                return begin
        else:
            begin += 1
    return -1


class Solution:
    ans = None

    def findShortest(self, li1: list, li2: list) -> None:
        for idx in li1:
            min_dis_idx = lower_bound(li2, idx)
            if min_dis_idx == -1:
                continue
            else:
                self.ans = min(self.ans, li2[min_dis_idx] - idx)
                if self.ans == 1:
                    return

    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        li1 = []
        li2 = []
        self.ans = n
        for idx in range(n):
            # li1 and li2 are ordered
            if words[idx] == word1:
                li1.append(idx)
            if words[idx] == word2:
                li2.append(idx)
        self.findShortest(li1, li2)
        if self.ans > 1:
            self.findShortest(li2, li1)

        return self.ans