# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针
#  👍 2560 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            s, e = i + 1, N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    while s < e and nums[s] == nums[s - 1]:
                        s = s + 1
                elif nums[s] + nums[e] < target:
                    s = s + 1
                else:
                    e = e - 1
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        # 先排序，关键！
        nums.sort()
        ans = set()
        N, target = 3, 0
        self._find_sum(nums, 0, N, target, [], ans)
        return list(ans)

    def _find_sum(self, nums, start, N, target, path, ans):
        # terminator
        if len(nums) < N or N < 2: return
        # process
        if N == 2:
            # 两数求和
            d = set()
            for j in range(start, len(nums)):
                if target - nums[j] in d:
                    ans.add(tuple(path + [target - nums[j], nums[j]]))
                else:
                    d.add(nums[j])
        else:
            for i in range(start, len(nums)):
                # 剪枝1: target比剩余数字能组成的最小值还要小 或 比能组成的最大值还要大，就可以停止循环了
                if target < nums[i] * N or target > nums[-1] * N: break
                # 剪枝2: 去重
                if i > start and nums[i] == nums[i - 1]: continue
                # drill down
                self._find_sum(nums, i + 1, N - 1, target - nums[i], path + [nums[i]], ans)
        return
# leetcode submit region end(Prohibit modification and deletion)
