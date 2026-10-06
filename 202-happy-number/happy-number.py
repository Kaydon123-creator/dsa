class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = str(n)
            n = sum([int(x)**2 for x in n])
        return True if n == 1 else False 

        