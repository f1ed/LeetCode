# The knows API is already defined for you.
# return a bool, whether a knows b

def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            fg = True
            # i knows j ?
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    fg = False
                    break
            if not fg:
                continue
            # j knows i ?
            for j in range(n):
                if i == j:
                    continue
                if not knows(j, i):
                    fg = False
                    break
            if not fg:
                continue
            else:
                return i
        return -1




