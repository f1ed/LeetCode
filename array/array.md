### 27. Remove Elements

[27-Remove Elements](https://leetcode.com/problems/remove-element/) 

Solution

```python
from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        tot = 0
        for element in nums:
            if element == val:
                continue
            else:
                nums[tot] = element
                tot = tot + 1
        return tot

```



1. Python的参数传递和函数返回值：

   ```python
   def removeElement(self, nums:List[int], val:int) -> int:
   ```

2. 题目要求：

   “remove all instances of that value [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) and return the new length.”

   "Do not allocate extra space for another array, you must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory."

   “Confused why the returned value is an integer but your answer is an array?

   Note that the input array is passed in by **reference**, which means modification to the input array will be known to the caller as well.”

   题目要求是在原数组上删除数值，不能额外开新的空间存储数组。

   意思就是说，虽然函数返回的是一个数值，但实际返回答案是一个数组。

   因为数组的传递是指针传递，返回的是数组长度，则相当于返回了这个in-place的新数组。

### 26. Remove Duplicates from Sorted Array

[26-Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 

Solution：

```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        tot = 0
        before = None
        for index in range(len(nums)):
            if nums[index] != before:
                nums[tot] = nums[index]
                before = nums[index]
                tot = tot + 1
            else:
                continue

        return tot
```



---

1. 第一次提交的时候`before = nums[0] - 1` 报错了，原因是传入数组长度为0，下标越界。

   注意空数组的下标越界问题。

### 80. Remove Duplicates from Sorted Array II

[80-Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) 

Solution:

```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        before = None
        before_cnt = 0
        length = 0
        for index in range(len(nums)):
            if nums[index] != before:
                nums[length] = nums[index]
                before = nums[index]
                length += 1
                before_cnt = 1
            else:
                before_cnt += 1
                if before_cnt <= 2:
                    nums[length] = nums[index]
                    length += 1
        return length

```

### 189. Rotate Array

[189-Rotate Array](https://leetcode.com/problems/rotate-array/) 

Problem:

简述题目大意，给一个列表nums，一个 $k$ 值，要求原址让列表循环右移 $k$ 位。

Solution:

其实以下三种做法时间空间复杂度差别不大，主要看个思路吧。

| S    | Runtime | Memory | Language |
| ---- | ------- | ------ | :------: |
| S1   | 64ms    | 15.2MB |  pyhon3  |
| S2   | 64ms    | 15.1MB | python3  |
| S3   | 116ms   | 15.1MB | python3  |

1. 简单做法：空间换时间

   时间复杂度：$\mathcal{O}(n)$ 

   空间复杂度：$\mathcal{O}(n)$ ，循环右移时多开了一个数组。

   ```python
   from typing import List
   import queue
   
   class Solution:
       def rotate(self, nums: List[int], k: int) -> None:
           """
           Do not return anything, modify nums in-place instead.
           """
           length = len(nums)
           a = [0] * length
           for index in range(length):
               a[(index + k)%length] = nums[index]
           nums[:] = a
   ```

2. 利用数学同余关系

   时间复杂度：$\mathcal{O}(n)$ 

   空间复杂度：$\mathcal{O}(n)$ ，循环右移时只多开了一个变量。

   原理：

   > 定理[1]：
   >
   > 设 $m$ 是正整数，整数 $a$ 满足 $(a,m)=1$ ，$b$ 是任意整数。若 $x$ 遍历模 $m$ 的一个完全剩余系，则 $ax+b$ 也遍历模 $m$ 的一个完全剩余系。

   由以上定理可以得知，设 $n$ 为列表长度， $x$ 是列表的下标，遍历 $n$ 的一个完全剩余系。

   - 如果 $(k,n)=1$ ， $kx$ 也遍历 $n$ 的一个完全剩余系。这种情况，列表下标通过 $k$ 的倍数的顺序连成一个环。

     ：只需要额外一个变量 $temp$ 存储移动占用的值。

   - 如果 $(k,n)\neq 1$ ，那么 $kx$ 不会遍历一个 $n$ 的完全剩余系，会出现下图的情况（如绿色的线的元素的 $idx = kx+0$ ，红色线的元素都是 $idx=kx+1$ ），会在 $k$ 的某个剩余类一直循环。

     ：遍历每个 $k$ 的剩余类。 在每次循环移位时，需要记录该次循环的起始位，防止重复。

     <img src="https://s1.ax1x.com/2020/09/14/wrcSVs.png" alt="wrcSVs.png" style="zoom:50%;" />

   ```python
   class Solution:
       def rotate(self, nums: List[int], k: int) -> None:
           """
           Do not return anything, modify nums in-place instead.
           """
           length = len(nums)
           k %= length
           start = 0
           cnt = 0
           while cnt < length:
               current, prev = start, nums[start]
               while True:
                   current = (current + k) % length
                   prev, nums[current] = nums[current], prev
                   cnt += 1
                   if current == start:
                       break
               start += 1
   ```

3. 利用反转列表的思路

   时间复杂度：$\mathcal{O}(n)$ 

   空间复杂度：$\mathcal{O}(n)$ 

   原理：

   ```pseudocode
   Original List                   : 1 2 3 4 5 6 7
   After reversing all numbers     : 7 6 5 4 3 2 1
   After reversing first k numbers : 5 6 7 4 3 2 1
   After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
   ```

   ```python
   from typing import List
   
   
   # Solution 3: Reverse
   class Solution:
   
       def reverse(self, nums: list, begin: int, end: int) -> None:
           while begin < end:
               nums[begin], nums[end] = nums[end], nums[begin]
               begin += 1
               end -= 1
   
       def rotate(self, nums: List[int], k: int) -> None:
           n = len(nums)
           k %= n
           self.reverse(nums, 0, n-1)
           self.reverse(nums, 0, k-1)
           self.reverse(nums, k, n-1)
   ```

   

---



1. Python用引用管理对象。

   ```c++
   int a1 = 1, *p = &a1;
   int a2 = 2, &b = a2;
   ```

   - 指针：指针变量是一个新变量，这个变量存储的是（变量a1的）地址，该地址指向一个存储单元。（该存储单元存放的是a1的值）。
   - 引用：引用的实质是变量的别名，所以a2和b实际是一个东西，在内存中占有同一个存储单元。

   所以python中交换对象可以直接`a,b = b,a` 

2. Python 列表的操作：切片。

### 41-First Missing Positive

[41-First Missing Positive](https://leetcode.com/problems/first-missing-positive/)  

Solution:

排一下序，维护一个expect变量就行了。

时间复杂度：$\mathcal{O}(n\log{n})$ ，题目没有卡常。

Runtime: 36 ms, faster than 70.96% of Python3 online submissions for First Missing Positive.

空间复杂度：$\mathcal{O}(n)$

Memory Usage: 13.8 MB, less than 69.19% of Python3 online submissions for First Missing Positive. 

```python
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        expect = 1
        for element in nums:
            if element == expect:
                expect += 1
            elif element > expect:
                return expect
        return expect
```

### 299-Bulls and Cows

[299-Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/) 

Problem:

题目大意是：给定两个相同长度的字符串，计算这两个字符串有多少个对应位数字相同，和多少个位置不对应但数字相同的个数。

Solution:

应用字符0-9本身数字的性质。

时间复杂度：$\mathcal{O}(n)$ 

空间复杂度：$\mathcal{O}(n)$ 

```python
class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        # 0-9 cnt for guess (expect the same digit)
        cnt = [0] * 10
        bulls = cows = 0
        g = lambda a: ord(a) - ord('0')
        for si, gi in zip(secret, guess):
            if si == gi:
                bulls += 1
            else:
                cnt[g(gi)] += 1

        for si, gi in zip(secret, guess):
            if si == gi:
                continue
            elif cnt[g(si)] > 0:
                cows += 1
                cnt[g(si)] -= 1
        output = "{}A{}B".format(bulls, cows)
        return output
```



---

1. ord()函数和chr()函数

   ord()返回字符的ASCII码，chr函数返回ASCII码对应的字符。

2. 浅析lambda表达式，匿名函数，类似于C语言的宏。

   格式：`lambda [arg1[, arg2,...]] : expression` 

3. 双变量同时遍历使用zip()函数

### 134-Gas Station

[134-Gas Station](https://leetcode.com/problems/gas-station/) 

Problem：

题目大意是：有N个环形加油站，每个加油站能加油gas[i]，一个汽车起始油量为0，且从i个站开到第i+1个站需要花费cost[i]的油量。找出这个车能顺时针跑完一圈的起始点（如果有，则唯一），如果不能返回-1。

Solution：

| Solution    | Runtime | Memory | Language |
| ----------- | ------- | ------ | -------- |
| S1-简单做法 | 3244ms  | 14.9MB | python3  |
| S2-原理优化 | 104ms   | 14.8MB | python3  |

1. 简单解法：

   时间复杂度：$\mathcal{O}(n^2)$ ，实际远达不到 $n^2$ ，算有一点贪心叭。

   空间复杂度：$\mathcal{O}(n)$ 

   该汽车从起点i能跑完的必要条件：

   - 起始点 `gas[i] - cost[i] >= 0` 。并且维护一个数组存放 `gas[i] - cost[i]` ，即这个站自给自足的油量余量。

   - 如果从满足条件1的起点开始跑一圈， 要求路程中的油量必须大于等于0。维护一个汽车当前总油量 $S$ （用前缀和维护），每跑过一段路程，都要求 $S>=0$ 。

   ```python
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
   ```

2. 对问题分析进行再简化

   ```python
     i	: 0 1 2 3 4
   g[i]: 1 2 3 4 5
   c[i]: 3 4 5 1 2
   g-c :-2-2-2 3 3
   sum :-2-4-6-3 0
   ```

   - 如果 $S=\sum_{i=0}^{n-1} g[i]-c[i],S<0$  那么一定无解， $S$ 称为总积累油量。

   - 如果 $S>=0$，如果有找出最优解的方法，则一定有解。

     1. 起点满足 $g[i]-c[i]>=0$ ，把这些点称为正余量点。

     2. 用 $\mathcal{O}(1)$ 算出从第 $i$ 个点出发到第 $n$ （n就是第0个点） 个点所积累的油量： $res[i] =S-sum[i-1]$ .即用总积累油量减去前 $i-1$ 段路程能积累的油量（一般积累为负）。(sum数组就是 g-c的前缀和)
     3. 对于满足起点要求 $g[i]-c[i]>=0$ 的所有点，计算从第 $i$ 个点出发到第 $n$ 个点到油量积累。那么有最大油量积累的点即为最优起始点。（题目规定如果存在，则点唯一）
     4. 因此，因为 $S$ 固定，只需要找到 $sum$ 数组中的最小值的下标，下标+1即是结果。

     - 证明其正确性：
       1. 如果满足 $g[i]-c[i]>=0$ 的上述点 $i,j（i<j)$  ，如果 $res[i]>=res[j]$ ，说明从 $i$ 到 $j$ 是正油量积累，贪心的思想，那肯定积累的油量越多越好， $i$ 比 $j$ 优。
       2. 如果 $res[i]<=res[j]$ ，说明从 $i$ 到 $j$ 是负油量积累，如果从 $i$ 点出发，到 $j$ 点就负油量了；如果从 $j$ 点出发，该车最后再跑 $i$ 到$j$  段，因为保证了总积累油量是正，所以最后一定有足够的油量能跑完 $i$ 到 $j$ 段。
       3. 再证只要 $S>=0$ 则一定有解。是动态尝试起始点，( $i,j$ 都满足 $g[i]-c[i]>=0$ ）从点 $i$ 开始，跑到点 $j$ 时，如果该途中途有出现油量不够，那就把 $i$ 到 $j$ 的这段路程放到路途的后面来跑，等油量积累够了再跑这段。

   Code:

   ```python
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
   
   ```

   



---

1. 前缀和
2. `list.index(value)` 找出list中值为`value` 的第一个下标。
3. `min(list)` 返回list中的最小值。



# reference

1. 《信息安全数学基础》 2.2同余类和剩余系。