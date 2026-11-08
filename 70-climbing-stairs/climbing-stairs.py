class Solution:
    def climbStairs(self, n: int) -> int:
        

        @cache
        def dp(m):
            if m == n :
                return 1
            if m >= n :
                return 0 

            return dp(m+1) + dp(m+2)

        return dp(0)




     