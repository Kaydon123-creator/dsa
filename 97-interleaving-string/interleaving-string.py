class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False
        @cache
        def dp(i,j):
            if i+j == len(s3):
                return True
            if i < len(s1) and s3[i+j] == s1[i]:
                if dp(i+1,j):
                    return True
            if j < len(s2) and s3[i+j] ==s2[j]:
                if dp(i,j+1):
                    return True 
                
            return False
        return dp(0,0)





        
                
                




        
