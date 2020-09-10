class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        检测字符串是否由字母和数字组成
        如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
        """
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
        return True