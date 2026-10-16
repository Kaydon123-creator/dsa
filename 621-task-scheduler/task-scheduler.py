class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        from collections import Counter 
        count = Counter(tasks)
        max_heap = [-x for x in count.values()]
        heapq.heapify(max_heap)
        queue = deque()
        time = 0 
        while queue or max_heap:
            time+=1
            if max_heap:
                process = -(-heapq.heappop(max_heap) - 1 )
                if process != 0:
                    queue.append((process,time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap,queue.popleft()[0])
        return time 


            


        
                 
            
            




        


            
        