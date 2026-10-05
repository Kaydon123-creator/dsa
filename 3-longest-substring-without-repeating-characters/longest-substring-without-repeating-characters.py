class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0 
        n = len(s)
        left = 0 
        right = 0
        dic = defaultdict(int)
        for right in range(n):
            dic[s[right]] +=1 
            while dic[s[right]] > 1 :
                dic[s[left]]-=1
                left+=1
            
            result = max(right - left + 1, result)
        return result


