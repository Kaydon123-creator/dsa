class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))
        
        stops = [float("inf")]*n
        min_heap=[(0,0, src)]
    
        while min_heap:
            distance, steps, node = heapq.heappop(min_heap) 
            
            if stops[node] <= steps or steps > k + 1:
                continue
            if node == dst:
                return distance
            if steps == k + 1:
                continue

            stops[node] = steps

            for neighbor, cost in graph[node]:
                heapq.heappush(min_heap,(distance+cost, steps+1, neighbor) )
            
        return -1 


        