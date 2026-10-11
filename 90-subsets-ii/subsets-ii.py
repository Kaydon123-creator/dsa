class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        seen = set()
        nums.sort()
        def backtrack(curr, index):
            print(index, curr)
            ans = tuple(curr)
            if ans not in seen:
                seen.add(ans)
                result.append(curr[:])
            else : 
                return 
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        backtrack([],0)
        return result
        