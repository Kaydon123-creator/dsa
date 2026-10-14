class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        from math import sqrt
        points.sort(key = lambda x:sqrt((x[0]**2)+(x[1]**2)))

        return points[:k]
        