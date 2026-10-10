class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

        count = 0
        heap = [((nums1[0]+nums2[0]), 0 , 0)]
        heapq.heapify(heap)
        result = []
        seen = set()
        while count < k:
            elem,i,j = heapq.heappop(heap)
        
            result.append((nums1[i],nums2[j]))
            if i < len(nums1) -1 and (i+1,j) not in seen:
                seen.add((i+1,j))
                heapq.heappush(heap,(nums1[i+1]+ nums2[j], i+1, j))
            if j < len(nums2) - 1 and (i,j+1) not in seen:
                seen.add((i,j+1))
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
            count+=1 
      
        return result
            

        