class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        min_heap = [float("inf")]
        intervals.sort()
        n = len(intervals)
        count = 0
        print(intervals)
        for i in range(n):
            if intervals[i][0] < min_heap[0]:
                count+=1
            else:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap,intervals[i][1])

        return count


            
        