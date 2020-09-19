class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """双指针"""
        p1, p2 = 0, 0
        nums = nums1[:m]
        nums1[:] = []
        while p1 < m and p2 < n:
            if nums[p1] < nums2[p2]:
                nums1.append(nums[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n:
            if m and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1