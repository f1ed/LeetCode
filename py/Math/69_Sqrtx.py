class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x+0.5))

a = Solution()
print(a.mySqrt(1))