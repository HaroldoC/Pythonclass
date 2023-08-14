import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler(
    "95GhnVKN8fi1RuClYjV6Jmrzz", "qnFpNsEUuod2zgeQQd8mZ1u7r5ZBJxEQMj9ng61s3e4adEoJoe"
)
auth.set_access_token(
    "1660772749432725504-kOJr4SjCGnvODDWI2Wphd2LDwoTFgP",
    "AwIDJjsuZlWVLgSA59k7y9EpMFAR3kPSyKQigDzrW6RNj",
)

# Create API object
api = tweepy.API(auth)
user = api.me()
print(user.followers_count)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search = "python"
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# generous bot
# for follower in tweepy.Cursor(api.followers).items():
#     if follower.name == "TinTin":
#         follower.follow()
#         break

# api.update_profile(description="I like python")


# Create a tweet
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# api.update_status("Hello Tweepy")
