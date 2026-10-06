class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic :
                dic[nums[i]] = i
            else: 
                if abs(dic[nums[i]] - i) <= k:
                    return True
                dic[nums[i]]= i 
        return False
        