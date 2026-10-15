class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
       
        words = set(wordDict)
        queue = deque([0])
        n = len(s)
        seen = set()
        while queue:
            index = queue.popleft()
            if index == n:
                return True
            
            for i in range(index, n):
                if s[index:i+1] in words and (i+1) not in seen:
                    seen.add((i+1))
                    queue.append(i+1)
            
        return False
                







