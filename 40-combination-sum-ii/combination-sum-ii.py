class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = [] 
        n = len(candidates)
        candidates.sort() 
        print(candidates)


        def backTrack(debut, curr, curr_sum):
            if curr_sum> target:
                return 
            if curr_sum == target:
                result.append(curr[:])
                return 
    
            for i in range(debut, n):
                if i > debut and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                curr_sum+= candidates[i]
                backTrack(i+1, curr, curr_sum)
                curr_sum -= curr.pop()
        backTrack(0,[], 0)
        return result
        