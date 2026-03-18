class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == False:
            return False
        dp = [None] * len(nums)
        def dfs(i): 
            jumps = nums[i]
            for j in range(jumps, -1, -1):
                if i + j >= len(nums):
                    dp[i] = True
                    return True
                if dp[i + j]:
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = True
            dfs(i)
        print(dp)
        return dp[0]
