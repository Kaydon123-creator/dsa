class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        n = len(candidates)
        def backTrack(debut, remain, lst ):
            print((debut, remain, lst))
            if remain > target:
                return 
            elif remain == target :
                result.append(lst[:])
                return 
            for i in range(debut,n ):
                remain += candidates[i]
                lst.append(candidates[i])
                backTrack(i, remain, lst )
                remain-=lst.pop()
        backTrack(0, 0, [])
        return result 
        