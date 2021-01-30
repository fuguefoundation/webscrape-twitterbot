import tweepy
from time import sleep
from credentials import *
from tweet_data_example import *

# Twitter auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet():
    for i in range(len(tweet_data)):
        try:
            # Create variables from the list file to formulate the tweet
            _id = tweet_data[i]['id']
            _title = tweet_data[i]['title']
            _desc = tweet_data[i]['desc']
            _url = tweet_data[i]['image']

            # Determine how long the description can be from the remaining characters
            _length = 270 - 23 - len(_title) - len(tweet_at) - len(tweet_hashtag)
            _shortDesc = _desc[:_length]

            # The aggregated tweet
            _tweet = str(i + 1) + '/ ' + _title + ': ' + _shortDesc + '| ' + _url + ' ' + tweet_at + ' ' + tweet_hashtag

            print(_tweet)

            # Send the tweet, uncomment when ready
            #api.update_status(_tweet)
        
        except tweepy.TweepError as e:
            print(e.reason)
        
        # Wait one day to run loop again (86400 seconds)
        sleep(5)

tweet()