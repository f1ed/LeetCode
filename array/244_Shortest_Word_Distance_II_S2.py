from typing import List


class WordDistance:

    def __init__(self, words: List[str]):
        self.words = words
        self.len = len(words)
        self.dict = {}
        for index in range(self.len):
            word = words[index]
            if word in self.dict:
                temp = self.dict[word]
                temp.append(index)
            else:
                temp = [index]
                self.dict[word] = temp

    def shortest(self, word1: str, word2: str) -> int:
        ans = self.len
        li1 = self.dict[word1]
        li2 = self.dict[word2]
        len1 = len(li1)
        len2 = len(li2)
        i = j = 0
        while i < len1 and j < len2:
            ans = min(ans, abs(li1[i] - li2[j]))
            if ans == 1:
                return ans
            # i goes ahead
            if li1[i] < li2[j]:
                i += 1
            else:
                j += 1
        return ans

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


