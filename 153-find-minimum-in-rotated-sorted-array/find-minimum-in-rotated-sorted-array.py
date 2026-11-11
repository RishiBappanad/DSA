class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        med = (l + r) // 2
        while nums[r] < nums[l]:
            med = (l + r) // 2
            if nums[med] > nums[l]:
                l = med + 1
            else:
                r = med
        return nums[med + 1]