class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        temp = []
        i = 0 
        while i < len(nums):
            j = i 
            while j < len(nums)-1 and nums[j+1] == nums[j] +1 :
                j+=1
            if j!=i:
                temp.append(str(nums[i])+"->"+str(nums[j]))
            else:
                temp.append(str(nums[j]))
            i = j + 1
        return temp
        
        