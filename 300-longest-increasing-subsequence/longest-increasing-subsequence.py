class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        @cache
        def dp(index):
            ans = 1
            for i in range(index+1,n):
                if nums[i] > nums[index]:
                    res = dp(i)
                    ans = max(1+ res, ans)
            return ans

        return max([dp(i) for i in range(n)])

      