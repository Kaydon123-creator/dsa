class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        result = [0]*n
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                index = stack.pop()[1]
                result[index] = (i-index)
            stack.append((temperatures[i], i))
        
        
        return result
