class Solution:
    def jump(self, nums: list[int]) -> int:
        left = right = 0 
        n =len(nums)
        result = 0 
        next = 0 
        j = 0 
        while right < n - 1:
            for i in range(left, right + 1):
                next = max(nums[i]+ i, next)
            left = right + 1 
            right = next 
            
            result+= 1 
        return result 


            

        