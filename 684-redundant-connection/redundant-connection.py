class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        rank = [0] * (n+1)
        parents = list(range(n+1))

        def find(n1):
            res = n1 
            while res!= parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res] 
        
            return res 

        def union(n1,n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1 == root2:
                return False
            
            if rank[root1] > rank[root2]:
                parents[root2] = root1 
            elif rank[root1] < rank[root2]:
                parents[root1] = root2
            else:
                parents[root2] = root1 
                rank[root1]+=1 
            return True

        for x,y in edges:
            res = union(x,y)
            if not res:
                return (x,y)
            
        
        
            
                
        
            