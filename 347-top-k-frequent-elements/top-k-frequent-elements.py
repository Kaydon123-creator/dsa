class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        dic = Counter(nums)
        dic = dict(sorted(dic.items(),key = lambda x:x[1]))
        list1 = list(dic.keys())
        return list1[len(list(set(nums))) - k :]
        
        