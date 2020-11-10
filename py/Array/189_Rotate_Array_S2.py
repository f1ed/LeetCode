from typing import List
import queue


# Solution 2: Cyclic Replacement


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        start = 0
        cnt = 0
        while cnt < length:
            current, prev = start, nums[start]
            while True:
                current = (current + k) % length
                prev, nums[current] = nums[current], prev
                cnt += 1
                if current == start:
                    break
            start += 1
