class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        cache = {}
        
        def dp(level, i):
            if (level,i) in cache:
                return cache[(level,i)]
            if level == n -1 :
                cache[(level, i)] = triangle[level][i]
                return triangle[level][i]

            left = dp(level+1,i)
            right = dp(level+1, i+1)
            cache[(level, i)] = triangle[level][i] + min(left, right)
            return triangle[level][i] + min(left, right)

        return dp(0,0)

        
        