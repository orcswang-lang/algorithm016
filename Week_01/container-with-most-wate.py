class Solution:
    def maxArea(self, height: List[int]) -> int:
        """双指针"""
        l, r, ans = 0, len(height) - 1, 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

    def maxArea1(self, height: List[int]) -> int:
        """双指针"""
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

    def maxArea2(self, height: List[int]) -> int:
        """双指针"""
        i, j, water = 0, len(height) - 1, 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water