from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        median1 = median2 = None
        i = j = 0
        tot = 0
        while i < n1 or j < n2:
            if (i < n1 and j < n2 and nums1[i] <= nums2[j]) or (i < n1 and j >= n2):
                tot += 1
                if tot == (n1 + n2)//2:
                    median1 = nums1[i]
                if tot == (n1 + n2)//2 + 1:
                    median2 = nums1[i]
                    break
                i += 1
            else:
                tot += 1
                if tot == (n1 + n2) // 2:
                    median1 = nums2[j]
                if tot == (n1 + n2) // 2 + 1:
                    median2 = nums2[j]
                    break
                j += 1
        if (n1 + n2) % 2 == 1:
            return median2
        else:
            return (median1 + median2)/2

a = Solution()
nums1 = [2, 5]
nums2 = [1, 2]
print(a.findMedianSortedArrays(nums1, nums2))


