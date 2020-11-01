class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans

    def findLength1(self, A: List[int], B: List[int]) -> int:
        # 滑动窗口
        def findmax(A, B):
            ans_max = 0
            la = len(A)
            lb = len(B)
            # B进来，从1到la长度
            for tlen in range(1, la + 1):
                ans_max = max(ans_max, max_len(A, 0, B, lb - tlen, tlen))
            # B出去,长度保持在la
            for j in range(lb - la, -1, -1):
                ans_max = max(ans_max, max_len(A, 0, B, j, la))
            # B出去，长度从la到0 -->相当于A左移
            for i in range(1, la):
                ans_max = max(ans_max, max_len(A, i, B, 0, la - i))

            return ans_max

        def max_len(A, i, B, j, length):
            count = 0
            temp_max = 0
            for k in range(length):
                if A[i + k] == B[j + k]:
                    count += 1
                elif count > 0:
                    temp_max = max(temp_max, count)
                    count = 0
            temp_max = max(temp_max, count)
            return temp_max

        if len(A) <= len(B):
            return findmax(A, B)
        else:
            return findmax(B, A)

    def findLength2(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret