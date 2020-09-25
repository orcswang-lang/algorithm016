# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]ß
#
#  Related Topics 数组 哈希表
#  👍 9064 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        length = len(nums)
        for i in range(length):
            if target - nums[i] not in idx:
                idx[nums[i]] = i
                continue
            return idx[target - nums[i]], i

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, num in enumerate(nums):
            if target - num not in idx:
                idx[num] = i
                continue
            return idx[target - num], i
# leetcode submit region end(Prohibit modification and deletion)
