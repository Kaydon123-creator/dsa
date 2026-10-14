class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        seen = set()
        result = 0 
        def countMax(char):
            l = 0 
            count = 0 
            res = 0
            for r in range(len(s)):
                if s[r]!=char:
                    count+=1 
                while l < len(s) and count > k:
                    if s[l] != char:
                        count-=1
                    l+=1 
                res = max(r-l+1, res)
            return res

        for char in s:
            if char not in seen:
                result = max(result, countMax(char))
                seen.add(char)

        return result
                
        
        