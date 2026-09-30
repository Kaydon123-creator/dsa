class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i 
            

        for k in range(len(nums)):
            if target-nums[k] in dic and dic[target-nums[k]]!=k:
                return [dic[target-nums[k]],k]
                
        