class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        target = sum(nums)/2

        if target%1!=0:
            return False
        print(target)
        @cache
        def dp(i, curr):
            if curr == target :
                return True 
            if i >= n:
                return False
            if curr >= target:
                return False

            return dp(i+1,nums[i]+ curr) or dp(i+1, curr)

        
        return dp(0,0)

            

   