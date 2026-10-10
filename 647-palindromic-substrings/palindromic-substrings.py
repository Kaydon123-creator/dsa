class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        def check_palindrom(l,r): 
            nonlocal res
            while 0<=l and r< n and s[l]==s[r]:
                res+=1 
                l-=1 
                r+=1 

        for i in range(n):
            check_palindrom(i,i)
            check_palindrom(i,i+1)

        return res

        