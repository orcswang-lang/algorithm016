class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        """单指针计数"""
        res, count = [], 0
        for c in S:
            if c == "(":
                if count > 0: res.append(c)
                count += 1
                continue
            if c == ")":
                if count >1: res.append(c)
                count += -1
                continue
        return "".join(res)

    def removeOuterParentheses2(self, S: str) -> str:
        """把非外层括号放进栈中"""
        res, stack = "", []
        for c in S:
            # 判断是非外层括号,1. 左括号加入前，栈不为空。2. 右括号加入并消括号后，栈不为空
            if c == "(":
                if stack: res += c
                stack.append(c)
            if c == ")":
                stack.pop()
                if stack: res += c
        return res