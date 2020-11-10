from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c_bit = 0
        n = len(digits)
        i = n - 1
        digits[i] += 1
        while i >= 0:
            if digits[i] < 10:
                break
            digits[i] %= 10
            if i == 0:
                c_bit = 1
            else:
                digits[i-1] += 1
            i -= 1
        if c_bit == 1:
            digits.insert(0, c_bit)
        return digits

a = Solution()
digits = [0]
ans = a.plusOne(digits)
for i in ans:
    print(i)