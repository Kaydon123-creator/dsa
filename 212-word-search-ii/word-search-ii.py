class Node():
    def __init__(self):
        self.isend = False
        self.childrens = {}

class Solution:
    def __init__(self):
        self.root = Node()
        self.path = ""

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        def buildTree(words):
            for word in words:
                root = self.root
                for c in word:
                    if c not in root.childrens:
                        root.childrens[c] = Node()
                    root = root.childrens[c]
                root.isend = True

        def search(i,j,root):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return 
            
            if board[i][j] == "#" or board[i][j] not in root.childrens:
                return 
            
            c = board[i][j] 
            board[i][j] = "#"
            self.path += c

            node = root.childrens[c]
            if node.isend:
                result.add(self.path)
                
           
            search(i+1,j, node) 
            search(i,j+1, node)  
            search(i,j-1, node)  
            search(i-1,j, node)
            board[i][j] = c
            self.path = self.path[:-1]

        buildTree(words)
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.path = ""
                search(i,j,self.root)
        return list(result)

                    

            
        

                

                

                

        