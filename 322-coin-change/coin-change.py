class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def dp(remain):
            result = float("inf")
            if remain == 0:
                return 0
            if remain < 0:
                return float(inf)
            for coin in coins :
                result = min(result, 1+ dp(remain-coin))
            return result
        ans = dp(amount) 
        return ans if ans != float(inf) else -1
        