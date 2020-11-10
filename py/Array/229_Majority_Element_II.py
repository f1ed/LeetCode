from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = {}
        ans = []
        for ele in nums:
            if ele in cnt:
                cnt[ele] += 1
            else:
                cnt[ele] = 1
        for (k, v) in cnt.items():
            if v > n/3:
                ans.append(k)
        return ans
