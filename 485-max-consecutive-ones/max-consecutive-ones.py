class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        left = 0 
        for right in range(len(nums)):
            if nums[right]==0:
                while left <= right:
                    left+=1
            print(result, left, right )
            result = max(result, right-left+1)
        return result
        