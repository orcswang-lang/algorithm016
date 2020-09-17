class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        回溯法
        如果左括号数量不大于n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号
        :param n:
        :return:
        """
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans

    def generateParenthesis2(self, n: int) -> List[str]:
        """
        按括号序列的长度递归
        :param n:
        :return:
        """
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis2(c):
                for right in self.generateParenthesis2(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

    def generateParenthesis3(self, n: int) -> List[str]:
        """
        动态规划
        dp[i]表示i组括号的所有有效组合
        dp[i] = "(dp[p]的所有有效组合)+【dp[q]的组合】"，其中 1 + p + q = i , p从0遍历到i-1, q则相应从i-1到0
        :param n:
        :return:
        """
        dp = [[] for _ in range(n + 1)]  # dp[i]存放i组括号的所有有效组合
        dp[0] = [""]  # 初始化dp[0]
        for i in range(1, n + 1):  # 计算dp[i]
            for p in range(i):  # 遍历p
                for k1 in dp[p]:  # 遍历得到dp[p]的所有有效组合
                    for k2 in dp[i - 1 - p]:  # 遍历得到dp[q]的所有有效组合
                        dp[i].append("({0}){1}".format(k1, k2))
        return dp[n]

    def generateParenthesis4(self, n: int) -> List[str]:
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right): yield q
                for q in generate(p + ')', left, right - 1): yield q

        return list(generate('', n, n))

    def generateParenthesis5(self, n: int) -> List[str]:
        """
        l:左括号计数
        r:右括号计数
        l - r < 0表示不是一个有效括号
        :param n:
        :return:
        """
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x + "(", l + 1, r))
            s.append((x + ")", l, r + 1))
        return res