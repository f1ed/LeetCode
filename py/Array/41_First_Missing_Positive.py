from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        expect = 1
        for element in nums:
            if element == expect:
                expect += 1
            elif element > expect:
                return expect
        return expect
