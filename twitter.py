""" Retweet Bot """
import tweepy
import time
import random

consumer_key = "ENTER API KEY HERE"
consumer_secret = "ENTER API SECRET KEY HERE"
key = "ENTER ACCESS TOKEN HERE"
secret = "ENTER ACCESS SECRET TOKEN HERE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print("Retweet Bot Up and Running...")

search = "ENTER HASHTAG HERE"  # Retweets tweets with this tag

status = [
    "ENTER_THE_COMMENTS_1",
    "ENTER_THE_COMMENTS_2",
]  # Enter the comments which would be retweeted

for tweet in tweepy.Cursor(api.search, search).items(1000):
    try:
        tweet.favorite()
        print('Tweet Liked')
        username = tweet._json['entities']['user_mentions'][0]['screen_name']
        tweet_id = tweet.id_str
        tweet_link = "https://twitter.com/" + username + "/status/" + tweet_id
        i = random.randint(0, len(status))
        api.update_status(status[i-1] + "\n" + tweet_link)
        print("Tweet Retweeted")
        time.sleep(7)  # Change the time of Retweet gap here in seconds
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
