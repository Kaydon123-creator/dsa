class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        def dfs(i):
            seen.add(i)
            for key in rooms[i]:
                
                if key not in seen:
                    dfs(key)
                      
        dfs(0)
        print(seen)
        return True if len(seen)==len(rooms) else False