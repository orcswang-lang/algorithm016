class Solution:
    def replaceSpace(self, s: str) -> str:
        return ''.join(['%20' if c == ' ' else c for c in s])