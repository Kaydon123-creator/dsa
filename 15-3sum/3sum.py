class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        def twoSum(i,res):
            left = i+1 
            right = n - 1
            total = res 
            while left < right:
                total = (nums[left] + nums[right]+ nums[i])
                if total > 0:
                    total -= nums[right]
                    right -= 1
                elif total < 0:
                    total -= nums[left]
                    left+= 1 
                else:
                    print(total, [nums[i], nums[left], nums[right]])
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    while left < right and (nums[left]==nums[left-1]):
                        left+=1
                    right-= 1
                    
            

        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            twoSum(i, nums[i])


        
        
        return result
            



            
                