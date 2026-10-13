from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findMin(nums):
            l = 0 
            r = len(nums)-1
            while l< r:
                mid = (l+r)//2

                if nums[mid] > nums[r]:
                    l = mid+1 
                else:
                    r = mid 
            return l 
        pivot = findMin(nums)

        def binarySearch(left,right, target):
            l = left
            r = right-1 
            while l<= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                if target > nums[mid] :
                    l = mid +1 
                else:
                    r = mid - 1
            return -1 
        if pivot == 0:
            return binarySearch(0, len(nums), target)
        if target >= nums[0] and target <= nums[pivot-1] :
            return binarySearch(0,pivot, target)
        else:
            return binarySearch(pivot, len(nums), target)
            

