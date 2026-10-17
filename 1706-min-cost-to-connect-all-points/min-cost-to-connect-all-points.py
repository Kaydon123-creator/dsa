class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        ## prim's algorithm 
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            x,y = points[i]
            for j in range(i+1,n):
                a,b = points[j]
                manhattan = abs(x-a) + abs(y-b)
                graph[(x,y)].append((a,b,manhattan))
                graph[(a,b)].append((x,y,manhattan))

        min_heap = [(0,points[0])]
        result = 0 
        seen = set()
        while min_heap:
            distance,(i,j)  = heapq.heappop(min_heap)
            if (i,j) in seen:
                continue 
                
            seen.add((i,j))

            result+= distance 

            n-=1 

            if n==0 :
                return result

            for x,y,cost in graph[(i,j)]:
                if (x,y) not in seen:
                    heapq.heappush(min_heap, (cost, (x,y)))
        
        return -1
        





        