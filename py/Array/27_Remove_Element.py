from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        tot = 0
        for element in nums:
            if element == val:
                continue
            else:
                nums[tot] = element
                tot = tot + 1
        return tot
