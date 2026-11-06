class Solution:
    def alienOrder(self, words: list[str]) -> str:

        graph = defaultdict(set)
        indegree = {c:0 for word in words for c in word }
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if w1.startswith(w2):
                if len(w1) > len(w2):
                    return "" 
            
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    if w2[i] not in graph[w1[i]]:
                        graph[w1[i]].add(w2[i])
                        indegree[w2[i]]+=1
                    break 
 
        queue = deque([c for c in indegree if indegree[c] == 0])
        ans = ""
        count = 0 
        while queue:
            letter = queue.popleft()
            count+=1
            ans += letter
            print(ans) 
            for nei in graph[letter]:
                indegree[nei]-=1 
                if indegree[nei] == 0 : 
                    queue.append(nei)
        return ans if count == len(indegree) else ""
            


        