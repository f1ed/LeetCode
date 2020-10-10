class Solution:
    def reverse(self, x: int) -> int:
        n_min = -(2 ** 31)
        n_max = 2 ** 31 - 1
        s = 0
        flag = True
        if x < 0:
            flag = False
            x = -x
        while x != 0:
            r = x % 10
            s = s * 10 + r
            x //=10
        if flag is False:
            s = -s
        if s < n_min or s > n_max:
            return 0
        return s

a = Solution()
print(a.reverse(-0))
