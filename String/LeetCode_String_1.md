# String

## 28-Implement strStr()

[28-Implement strStr()](https://leetcode.com/problems/implement-strstr/solution/) 

Problem:

返回第一个字串出现的下标

Solution：

Python就暴力匹配。

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1 = len(haystack)
        n2 = len(needle)
        for i in range(0, n1-n2+1):
            if haystack[i:i+n2] == needle:
                return i
        return -1
```

## 14-Longest Common Prefix

[14-Longest Common Prefix](https://leetcode-cn.com/problems/longest-common-prefix/)

Problem:

返回串的公共最长前缀。

Solution：

暴力匹配长度就好。

```python
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LCP = 0
        n = len(strs)
        if n == 0:
            return ""
        while True:
            for i in range(0, n):
                if LCP < len(strs[i]) and strs[i][LCP] == strs[0][LCP]:
                    continue
                else:
                    return strs[0][0: LCP]
            LCP += 1

```

## 58-Length of Last Word

[58-Length of Last Word](https://leetcode.com/problems/length-of-last-word/) 

Problem:

单词串由字母和空格组成，返回最后一个单词的长度。

Solution：

注意串最后的空格。

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        length = 0
        end = n-1
        while end-1 >= 0 and s[end] == ' ':
            end -= 1
        for i in range(end, -1, -1):
            if s[i] == ' ':
                return length
            else:
                length += 1
        return length
```

## 58-First Unique Character in a String

Problem:

找第一个没有重复出现的字符下标。

Solution：

暴力。

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a_ascii = ord('a')
        cnt = [0]*(26+5)
        for i in s:
            cnt[ord(i)-a_ascii] += 1
        for idx in s:
            if cnt[ord(i)-a_ascii] == 1:
                return s.index(i)
        return -1
```

---

寻找子串开始索引：

1. **str.find(substr, beg=0, end=len(string))** 
   - substr: 字串
   - beg: 开始索引
   - end: 结束索引，默认字符串长度。
   - 如果字符串不包含子串，则返回`-1` 
2. **str.index(str, beg=0, end=len(string))** 
   - 和find差不多，如果不包含子串会抛出异常。

## 383-Ransom Note

[383-Ransom Note](https://leetcode.com/problems/ransom-note/) 

Problem:

给两个字符串，判断串1的字符能否由串2的字符组成。

Solution：

字典计数。

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDir = {}
        magazineDir = {}
        for ch in ransomNote:
            ransomDir.setdefault(ch, 0)
            ransomDir[ch] += 1
        for ch in magazine:
            magazineDir.setdefault(ch, 0)
            magazineDir[ch] += 1
        for (k, v) in ransomDir.items():
            if k not in magazineDir:
                return False
            if ransomDir[k] > magazineDir[k]:
                return False
        return True
```

---

1. 初始化字典的值：`dic.setdefault(ch, 0)` 



## 344-Reverse String

[344-Reverse String](https://leetcode.com/problems/reverse-string/) 

Problem: 

in-place 反转字符串 with O(1) 的额外空间。

Solution：

前后两个指针交换。

```python
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = n-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```



## 151-Reverse Words in a String

[151-Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) 

Problem:

反转字符串word by word.(结果中单词间只能有一个空格)

Solution：

把单词存入列表，再输出。

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        li = []
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            l = i
            while i < n and s[i] != ' ':
                i += 1
            r = i
            if r != l:
                li.append(s[l:r])

        ans = ' '.join(li[-1::-1])
        return ans
```

---

[Python连接字符串总结](https://segmentfault.com/a/1190000015475309) 

1. 加号连接：`'a' + 'b' ` 
2. 逗号连接，只能用于print打印: `print(a, b)` 
3. 直接连接: `print('a' 'b')` 
4. 使用 `%` 格式化字符串：`'%s %s' % ('hello', 'world')` 
5. `format` 格式化字符串：`'{}{}'.format('hello', 'world')` 
6. `join` 内置方法：用字符来连接一个序列，数组或列表等：`'-'.join(['aa', 'bb', 'cc'])` 
7.  `f-string` 方法：`aa, bb = 'hello', 'world'` , `f'{aa} {bb}'` 
8. `*` 操作符：字符串乘法。

反转列表：`[-1: : -1]` 

## 186-Reverse Words in a String II

[186-Reverse Words in a String II](https://leetcode-cn.com/problems/reverse-words-in-a-string-ii/) 

Problem:

反转单词in-places.

Solution:

两次反转，第一次整体反转，第二次再单词反转。

（不额外开个数组来逐个赋值AC不了，不知道为啥q w q)

```python
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = s[-1::-1]
        n = len(temp)
        i = 0
        while i < n:
            l = i
            while i < n and temp[i] != ' ':
                i += 1
            r = i
            temp[l:r] = list(reversed(temp[l:r]))

            i += 1
        for index in range(n):
            s[index] = temp[index]
```

---

- Python 反转列表的方法：

  1. `list(reversed(a))` , reversed(a)返回的是迭代器，转换成list。
  2. `a[::-1]` 

- Python 字符串(str)和列表(list)互相转换：

  1. str 转换为 list

     - `list()` 转换为单个字符列表
     - `str.split()` 或者`str.split(' ')` 空格分割转换

     ```python
     str1 = "123"
     list1 = list(str1)
     print list1
     # ['1', '2', '3']
     
     str2 = "123 sjhid dhi"
     list2 = str2.split() #or list2 = str2.split(" ")
     print list2
     # ['123', 'sjhid', 'dhi']
     
     str3 = "www.google.com"
     list3 = str3.split(".")
     print list3
     # ['www', 'google', 'com']
     ```

  2. list转换为str:
     - `"".join(list)` 无空格连接
     - `".".join(list)`  

## 345-Reverse Vowels of a String

[345-Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) 

Problem:

反转字符串中的元音字母。

Solution：

元音字母，包括大写元音字母和小写元音字母。

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        dic = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        rev = [0] * n
        for index in range(n):
            if s[index] in dic or s[index].lower() in dic:
                rev[index] = 1
        l = 0
        r = n - 1
        while l < r:
            while l < r and rev[l] == 0:
                l += 1
            while l < r and rev[r] == 0:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
```

---

- Python大小写转换：

  - 所有字符转换为大写：`str.upper()` 
  - 所有字符转换为小写：`str.lower()` 
  - 第一个字母转换为大写字母，其余小写：`str.capitalize()` 
  - 把每个单词的第一个字母转换为大写，其余小写。

  ```python
  str = "www.runoob.com"
  print(str.upper())          # 把所有字符中的小写字母转换成大写字母
  print(str.lower())          # 把所有字符中的大写字母转换成小写字母
  print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
  print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写
  
  # WWW.RUNOOB.COM
  # www.runoob.com
  # Www.runoob.com
  # Www.Runoob.Com
  ```

- Python中string是不可变对象，不能通过下标的方式（如`str[0]='a'` )改变字符串。

## 205-Isomorphic Strings

[205-Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) 

Problem:

判断是否同构字符串。

Solution：

字符到字符的映射，必须是单射。

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        dic = {}
        vSet = set()  # satisfy single map
        for idx in range(n):
            ch = s[idx]
            # single map
            if ch not in dic and t[idx] not in vSet:
                dic[ch] = t[idx]
                vSet.add(t[idx])
                continue
            if ch in dic and dic[ch] == t[idx]:
                continue
            return False
        return True
```

---

- Python 集合的操作：

  1. 创建空集合：`set()` 

  2. 创建有初值的集合：`SET = {v0, v1, v2}` 或者`SET = set(v0)` 

  3. 判断元素是否在集合中：`x in SET` 

  4. 集合运算：

     `a-b` :属于a集合不属于b集合

     `a|b` :属于a集合或属于b集合

     `a&b` :集合a和集合b都包含的元素

     `a^b` : 不同时包含于集合a和集合b的元素

  5. 集合中添加元素：`s.add(x)` 

  6. 集合中添加元素，且参数可以是列表、元组、字典(是每个元素都添加进去）等：`s.update(x)` 

  7. 移除元素：`s.remove(x)` ，如果元素不存在，则会发生错误。

  8. 移除元素：`s.discard(x)` ，如果元素不存在，不会发生错误。

  9. 随机删除集合中的一个元素：`s.pop()` （原理：对集合无序排序，然后删除无序排列集合的第一个）

  10. 计算集合元素的个数：`len(s)` 

  11. 清空集合`s.clear()` 

- List Comprehension && Set Comprehension && Dictionary Comprehension

  这个相当于数学中的 $S=\{2\cdot x\mid x\in \left[0,9\right)\}$ 的表达。

  1. List Comprehension

     如果用数学中的这个表达来看下面的式子，就很显而易见了。

     ```python
     arr = [i for i in range(10)]
     ```

     再看看加了其他限制的例子

     ```python
     # filter the elements
     arr1 = [x for x in arr if x % 2==0]
     
     # add more conditions
     arr2 = [x**2 for x in arr if x >= 3 and x % 2]
     
     # use nested for loops
     arr3 = [(x, y) for x in range(3) for y in range(4)]
     ```

     使用List Comprehension不仅优美，而且效率也会很高。

  2. Set Comprehension

     同样的

     ```python
     s = {x for x in range(100) if x%2 != 0 and x%3 != 0}
     ```

  3. Dictionary Comprehension

     Syntax：`{expression(variable): expression(variable) for variable, variable in input_set [predicate][, …]}`  

     ```python
     # [(set_k), (set_v)]
     >>> {k: v for k, v in [(1, 2), (3, 4)]}
     {1: 2, 3: 4}
     
     >>> {n: n for n in range(2)}
     {0: 0, 1: 1}
     >>> {chr(n): n for n in (65, 66, 66)}
     {'A': 65, 'B': 66}
     
     # ((k1, v1), (k2, v2))
     >>> {k: v for k, v in (('I', 1), ('II', 2))}
     {'I': 1, 'II': 2}
     >>> {k: v for k, v in (('a', 0), ('b', 1)) if v == 1}
     {'b': 1}
     ```

     

## 68-Text Justification

[68-Text Justification](https://leetcode.com/problems/text-justification/) 

Problem:

文本对齐，总结下来有以下几点要求。

- 如果不是最后一行，且该行不止一个单词，则要求左右对齐。
  - 左右对齐：尽可能让单词间的空格均匀分布，如果不能均匀分布，则单词左边的空格应该比右边的空格多。
  - 贪心的思想：应该尽可能的多放单词。
- 如果是最后一行，或者该行只有一个单词，则要求左对齐。

Solution：

分两种情况处理，判断是左对齐，还是右对齐。

1. 左对齐：该行有x个单词

   前x-1个单词的后面都应该只有一个空格。

   最后一个单词后面就应该补齐所有空格。

2. 左右对齐：该行有x个单词，有x-1个空格间隙。

   计算得到该行的空格数w，则如果能均匀分配，则每个间隙应该有aver = w // (x-1) 个空格。

   但也许不会均匀分配，因此，可能会多出m个空格（m < x-1 )

   即前m个单词，单词的后面应该有（aver+1)个空格，后面的(x-1) - m个单词应该有aver个空格。

   最后一个单词的后面没有空格。

```python
from typing import List


class Solution:
    def __init__(self):
        self.words = None
        self.maxWidth = None
        self.sum = None

    def leftJustify(self, l: int, r: int) -> str:
        wordsNum = r - l + 1
        lengthNum = self.sum[r] if l == 0 else self.sum[r] - self.sum[l - 1]
        spaceNum = self.maxWidth - lengthNum
        temp = ""
        for i in range(l, r):
            temp += self.words[i] + " "
        temp += self.words[r] + " "*(spaceNum - (wordsNum - 1))
        return temp

    def leftRightJustify(self, l: int, r: int) -> str:
        wordsNum = r - l + 1
        lengthNum = self.sum[r] if l == 0 else self.sum[r] - self.sum[l - 1]
        spaceNum = self.maxWidth - lengthNum
        temp = ""
        averSpace = spaceNum // (wordsNum - 1)
        moreSpace = spaceNum - averSpace*(wordsNum - 1)
        for i in range(moreSpace):
            temp += self.words[l+i] + " " * (averSpace + 1)
        for i in range(l+moreSpace, r):
            temp += self.words[i] + " " * averSpace
        temp += self.words[r]
        return temp

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.words = words
        self.maxWidth = maxWidth
        n = len(words)
        sum = [0]*n
        sum[0] = len(words[0])
        # sum prefix length of words
        for i in range(1, n):
            sum[i] = sum[i - 1] + len(words[i])
        self.sum = sum
        l = 0
        ans = []
        while l < n:
            r = l
            lengthNum = len(self.words[l])
            while r+1 < n and lengthNum + len(self.words[r+1]) + 1 <= maxWidth:
                lengthNum += len(self.words[r+1]) + 1  # space
                r += 1
            # only one word or the last line
            if r - l + 1 == 1 or r == n - 1:
                ans.append(self.leftJustify(l, r))
            else:
                ans.append(self.leftRightJustify(l, r))
            l = r + 1
        return ans
```

---

- Python的三元运算符：

  #如果条件为真，返回真 否则返回假
  condition_is_true if condition else condition_is_false

  ```python
  is_fat = True
  state = "fat" if is_fat else "not fat"
  ```

- Python的整除是：`\\` ，实数除是：`\` 

# Reference

1. Python中字符串的连接方法总结： https://segmentfault.com/a/1190000015475309
2. 

