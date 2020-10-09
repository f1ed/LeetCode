from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        S = set()
        for i in nums:
            if i in S:
                return True
            S.add(i)
        return False