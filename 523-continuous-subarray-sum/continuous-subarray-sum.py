class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        prefix = {}
        curr = 0
        for i,num in enumerate(nums):
            curr += num
            reminder = curr % k
            if reminder in prefix:
                if i - prefix[reminder]> 1:
                    return True 
            else :
                prefix[reminder] = i 
                
            if reminder == 0 and i > 0:
                return True

            
        return False


