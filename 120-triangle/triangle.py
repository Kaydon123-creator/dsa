class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        @cache
        def dp(level, i):
            if level == n -1 :
                return triangle[level][i]

            left = dp(level+1,i)
            right = dp(level+1, i+1)

            return triangle[level][i] + min(left, right)

        return dp(0,0)

        
        