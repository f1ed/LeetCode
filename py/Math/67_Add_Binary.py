class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = list(reversed(a))
        b = list(reversed(b))
        lenA = len(a)
        lenB = len(b)
        ans = ''
        for i in range(max(lenA, lenB)):
            sum = carry
            if i < lenA:
                sum += int(a[i])
            if i < lenB:
                sum += int(b[i])
            ans = str(sum % 2) + ans
            carry = sum // 2
        if carry:
            ans = str(carry) + ans
        return ans
if __name__ == '__main__':
    x = Solution()
    ans = x.addBinary("1011", "101")
    print(ans)
