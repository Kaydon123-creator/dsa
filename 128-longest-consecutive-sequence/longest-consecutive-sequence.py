class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        output = 0
        if len(nums) <= 1:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                result+=1
                print(nums[i], result)
            elif nums[i] == nums[i+1]:
                continue
            else:
                result = 0 
            output = max(output, result)
        return output + 1
        

        