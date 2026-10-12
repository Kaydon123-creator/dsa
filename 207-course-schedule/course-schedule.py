class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for x,y in prerequisites:
            indegree[x] +=1 
            graph[y].append(x)
        print(graph, indegree)
        queue = deque([])
        for i,x in enumerate(indegree):
            if x == 0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.popleft()
            print(node)
            count +=1 
            for neighbor in graph[node]:
                indegree[neighbor]-=1 

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return True if count == numCourses  else False