from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = {}
        for ele in nums:
            if ele in cnt:
                cnt[ele] += 1
            else:
                cnt[ele] = 1
        return max(cnt, key=cnt.get)