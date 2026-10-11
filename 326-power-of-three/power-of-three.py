class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        import math
        x = round(math.log(abs(n), 3))

        
        return True if 3 ** x == n else False 
        
            
        