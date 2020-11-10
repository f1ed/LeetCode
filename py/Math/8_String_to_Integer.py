class Solution:
    def is_digit(self, ch: str) -> bool:
        c = ch[0]
        if ord('0') <= ord(c) <= ord('9'):
            return True
        return False

    def is_out_of_range(self, x: int) -> bool:
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1
        if x < INT_MIN or x > INT_MAX:
            return True
        return False

    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n or (s[i] is not '+' and s[i] is not '-' and self.is_digit(s[i]) is False):
            return 0

        is_neg = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            is_neg = -1
        if i == n:
            return 0

        num = 0
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1
        while i < n and self.is_digit(s[i]) is True:
            num = num * 10 + ord(s[i]) - ord('0')
            if self.is_out_of_range(num*is_neg) is True:
                if is_neg == -1:
                    return INT_MIN
                else:
                    return INT_MAX
            i += 1
        return num*is_neg

a = Solution()
print(a.myAtoi('42'))
print(a.myAtoi('-42'))
print(a.myAtoi('4193 with words'))
print(a.myAtoi('words and 987'))
print(a.myAtoi('-91283472332'))
print(a.myAtoi('    -'))
print(a.myAtoi('    '))
print(a.myAtoi('+     122'))
print(a.myAtoi(' 1223 4111'))
print(a.myAtoi('-0'))
print(a.myAtoi('-+12'))
print(a.myAtoi('------+12'))
print(a.myAtoi('.12'))
print(a.myAtoi('+-12'))


