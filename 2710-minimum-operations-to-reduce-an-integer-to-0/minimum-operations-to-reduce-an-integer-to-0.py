
class Solution:

    def minOperations(self, n: int) -> int:
        from math import log2
        if n == 0:
            return 0
        if log2(n) % 1 == 0:          # n is a power of 2
            return 1
        
        d1 = n - pow(2, int(log2(n)))
        d2 = pow(2, int(log2(n)+1)) - n  

        return 1 + min(self.minOperations(d1),self.minOperations(d2))
        

    
        