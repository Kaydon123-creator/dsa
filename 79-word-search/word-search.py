class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        seen = set()
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        n = len(board)
        m = len(board[0])
        def dfs(i,j,k):
            k+=1

            if k > len(word):
                return False

            if k == len(word):
                return True 
            
            for r,c in directions:
                new_i = r + i
                new_j = c + j 
                if 0<=new_i<n and 0<=new_j<m and (new_i,new_j) not in seen and board[new_i][new_j]==word[k]:
                    seen.add((new_i,new_j)) 
                    if dfs(new_i, new_j, k):
                        return True
                    seen.remove((new_i,new_j))
            return False

            
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and (i,j) not in seen:
                    seen.add((i,j))
                    if dfs(i,j, 0):
                        return True
                    seen.remove((i,j))
        return False
        


            

       