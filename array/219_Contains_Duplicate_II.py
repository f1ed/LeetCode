from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dict:
                dict.setdefault(nums[i], i)
            else:
                if i - dict[nums[i]] <= k:
                    return True
                dict[nums[i]] = i
        return False
