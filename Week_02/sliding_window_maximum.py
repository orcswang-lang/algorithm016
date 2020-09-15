class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        暴力法
        :param nums:
        :param k:
        :return:
        """
        if not nums: return []
        idx, max_nums = 0, []
        while idx <= len(nums) - k:
            max_nums.append(max(nums[idx:idx+k]))
            idx = idx + 1
        return max_nums

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        """双端队列"""
        deque = collections.deque()
        max_nums = []
        for i, n in enumerate(nums):
            while deque and nums[deque[-1]] < n:
                deque.pop()
            deque += i,
            if deque[0] == i - k:
                deque.popleft()
            if i >= k - 1:
                max_nums += nums[deque[0]],
        return max_nums

    def maxSlidingWindow4(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k):  # 未形成窗口
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)):  # 形成窗口后
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res