class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        shortest = {x:float("inf") for x in range(1,n+1)}
        shortest[k] = 0
        min_heap = [(0,k)]

        while min_heap:
            weight,node = heapq.heappop(min_heap)

            for neighbor, cost in graph[node]:
                new_weight = cost + weight
                if new_weight < shortest[neighbor]:
                    shortest[neighbor] = new_weight
                    heapq.heappush(min_heap,(new_weight, neighbor))
        
       
        if float("inf") not in shortest.values():
            return max(shortest.values())
        else:
            return -1


        

        
       