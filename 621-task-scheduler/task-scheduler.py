class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        from collections import Counter
        queue = deque()
        count = Counter(tasks)
        heap = [-x for x in count.values()]
        heapq.heapify(heap)
        time = 0 
        while queue or heap:
            time +=1
            if heap:
                task = heapq.heappop(heap) + 1
                if task:
                    queue.append((task, n + time))
            if queue and queue[0][1] == time:
                task = queue.popleft()[0]
                heapq.heappush(heap,task)
        return time
            
                 
            
            




        


            
        