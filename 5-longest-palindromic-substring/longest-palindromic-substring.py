class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        result = "" 
        def extend(l,r):
            while l>= 0 and r<n and s[l] == s[r]:
                l-=1 
                r+=1 
            return s[l+1:r] 
        
        for i in range(n):
            s1 = extend(i,i)
            s2 = extend(i,i+1)
            
            if len(s1) > len(result):
                result = s1
            if len(s2) > len(result):
                result = s2
        return result
        

            
       
        
           
            
            
                            
                        




        