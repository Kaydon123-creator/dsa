class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        l = 1 
        r = len(nums) 

        while l<r:
            mid = (l+r)//2
            count = 0 
            for num in nums:
                if num <= mid:
                    count+=1 
            if count > mid:
                r = mid 
            else:
                l = mid + 1 
        
        return l
            