from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = [1]
        for i in range(0, rowIndex):
            for j in range(i, 0, -1):
                temp[j] += temp[j-1]
            temp.append(1)
        return temp

