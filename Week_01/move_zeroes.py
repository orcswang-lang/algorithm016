class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre_idx = 0
        n = len(nums)
        for i in range(n):
            idx = i-pre_idx
            if nums[idx] != 0:continue
            nums.pop(idx)
            nums.append(0)
            pre_idx += 1