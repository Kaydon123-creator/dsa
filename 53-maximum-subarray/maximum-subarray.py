class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        curr = maxi = nums[0] 
        
        for num in nums[1:]:
            curr = max(curr+num, num)
            maxi = max(maxi, curr)
        return maxi
        
        