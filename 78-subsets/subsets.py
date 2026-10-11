class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        def backTrack(index, curr):
            result.append(curr[:])
            for i in range(index,n):
                curr.append(nums[i])
                backTrack(i+1,curr)
                curr.pop()
        backTrack(0,[])
        return result



            


        