from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        begin = 0
        end = n - 1
        while begin <= end:
            mid = (begin + end) >> 1
            h = n - mid
            if citations[mid] >= h:
                end = mid
                if begin == end:
                    return h
            else:
                begin += 1
        return n - begin
