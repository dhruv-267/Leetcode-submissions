class Twitter:

    def __init__(self):
        self.count = 0  #count/ timestamp attached to each tweet
        self.followmap = {} # key:value = userId : set(followeeID)
        self.tweetmap = {} #key:value = userId : [[tweetid,count]]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count-=1
        if userId not in self.tweetmap:
            self.tweetmap[userId] = [[tweetId,self.count]]
        else:
            self.tweetmap[userId].append([tweetId,self.count])

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followmap.get(userId,set())
        followees.add(userId)
        tweetlist = []
        for followee in followees:
            if followee in self.tweetmap:
                index = len(self.tweetmap[followee])-1
                tweetid, count = self.tweetmap[followee][index]
                tweetlist.append([count,tweetid,followee,index-1])
        heapq.heapify(tweetlist)
        feed = []
        while tweetlist and len(feed)<10:
            count , tweetid , followee, index = heapq.heappop(tweetlist)
            feed.append(tweetid)
            if index >= 0:
                tweetid, count = self.tweetmap[followee][index]
                heapq.heappush(tweetlist,[count,tweetid,followee,index-1])
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap and followeeId in self.followmap[followerId]:
            self.followmap[followerId].discard(followeeId)
        
