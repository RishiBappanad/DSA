class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        def area(left, right):
            return min(height[left], height[right]) * (right - left)
        best = area(l, r)
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            best = max(area(l, r), best)

        return best