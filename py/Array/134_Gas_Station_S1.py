from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remain = []
        for g, c in zip(gas, cost):
            remain.append(g - c)
        for i in range(n):
            if remain[i] < 0:
                continue
            else:
                S = 0
                for j in range(n):
                    S += remain[(i + j) % n]
                    if S < 0:
                        break
                if S >= 0:
                    return i
        return -1