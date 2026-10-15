class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        res = nums[0]
        curr = 1
        for num in nums:
            curr *= num 
            res = max(curr, res)
            if num == 0:
                curr =1 
            
        curr = 1 
        for num in nums[::-1]:
            curr *= num
            res = max(res,curr)
            if num == 0:
                curr = 1 
            
        return res

      