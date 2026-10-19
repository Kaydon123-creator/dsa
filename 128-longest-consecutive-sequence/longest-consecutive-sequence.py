class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        #store distinct numbers
        set_of_nums = set(nums)

        #remove duplicates 
        nums = list(set_of_nums)

        result = 0 

        for num in nums:

            if num - 1 in set_of_nums:
                continue 
            curr = 1 
            #num is the start of a new_subsequence
            start = num 
            #tcheck if successor is in the array  
            while start + 1 in set_of_nums:
                start+=1 
                curr+=1 

            result = max(result, curr)

        return result 


            
       

        

        