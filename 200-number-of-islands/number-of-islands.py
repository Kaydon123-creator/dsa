class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        island = 0 
        def dfs(i,j):
            if (i,j) in seen:
                return 
            seen.add((i,j))
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for l,r in directions:
                if 0<=i+l< len(grid) and 0<=j+r< len(grid[0]) and (i+l,j+r) not in seen and grid[i][j]=="1":
                    dfs(i+l, j+r)
                      
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j)
                    island+=1

        return island
        