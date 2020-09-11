class Solution:
    def isValid(self, s: str) -> bool:
        """
        定义一个栈，根据栈的特性，进行左右括号的抵消，结束后栈长度为1则说明已全部抵消，有效且合法
        """
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1