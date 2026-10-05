class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse= True)
        n = len(citations)
        i = 0
        count= 0
        while i < n and citations[i] > count :
            i+=1
            count+=1
           
        return count
           