class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = [] 
        n = len(candidates)
        candidates.sort() 
        print(candidates)


        def backTrack(debut, curr):
            if sum(curr)> target:
                return 
            if sum(curr) == target:
                result.append(curr[:])
                return 
    
            for i in range(debut, n):
                if i > debut and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backTrack(i+1, curr)
                curr.pop()
        backTrack(0,[])
        return result
        