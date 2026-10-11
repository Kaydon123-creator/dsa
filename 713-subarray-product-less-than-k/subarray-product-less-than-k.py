class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        left = right = 0 
        curr = 1
        res = 0
        for right in range(len(nums)):
            curr*= nums[right]
            while curr >= k:
                curr //=nums[left]
                left+=1 
            res+=right-left+1 
        return res
        

        