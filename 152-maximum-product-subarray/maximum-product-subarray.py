class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = curr_min = 1
        for i in nums:
            best = curr_max * i
            curr_max = max(best, curr_min * i, i)
            curr_min = min(best, curr_min * i, i)
            res = max(res, curr_max)
        return res
