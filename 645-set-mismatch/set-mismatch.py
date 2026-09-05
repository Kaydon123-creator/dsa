class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        nums1 = set(nums)
        dic = Counter(nums)
        doublon = [x for x,n in dic.items() if n > 1]
        nums2 = [x for x in range(1,len(nums)+1) if x not in nums1]

        
        return doublon + nums2
        