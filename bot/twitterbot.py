import tweepy
from time import sleep
from credentials import *
from tweet_data import *

# Twitter auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet():
    for i in range(55):
        try:
            # Create variables from the list file to formulate the tweet
            _id = tweet_list[i]['id']
            _title = tweet_list[i]['title']
            _desc = tweet_list[i]['desc']
            _url = tweet_url + _id

            # Determine how long the description can be from the remaining characters
            _length = 267 - 23 - len(_title) - len(tweet_at) - len(tweet_hashtag)
            _shortDesc = _desc[:_length]

            # The aggregated tweet
            _tweet = str(i + 1) + '/ ' + _title + ' | ' + _shortDesc + '... ' + _url + ' ' + tweet_at + ' ' + tweet_hashtag

            print(_tweet)

            # Send the tweet
            api.update_status(_tweet)
        
        except tweepy.TweepError as e:
            print(e.reason)
        
        # Wait one day to run loop again (86400 seconds)
        sleep(86400)

tweet()