class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

    def rob1(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return sum(nums)
        a, b, c, d = 0, 0, 0, nums[0]
        for i in nums[1: -1]:
            a, b, c, d = b, max(b, a + i), d, max(d, c + i)
        return max(b, a + nums[-1], d)