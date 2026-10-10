class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr_sum = 0 
        result = 0
        for num in nums:
            curr_sum+=num
            if curr_sum-k in prefix:
                result+= prefix[curr_sum-k]
            prefix[curr_sum]+=1
        return result
            
# 1 1 -1 1 

# 3


        



        