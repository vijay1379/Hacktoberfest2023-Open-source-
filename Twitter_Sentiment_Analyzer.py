import tweepy
from textblob import TextBlob

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_key_secret = 'YOUR_CONSUMER_KEY_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search_tweets(q='AVENGERS')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment.polarity > 0:
        print("Positive")
    elif analysis.sentiment.polarity < 0:
        print("Negative")
    else:
        print("Neutral")
