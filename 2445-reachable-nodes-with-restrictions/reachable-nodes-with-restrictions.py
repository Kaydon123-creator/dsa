class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        restricted = set(restricted)

        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        queue = deque()
        for node in range((n)):
            if node in restricted:
                continue
            queue.append(node)
            break 
        count = 0 
        seen = set()
        while queue:
            count+=1
            node = queue.popleft()
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen and not nei in restricted:
                    queue.append(nei)

        return count

        