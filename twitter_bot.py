import tweepy
import time


class TweetBot:
    def __init__(self):
        # Authentication and API object creation
        self.auth = tweepy.OAuthHandler("G7i43jjsz5kqzmB35je8h3ldh", "Tmy01NijyMZY3F4M7AlnawkPvNaTtFJH0pIVr580TUZMa5qa4j")
        self.auth.set_access_token("1286172822738317312-R1QbHISTkszt182jEblvRiXVmkncLg", "rYN9xAucOCqvYeKlsBhph7hCr0RFfLpSEJrwJrhhtdNGh")
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        # Wait between each request of favourites(in seconds)
        self.wait_between_requests = 2 
    def __str__(self):
        me = self.api.me()
        return "This is a twitter bot of @" + me.screen_name


    # Function for liking tweets, takes a list of users and optional parameter tweet_count for number of tweets to like(default 10 tweets will be liked)
    def like_user_tweets(self, userList, tweet_count = 10):
        for user_id in userList:
            for tweet in tweepy.Cursor(self.api.user_timeline, id=user_id).items(tweet_count):
                time.sleep(self.wait_between_requests)
                try:
                    tweet.favorite()
                    print("Tweet Liked: {}".format(tweet.text))
                except tweepy.TweepError as e:
                    print("Error: {} Tweet: {}".format(e.reason, tweet.text))


    # Function for retweeting, takes a list of users and optional parameter tweet_count for number of tweets to retweet(default 10 tweets will be retweeted)
    def retweet_user_tweets(self, userList, tweetCount = 10):
        for user_id in userList:
            for tweet in tweepy.Cursor(self.api.user_timeline, id=user_id).items(tweetCount):
                time.sleep(self.wait_between_requests)
                try:
                    tweet.retweet()
                    print("Tweet Retweeted: {}".format(tweet.text))
                except tweepy.TweepError as e:
                    print("Error: {} Tweet: {}".format(e.reason, tweet.text))
    

    # Function for liking tweets of hashtags, takes a list of hashtags and optional parameter tweet_count for number of tweets to like(default 10 tweets will be liked)
    def like_hashtag_tweets(self, hashtagList, tweetCount = 10):
        for hashtag in hashtagList:
            for tweet in tweepy.Cursor(self.api.search, q=hashtag).items(tweetCount):
                time.sleep(self.wait_between_requests)
                try:
                    tweet.favorite()
                    print('Tweet Liked with {} : {}'.format(hashtag, tweet.text))
                except tweepy.TweepError as e:
                    print("Error: {} Tweet: {}".format(e.reason, tweet.text))


    # Function for unliking all the tweets liked by the bot account
    def unlike_all_tweets(self):
        for tweet in self.api.favorites():
            time.sleep(self.wait_between_requests)
            try:
                self.api.destroy_favorite(tweet.id)
                print("Unliked: {}".format(tweet.text))
            except tweepy.TweepError as e:
                print("Error: {} Tweet: {}".format(e.reason, tweet.text))

bot = TweetBot()
print(bot)
hashtags = ["#python", "#bot", "#dog"]
accounts = ["buyucoin", "iamsrk", "narendramodi"]
bot.like_user_tweets(accounts, 2) # Recent two tweets of all acounts will be liked
bot.like_hashtag_tweets(hashtags, 2) # Recent two tweets of the hashtag will be liked

# Uncomment to unlike all tweets
# bot.unlike_all_tweets()


