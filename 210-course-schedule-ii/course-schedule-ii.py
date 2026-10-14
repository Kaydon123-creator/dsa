class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses 
        graph = defaultdict(list)
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x]+=1
        
        queue = deque()
        for num_course,degree in enumerate(indegree):
            if degree == 0:
                queue.append(num_course)
        
        res = [] 
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbor in graph[course]:
                indegree[neighbor]-= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return res if len(res) == numCourses else []

