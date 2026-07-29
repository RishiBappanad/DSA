class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(res[-1] * nums[i - 1]) if len(res) > 0 else res.append(1)
        suffix = 1
        print(res)
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            if i + 1 < len(res):
                suffix *= nums[i] 
            else:
                suffix = nums[-1]
        return res