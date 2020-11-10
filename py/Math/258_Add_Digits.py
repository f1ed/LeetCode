class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while num:
            mod = num % 10
            ans += mod
            if ans >= 10:
                ans %= 10
                ans += 1
            num //= 10
        return ans

if __name__ == '__main__':
    x = Solution()
    print(x.addDigits(13456))