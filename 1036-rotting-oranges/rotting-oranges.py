class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque([])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j))
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        while queue:
            k = len(queue)
            for _ in range(k):
                (i,j) = queue.popleft()
                for r,l in directions:
                    new_i, new_j = i+r, j+l
                    if 0<=new_i<n and 0<=new_j<m and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        queue.append((new_i,new_j))
            count+=1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return  max(0, count - 1)
            
                    

                

        





        