class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        @cache
        def dp(index):
            result = 1
            for i in range(index + 1, n):
                if nums[i]> nums[index]:
                    result = max(result,1+dp(i))
            return result 
        return max([dp(i) for i in range(n)])
            





       
       