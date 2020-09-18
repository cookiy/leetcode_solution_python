"""
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:

Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-twitter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""



class Twitter:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = dict()  # key:value分别对应用户 userId(int) 和 其关注者(list)
        self.posts = []  # 发布的帖子，每个元素格式为 [userId, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts.append([userId, tweetId])  # 将帖子加入 posts 列表
        if not self.users.get(userId):  # 同步更新用户列表，如果 userId 在字典中的值不存在，则设为初始值 [],否则不操作
            self.users[userId] = []

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users.keys():  # 检查 userId 的合法性,如果该用户不存在，直接返回
            return
        else:  # 用户存在
            ids = [userId] + self.users.get(userId)  # 计算待排查id，包括用户自身 id 还有他 follow 的人的 id
            tmp = []  # 待返回的结果集
            count = 10  # 计数器：排查最新的10条
            for post in self.posts[-1:-(len(self.posts) + 1):-1]:  # 开始排查，并将 tweetId 加入结果集
                if count > 0:
                    if post[0] in ids:
                        tmp.append(post[1])
                        count -= 1
            return tmp

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # 检查 followerId 用户的 id 合法性，如果没在 self.users 中出现过，则设为初始值
        if followerId not in self.users.keys():
            self.users[followerId] = []
            self.users[followerId].append(followeeId)
        # followerId 如果在 self.users 中出现过，则直接将 followeeId 直接加入
        else:  
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # 检查合法性，如果 followerId 未曾出现，则直接返回
        if followerId not in self.users.keys():
            return 
        else:
            # 检查被移除的 id 的合法性，如果存在直接删除
            if followeeId in self.users[followerId]:
                self.users[followerId].remove(followeeId)
            else:
            # 被移除的 id 不存在，返回
                 return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)