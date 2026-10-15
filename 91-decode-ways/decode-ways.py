class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def dp(i):
            if i>=n:
                return 1
            res = 0
            if int(s[i]) == 0:
                return 0
            res = dp(i+1) 
            if i < n - 1 and int(s[i]+s[i+1]) <= 26:
                res+= dp(i+2)
            
            return res

        return dp(0)


        
                

        