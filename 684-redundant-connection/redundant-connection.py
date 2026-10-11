class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        graph = defaultdict(list)
        visited = set()
        flag =False 
        def dfs(node, parent, visited):
            nonlocal flag
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor not in visited:
                    dfs(neighbor, node, visited)
                else:
                    flag = True
            return flag
        
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
            visited = set()
            if dfs(node, 1, visited):
                return (node, neighbor)
        return -1
            
                
        
            