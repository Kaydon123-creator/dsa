class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        result = 0 
        @cache
        def dfs(index):
            nonlocal result
            if index == n:
                return 1
            curr = ""
            for i in range(index, n):
                if s[i] == "0" and not curr:
                    break
                curr += (s[i])
                if int(curr) <= 26 :
                    result+= dfs(i+1)
                else:
                    break 
            return result 
                
        dfs(0)
        return result
                

        