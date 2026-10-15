class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        res = 0
        @cache
        def dp(index, curr):
            nonlocal res
            if curr == target and index == n:
                return 1
            if index >= n:
                return 0

            return dp(index+1,curr + nums[index]) + dp(index+1,curr - nums[index])
            
        return dp(0,0)






        