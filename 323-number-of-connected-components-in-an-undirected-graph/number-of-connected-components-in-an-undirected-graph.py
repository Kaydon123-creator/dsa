class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        rank = [0]*n
        parent = list(range(n))

  
        def find(n1):
            res = n1 
            while res!=parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(a1,b1):
            root1 = find(a1)
            root2 = find(b1)
            if root1==root2:
                return
            if rank[root1]>rank[root2]:
                parent[root2]= root1
            elif rank[root1]<rank[root2]:
                parent[root1] = root2
            else:
                parent[root1] = root2
                rank[root2]+=1
        
            
        
        for x,y in edges:
            union(x,y)
            
    
        return len(list(set(find(i) for i in range(n))))
            



        