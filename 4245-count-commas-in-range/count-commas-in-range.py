class Solution:
    def countCommas(self, n: int) -> int:
        result = 0
        if n//1000:
            result+= n - 1000 + 1 
        return result

        