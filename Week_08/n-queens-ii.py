class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.res

    def dfs(self,n, row, col, ld, rd):
        if row >= n:
            self.res +=1
            return
        bits = ~(col | ld | rd) & ((1 << n) - 1)
        while bits >0:
            pick = bits & -bits
            self.dfs(n, row + 1, col | pick, (ld | pick) << 1, (rd | pick) >> 1)
            bits &= bits - 1