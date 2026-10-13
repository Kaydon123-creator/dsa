class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(k,path, i,j):
            if board[i][j]!= word[k]:
                return False
                
            if len(word)-1 == k:
                return True
            if k >= len(word):
                return False
            for r,c in directions:
                new_i , new_j = i+r, j+c
                if 0<= new_i < n and 0 <= new_j < m and (new_i,new_j) not in path:
                            path.add((new_i,new_j))
                
                            if dfs(k+1,path, new_i,new_j):
                                return True
                  
                            path.remove((new_i, new_j))
            return False 

        for i in range(n):
            for j in range(m):
                if dfs(0,{(i,j)},i,j):
                    return True
        return False

        
                        

                
                    


        