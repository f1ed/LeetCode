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

a = Solution()
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
words = ["abc", "cd", "f", "h", "aaaaaaa"]
maxWidth = 12
ans = a.fullJustify(words, maxWidth)
for i in ans:
    print(i)




