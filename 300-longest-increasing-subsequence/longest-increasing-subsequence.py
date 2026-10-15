class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        @cache 
        def dp(index):
            best = 1
            for i in range(index + 1, n):
                if nums[i] > nums[index]:
                    best = max(best ,1 + dp(i))
            return best

    
        return max([dp(i) for i in range(n)])
                