""" 
Useful Resources:
http://docs.tweepy.org/en/v3.5.0/getting_started.html 
https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25
http://docs.tweepy.org/en/latest/

Creating The Twitter Sentiment Analysis Program in Python with Naive Bayes Classification
https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed

Tweepy, TextBlob and Sentiment Analysis — Python
https://medium.com/@r.ratan/tweepy-textblob-and-sentiment-analysis-python-47cc613a4e51
"""

import tweepy
import json
import pandas as pd

## Functions

def tweepyToDataframe ()

## Analysis

connections = json.load(open('C:/Users/amitt/OneDrive/Code/2020-07-29 Twitter API Keys/connection.json'))
api_key = connections['Twitter API']['API Key']
api_secret_key = connections['Twitter API']['API Secret Key']
bearer_token = connections['Twitter API']['Bearer Token']
access_token = connections['Twitter API']['Access Token']
access_token_secret = connections['Twitter API']['Access Token Secret']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# # Test that Twitter API connection is working
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (f"{tweet.user.name}: {tweet.text}")
# 
# public_tweets = pd.DataFrame(public_tweets)
    
tweets_fetched = api.search("game", count = 10)

for tweet in tweets_fetched:
    print (f"{tweet.user.name}: {tweet.text}")
    
cnn_breaking_news = api.user_timeline('cnnbrk')

json_data = [i._json for i in cnn_breaking_news]
df = pd.io.json.json_normalize(json_data)
