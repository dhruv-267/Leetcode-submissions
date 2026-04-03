class Twitter:

    def __init__(self):
        self.timer = 0  #timestamp of each post
        self.followmap = {} # key:value = followerId : set(followeeId) #O(1)
        self.tweetmap = {}  # key : value = userId : list[[tweetid,timer] 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer-=1
        if userId not in self.tweetmap:
            self.tweetmap[userId] = [[tweetId,self.timer]]
        else:
            self.tweetmap[userId].append([tweetId,self.timer])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetlist = []
        followees = self.followmap.get(userId,set())
        followees.add(userId)
        for followee in followees:
            if followee in self.tweetmap:
                tweetid , timer = self.tweetmap[followee][-1]
                tweetlist.append([timer,tweetid,followee,len(self.tweetmap[followee])-2])
        heapq.heapify(tweetlist)

        feed = []
        while tweetlist and len(feed) <10:
            timer , tweetid, followee, index = heapq.heappop(tweetlist)
            feed.append(tweetid)
            if index>=0:
                tweetid , timer = self.tweetmap[followee][index]
                heapq.heappush(tweetlist,[timer,tweetid,followee,index-1])
        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
        
