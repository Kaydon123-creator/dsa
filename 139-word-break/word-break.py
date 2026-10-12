class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        queue = deque([0])
        seen = set(wordDict)
        visited = set()
        while queue:
            index = queue.popleft()
  
            if index == len(s):
                return True
            
            for i in range(index + 1, len(s)+1):
                if i not in visited and s[index:i] in seen:
                    visited.add(i)
                    print(s[index:i], index, 1)
                    queue.append(i)

        return False
            

        