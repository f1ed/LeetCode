from typing import List


# Solution 1: Easy Solution

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        a = [0] * length
        for index in range(length):
            a[(index + k) % length] = nums[index]
        nums[:] = a[:]
