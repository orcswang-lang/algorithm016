
class SolutionO:

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        方法1
        1.将列表转换数字
        2.转换后的数字加1
        3.再将加一后的数字转为列表
        :param digits:
        :return:
        """
        nums = [val * 10 ** idx for idx, val in enumerate(digits[::-1])]
        num = sum(nums) + 1
        return [int(n) for n in str(num)]

    def plusOne1(self, digits: List[int]) -> List[int]:
        """
        方法2
        从后往前依次判断末尾是否为9，如果是则移除并追加0
        :param digits:
        :return:
        """
        newlst = []
        while digits and digits[-1] == 9:
            digits.pop()
            newlst.append(0)
        if not digits:
            return [1] + newlst
        digits[-1] += 1
        return digits + newlst