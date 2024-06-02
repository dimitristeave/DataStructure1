# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
from collections import defaultdict


class Twitter:
    # Initialize your data structure here
    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []

    # Compose a new tweet
    def postTweet(self, userId: int, tweetId: int):
        self.tweets.append((userId, tweetId))

    # Retrieve the 10 most recent tweet ids as mentioned in question
    def getNewsFeed(self, userId: int):
        res = []
        i = len(self.tweets) - 1
        while i >= 0 and len(res) < 10:
            if self.tweets[i][0] in self.users[userId] or self.tweets[i][0] == userId:
                res.append(self.tweets[i][1])
            i -= 1
        return res

    # Follower follows a followee. If the operation is invalid, it should be a no-op.
    def follow(self, followerId: int, followeeId: int):
        self.users[followerId].add(followeeId)

    # Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    def unfollow(self, followerId: int, followeeId: int):
        if followeeId in self.users[followerId]: self.users[followerId].remove(followeeId)


# {
# Driver Code Starts.
if __name__ == '__main__':
    obj = Twitter()
    totalQueries = int(input())
    for _ in range(totalQueries):
        query = list(map(int, input().split()))
        if (query[0] == 1):
            userId, tweetId = query[1], query[2]
            obj.postTweet(userId, tweetId)
        elif (query[0] == 2):
            userId = query[1]
            vec = obj.getNewsFeed(userId)
            for val in vec:
                print(val, end=' ')
            print()
        elif (query[0] == 3):
            follower, followee = query[1], query[2]
            obj.follow(follower, followee)
        else:
            follower, followee = query[1], query[2]
            obj.unfollow(follower, followee)
# } Driver Code Ends