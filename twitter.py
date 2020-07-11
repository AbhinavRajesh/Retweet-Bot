import tweepy
import time

consumer_key = "ENTER API KEY HERE"
consumer_secret = "ENTER API SECRET KEY HERE"
key = "ENTER ACCESS TOKEN HERE"
secret = "ENTER ACCESS SECRET TOKEN HERE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print("Retweet Bot Up and Running...")

search = "ENTER HASHTAG HERE"  # Retweets tweets with this tag
nor = 0

for tweet in tweepy.Cursor(api.search, search).items(500):
    try:
        tweet.favorite()
        print('Tweet Liked')
        tweet.retweet()
        print("Tweet Retweeted")
        nor += 1
        print("Number of Retweets: " + str(nor))
        time.sleep(7)  # Change the time of Retweet gap here in seconds
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
