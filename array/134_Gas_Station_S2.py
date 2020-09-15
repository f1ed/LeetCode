from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        sum = 0
        remain = []
        for g, c in zip(gas, cost):
            remain.append(g - c)
            sum += g - c
        if sum < 0:
            return -1
        for i in range(1, n):
            remain[i] += remain[i - 1]
        min_idx = remain.index(min(remain))
        return (min_idx + 1) % n
