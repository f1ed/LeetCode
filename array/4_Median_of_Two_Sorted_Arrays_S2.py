from typing import List


class Solution:
    def __init__(self):
        self.nums1 = None
        self.nums2 = None

    def findKthOfTwo(self, l1: int, l2: int, k: int) -> int:
        nums1 = self.nums1
        nums2 = self.nums2
        n = len(nums1)
        m = len(nums2)
        # nums1 is empty
        if l1 == n:
            return nums2[l2+k-1]
        # nums2 is empty
        if l2 == m:
            return nums1[l1+k-1]
        # both not empty
        if k == 1:
            return nums1[l1] if nums1[l1] <= nums2[l2] else nums2[l2]
        # to avoid the rest length of nums1/nums2 is shorter than k//2
        k1 = k//2 if l1+k//2 <= n else n-l1
        k2 = k//2 if l2+k//2 <= m else m-l2
        if nums1[l1+k1-1] == nums2[l2+k2-1]:
            return nums1[l1+k1-1] if k-k1-k2 == 0 else self.findKthOfTwo(l1+k1, l2+k2, k-k1-k2)
        elif nums1[l1+k1-1] > nums2[l2+k2-1]:
            return self.findKthOfTwo(l1, l2+k2, k-k2)
        else:
            return self.findKthOfTwo(l1+k1, l2, k-k1)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        self.nums1 = nums1
        self.nums2 = nums2
        # median: the average of (n+m+1)//2 th  and  (n+m+2)//2 th
        return (self.findKthOfTwo(0, 0, (n+m+1)//2) + self.findKthOfTwo(0, 0, (n+m+2)//2)) / 2

a = Solution()
nums1 = [2,3,9]
nums2 = [6,7]
print(a.findMedianSortedArrays(nums1, nums2))
