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





# Reference

1. Python中字符串的连接方法总结： https://segmentfault.com/a/1190000015475309
2. 

