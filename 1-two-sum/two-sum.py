class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(len(nums)):
            
            if (target - nums[i]) not in dic:
           
                dic[(target - nums[i])] = i 
            if nums[i] in dic and dic[nums[i]] != i:
                return [i, dic[nums[i]]]
          
     
      