class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for n in range(1, n+1):
            divisible_by_3 = (n % 3 == 0)
            divisible_by_5 = (n % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(n))
        return ans

    def fizzBuzz1(self, n: int) -> List[str]:
        ans = []
        for n in range(1, n + 1):
            divisible_by_3 = (n % 3 == 0)
            divisible_by_5 = (n % 5 == 0)
            num_ans_str = ""
            if divisible_by_3:
                num_ans_str += "Fizz"
            if divisible_by_5:
                num_ans_str += "Buzz"
            if not num_ans_str:
                num_ans_str += str(n)
            ans.append(num_ans_str)
        return ans

    def fizzBuzz2(self, n: int) -> List[str]:
        """基于字典特性"""
        ans = []
        fizz_buzz_dict = collections.OrderedDict()
        fizz_buzz_dict[3] = "Fizz"
        fizz_buzz_dict[5] = "Buzz"
        for n in range(1, n + 1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():
                if n % key == 0:
                    num_ans_str += fizz_buzz_dict[key]
            if not num_ans_str:
                num_ans_str += str(n)
            ans.append(num_ans_str)
        return ans

    def fizzBuzz3(self, n: int) -> List[str]:
        res = []
        num_tuple_list = [(15, 'FizzBuzz'), (3, 'Fizz'), (5, 'Buzz'), (1, '')]
        for num in range(1, n + 1):
            for div, char in num_tuple_list:
                if num % div == 0:
                    res.append(str(num) if div == 1 else char)
                    break

        return res

    def fizzBuzz4(self, n: int) -> List[str]:
        """
        列表推导,根据余数取反进行拼接字符
        :param n:
        :return:
        """
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]