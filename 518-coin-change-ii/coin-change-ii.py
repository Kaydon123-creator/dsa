class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        @cache 
        def dp(curr, index):
        
            if curr == amount:
                return 1
            if curr > amount or index == len(coins):
                return 0
            res = 0 
            
            res = dp(curr+coins[index], index)
            skip = dp(curr, index+1)

            return res+skip
        
        
        return dp(0,0)

        