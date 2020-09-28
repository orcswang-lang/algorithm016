class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(first = 0):
            # 全部数字都填完毕
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                helper(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        helper()
        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        res = []
        backtrack(nums, [])
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        if len(nums) == 1: return [nums]
        ans = []
        for i, num in enumerate(nums):
            ans.extend([[num] + p for p in self.permute(nums[:i] + nums[i + 1:])])
        return ans

    def permute3(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums: List[int], size: int, depth: int, path: List[int], state: int, res: List[int]):
            if depth == size:
                res.append(path)
                return

            for i in range(size):
                if ((state >> i) & 1) != 0: continue
                dfs(nums, size, depth + 1, path + [nums[i]], state ^ (1 << i), res)

        size = len(nums)
        if size == 0: []

        state = 0
        res = []
        dfs(nums, size, 0, [], state, res)

        return res

    def permute4(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))