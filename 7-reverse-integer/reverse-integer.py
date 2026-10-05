class Solution:
    def reverse(self, x: int) -> int:
        neg = ""
        if x < 0:
            neg = "-"
            x = str(x)[1:]
        else:
            x = str(x)

        x = x[::-1]
        x = int(neg+x)
        return x if x >= -(2**31 - 1) and x < (2**31 - 1) else 0
        