class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        def findNext(i):
            for j in range(i+1, len(nums2)):
                if nums2[j]>nums2[i]:
                    return nums2[j]
            else:
                return -1
        for x in nums1:
            for i in range(len(nums2)):
                if nums2[i]==x:
                    result.append(findNext(i))
        return result

       
        