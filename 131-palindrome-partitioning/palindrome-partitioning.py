class Solution:
    def partition(self, s: str) -> list[list[str]]:

        def is_palindrom(s):
            l = 0 
            r = len(s) - 1

            while l < r  :
                if s[l]==s[r]:
                    l+=1 
                    r-=1 
                else:
                    return False 
            return True
        result = []

        def backtrack(index, partition):
            if index >= len(s):
                result.append(partition[:])
            for i in range(index, len(s)):
                
                if is_palindrom(s[index:i+1]):
                    partition.append(s[index:i+1])
                    backtrack(i+1, partition)
                    partition.pop()
        backtrack(0,[])

        return result


        


        