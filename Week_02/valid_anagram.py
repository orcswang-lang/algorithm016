class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """根据哈希表"""
        if len(s) != len(t): return False
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in t:
            if c not in count: return False
            count[c] -= 1
        for v in count.values():
            if v != 0: return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def isAnagram3(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram4(self, s, t):
        """
        排序
        长度不相等则提前返回
        排序后进行对比
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)

    def isAnagram5(self, s: str, t: str) -> bool:
        """ASCII码判断"""
        return abs(sum([ord(x) ** 0.5 for x in s]) - sum([ord(y) ** 0.5 for y in t])) < 1e-5