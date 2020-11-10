# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
                continue
        for i in range(n):
            if celebrity == i:
                continue
            if (not knows(celebrity, i)) and knows(i, celebrity):
                continue
            else:
                return -1
        return celebrity




