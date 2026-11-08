class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:



                    
            @cache

            def dp(cumul):
                if cumul == amount:
                    return 0
                if cumul>= amount:
                    return -1

                ans = float("inf")

                for c in coins:
                    res = dp(cumul + c)
                    ans = min(1 + dp(cumul + c), ans) if dp(cumul+c) != -1 else ans

                return ans if ans != float("inf") else -1


            return dp(0)

            

       
        