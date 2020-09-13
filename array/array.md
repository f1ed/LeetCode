### 27. Remove Elements

[Remove Elements](https://leetcode.com/problems/remove-element/) 

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

[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 

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

1. 第一次提交的时候`before = nums[0] - 1` 报错了，原因是传入数组长度为0，下标越界。

   注意空数组的下标越界问题。