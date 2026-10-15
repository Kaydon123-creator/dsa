class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
       
        words = set(wordDict)
        queue = deque([0])
        n = len(s)
        seen = set()
        @cache
        def dp(index):
            if index == n:
                return True

            for i in range(index, n):
                if s[index:i+1] in words:
                    if dp(i+1):
                        return True
            return False

        return dp(0)
                



# a a a b 

# a aa  
 

                       






