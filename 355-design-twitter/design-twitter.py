class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0 

    

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts[userId], (-self.time, tweetId ))
        self.time+=1


    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = self.posts[userId][:]
        cnt = 0 


        for user in self.users[userId]:
           heap+= self.posts[user]
           
        heapq.heapify(heap)

        while heap and cnt< 10:
            cnt+=1 
            res.append(heapq.heappop(heap)[1])
        
        return res
         
         
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
       
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
       

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)