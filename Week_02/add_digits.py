class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            count =0
            while num >0:
                count += num % 10
                num //=10
            num = count
        return num

    def addDigits1(self, num: int) -> int:
        if num < 9: return num
        n = num % 9
        if n == 0: return 9
        return n

    def addDigits2(self, num: int) -> int:
        while num > 9:
            num = sum([int(digit) for digit in str(num)])
        return num

    def addDigits3(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num != 0 else 0

    def addDigits4(self, num: int) -> int:
        res = num % 9
        return res if res != 0 or num == 0 else 9

    def addDigits5(self, num: int) -> int:
        return num % 9 or 9 * bool(num)