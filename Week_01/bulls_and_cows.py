class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        acnt, bcnt = 0, 0

        for i in range(len(secret)):
            if secret[i] == guess[i]: acnt += 1

        d1 = dict(collections.Counter(list(secret)))
        d2 = dict(collections.Counter(list(guess)))

        for i in d1:
            if i in d2:
                bcnt += min(d1[i],d2[i])
        bcnt = bcnt - acnt
        return "{acnt}A{bcnt}B".format(acnt=acnt, bcnt=bcnt)

    def getHint2(self, secret: str, guess: str) -> str:
        acnt = sum(s == g for s, g in zip(secret, guess))
        bcnt = sum((collections.Counter(secret) & collections.Counter(guess)).values()) - acnt
        return "{acnt}A{bcnt}B".format(acnt=acnt, bcnt=bcnt)