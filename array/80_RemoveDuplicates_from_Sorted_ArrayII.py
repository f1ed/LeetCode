from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        before = None
        before_cnt = 0
        length = 0
        for index in range(len(nums)):
            if nums[index] != before:
                nums[length] = nums[index]
                before = nums[index]
                length += 1
                before_cnt = 1
            else:
                before_cnt += 1
                if before_cnt <= 2:
                    nums[length] = nums[index]
                    length += 1
        return length

