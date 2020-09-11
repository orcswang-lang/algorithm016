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