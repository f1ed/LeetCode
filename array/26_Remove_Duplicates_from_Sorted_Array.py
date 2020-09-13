from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        tot = 0
        before = None
        for index in range(len(nums)):
            if nums[index] != before:
                nums[tot] = nums[index]
                before = nums[index]
                tot = tot + 1
            else:
                continue

        return tot