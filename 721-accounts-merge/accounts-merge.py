class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = defaultdict(list)
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
        result = []
        
        def dfs(node,):
            path.add(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in path:
                    dfs(neighbor)

        visited = set()
        for account in accounts:
            name = account[0]
            path = set()
            email = account[1]
            if email in visited:
                continue
            dfs(email)
            result.append([name]+sorted(list(path)))
            
        return result
            

            

       


        