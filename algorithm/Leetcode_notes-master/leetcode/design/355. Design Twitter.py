class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_list = {}
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.user_list:
            # post，关注的人
            self.user_list[userId] = [[], []]
        self.user_list[userId][0].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.user_list:
            return []
        follow = self.user_list[userId][1]
        result = self.merge(follow, userId)
        return result

    def merge(self, user_follow, id_self):
        heap = []
        for i in user_follow:
            post = self.user_list[i][0]
            for time, id in post:
                heapq.heappush(heap, (-time, id))

        for time, post_id in self.user_list[id_self][0]:
            heapq.heappush(heap, (-time, post_id))
        times = 10
        result = []
        while heap and times > 0:
            time, post_id = heapq.heappop(heap)
            result.append(post_id)
            times -= 1
        return result

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.user_list:
            self.user_list[followerId] = [[], []]
        if followeeId not in self.user_list:
            self.user_list[followeeId] = [[], []]
        if followerId != followeeId and followeeId not in self.user_list[followerId][1]:
            self.user_list[followerId][1].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.user_list and followeeId in self.user_list:
            follow_list = self.user_list[followerId][1]
            if followeeId in follow_list:
                self.user_list[followerId][1].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)