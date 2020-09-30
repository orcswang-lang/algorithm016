class Solution:
    def jump(self, nums: List[int]) -> int:
        """贪心，正向查找可到达的最大位置"""
        ans, end, max_pos = 0, 0, 0

        for i in range(len(nums) -1):
            max_pos = max(nums[i] + i, max_pos)
            if i == end:
                end = max_pos
                ans += 1
        return ans

    def jump1(self, nums: List[int]) -> int:
        start = end = step = 0
        while end < len(nums) - 1:
            start, end = end + 1, max([i + nums[i] for i in range(start, end + 1)])
            step += 1
        return step