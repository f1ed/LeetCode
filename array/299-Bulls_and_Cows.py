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
