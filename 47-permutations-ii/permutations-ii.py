class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        seen = set()

        def backtrack(curr, path):
            if len(curr) == len(nums) and tuple(curr) not in seen:
                ans.append(curr[:])
                seen.add(tuple(curr))
                return
           
            for i in range(len(nums)):
                if i not in path:
                    curr.append(nums[i])
                    path.add(i)
                    backtrack(curr, path)
                    curr.pop()
                    path.remove(i)

        ans = []
        backtrack([], set())
        return ans