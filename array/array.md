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

Solution:

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

   【待完善】

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

