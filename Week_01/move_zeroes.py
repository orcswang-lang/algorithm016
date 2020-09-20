class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        从数组头部开始循环,判断值是否等于0，如果是则弹出该值，并且在list末尾追加0，否则什么都不做，
        """
        pre_idx = 0
        n = len(nums)
        for i in range(n):
            idx = i-pre_idx
            if nums[idx] != 0:continue
            nums.pop(idx)
            nums.append(0)
            pre_idx += 1

    def moveZeroes1(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                i += 1
                continue
            nums.pop(i)
            nums.append(0)
            n -= 1

    def moveZeroes2(self, nums: List[int]) -> None:
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0: continue
            nums[i], nums[p] = nums[p], nums[i]
            p += 1

    def moveZeroes3(self, nums: List[int]) -> None:
        size, i = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                size += 1
            else:
                nums[i - size], nums[i] = nums[i], nums[i - size]
            i += 1