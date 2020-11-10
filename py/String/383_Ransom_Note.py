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

a = Solution()
ransomNote = "aa"
magazine = "aab"
if a.canConstruct(ransomNote, magazine):
    print("true")
else:
    print("false")
