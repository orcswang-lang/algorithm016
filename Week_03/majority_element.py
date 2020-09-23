class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """hash"""
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement1(self, nums: List[int]) -> int:
        """排序"""
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement2(self, nums: List[int]) -> int:
        """排序"""
        return sorted(nums)[len(nums) // 2]

    def majorityElement3(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            if res[num] > len(nums) // 2:
                return num
            else:
                res[num] += 1

    def majorityElement4(self, nums: List[int]) -> int:
        """分治"""
        def majority_element_rec(lo, hi):
            if lo == hi: return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            if left == right: return left

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right