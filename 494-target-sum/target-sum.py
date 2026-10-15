class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        res = 0
        cache = {}
        def dp(index, curr):
            if (index,curr) in cache:
                return cache[(index,curr)]
            if curr == target and index == n:
                return 1
            if index >= n:
                return 0

            res1 = dp(index+1,curr + nums[index]) 
            res2 = dp(index+1,curr - nums[index])
            cache[(index+1,curr+nums[index])] = res1 
            cache[(index+1,curr-nums[index])] = res2 
            return res1+res2
            
        return dp(0,0)






        