---
title:  「LeetCode」：Math
date: 2020/10/10 #
description: #
categories: LeetCode
tags: 
- LeetCode
- Math
toc: true
thumbnail: /gallery/thumbnails/84326425_p0_master1200.jpg
banner: #
comments: #true or false





---



LeetCode Math 专题记录。

10月初。

Albert Einstein:

 "I believe that not everything that can be counted counts, and not everything that counts can be counted"

「并非所有重要的东西都是可以被计算的，也并不是所有能被计算的东西都那么重要。」

<!--more-->

## 7. Reverse Integer[E]

[7. Reverse Integer[E]](https://leetcode.com/problems/reverse-integer/) 

Problem:

反转32bits的有符号数字，如果反转后会溢出则返回0.

Solution：

直观的解决它，先算出反转后的数字，用比较大小来看是否溢出。（最开始还想着转换为bit串来看，就复杂了）

```python
class Solution:
    def reverse(self, x: int) -> int:
        n_min = -(2 ** 31)
        n_max = 2 ** 31 - 1
        s = 0
        flag = True
        if x < 0:
            flag = False
            x = -x
        while x != 0:
            r = x % 10
            s = s * 10 + r
            x //=10
        if flag is False:
            s = -s
        if s < n_min or s > n_max:
            return 0
        return s
```

---

- 十进制转换为二进制、八进制、十六进制：

  - 二进制：`bin(a)`  ,也可以直接赋二进制的值`0b10101` 
  - 八进制：`oct(a)` ，赋值八进制的值`0o263361` 
  - 十六进制：`hex(a)` ,赋值十六进制`0x1839ac29` 

  

## 165. Compare Version Numbers[M]

[165. Compare Version Numbers[M]](https://leetcode.com/problems/compare-version-numbers/) 

Problem：

比较版本号。

Solution：

直观～Easy～

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        li1 = version1.split('.')
        li2 = version2.split('.')
        n_1 = len(li1)
        n_2 = len(li2)
        n = max(n_1, n_2)
        for i in range(n):
            a = int(li1[i]) if i < n_1 else 0
            b = int(li2[i]) if i < n_2 else 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
```

---

- Python中的强制转换：
  1. 字符串转换为int : `int_value = int(str_value)` 
  2. int转换为字符串：`str.value = str(int_value)` 
  3. int转换为unicode： `unicode(int_value)` 
  4. unicode转换为int：`int(unicode_value)` 
  5. 字符串转换为unicode：`unicode(str_value)` 
  6. unicode转换为字符串：`str(unicode_value)` 
- Java中的强制转换：
  1. 字符串String转化为int：`int_value = String.parseInt(string_value)` 或者 `(int)string_value)` 
  2. int转化为字符串String：`string_value = (String)int_value` 

## 66. Plus One[E]

[66. Plus One[E]](https://leetcode.com/problems/plus-one/) 

Problem:

用列表表示一个正数，返回正数+1的列表结果。

Solution：

记录一个最高位的进位情况。

```python
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c_bit = 0
        n = len(digits)
        i = n - 1
        digits[i] += 1
        while i >= 0:
            if digits[i] < 10:
                break
            digits[i] %= 10
            if i == 0:
                c_bit = 1
            else:
                digits[i-1] += 1
            i -= 1
        if c_bit == 1:
            digits.insert(0, c_bit)
        return digits
```

---

- Python中list添加元素的集中方法：（append(); extend(); insert(); +加号）

  1. append() ：在List尾部追加单个元素，只接受一个参数，参数可以是任意数据类型。

  2. extend() ：在list尾部追加一个列表，将该参数列表中的每个元素连接到原列表。

     ```shell
     >>> a = [1,2,3]
     >>> b = [3,4,5]
     >>> a.extend(b)
     >>> a
     [1, 2, 3, 3, 4, 5]
     ```

  3. insert(index, object)：将一个元素插入到列表中，第一个参数是插入的索引点，第二个是插入的元素。
  4. +加号：将两个list相加，返回一个新的list对象。

  区别：前三种方法(append, extend, insert)可以对列表增加元素，没有返回值，是直接修改原数据对象，而+加号是需要创建新的list对象，需要消耗额外的内存。