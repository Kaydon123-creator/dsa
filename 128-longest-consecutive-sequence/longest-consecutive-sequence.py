class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        res = 0 
        ans = 0 
        nums = list(set(nums))
        for num in nums:
            if num-1 in seen:
                continue
            else:
                curr = 1
                while num+1 in seen:
                    curr+=1
                    num = num+1 
                res = max(res,curr)
        return res

                    

        

        