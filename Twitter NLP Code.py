import Module
import tweepy
import json
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

## Connecting to Twitter API

connections = json.load(open('C:/Users/amitt/OneDrive/Code/2020-07-29 Twitter API Keys/connection.json'))
api_key = connections['Twitter API']['API Key']
api_secret_key = connections['Twitter API']['API Secret Key']
bearer_token = connections['Twitter API']['Bearer Token']
access_token = connections['Twitter API']['Access Token']
access_token_secret = connections['Twitter API']['Access Token Secret']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth #,
                 # wait_on_rate_limit=True, 
                 # wait_on_rate_limit_notify=True
                 )


## Create list of search terms and combine into dataframe

search_criteria = ['cyberpunk 2077',
                   'watch dogs legion',
                   'hitman 3',
                   'crusader kings 3',
                   'star wars squadrons'
                   ]

sentiment_df_list = []

for search in search_criteria:
    tweets = tweepy.Cursor(api.search,
                       q=search,
                       lang="en",
                       since='2020-01-01').items(200)
    tweets_no_urls = [Module.remove_url(tweet.text) for tweet in tweets]
    sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]
    sentiment_values = [[str(search), tweet.sentiment.polarity, tweet.sentiment.subjectivity, str(tweet) ] for tweet in sentiment_objects]
    sentiment_values_df = pd.DataFrame(sentiment_values, columns=["search terms", "polarity", "subjectivity", "tweet"])
    sentiment_df_list.append(sentiment_values_df)

sentiment_df = pd.concat(sentiment_df_list)

sentiment_df.hist(column='polarity', by='search terms', figsize = (10,12), range=[-1, 1])

plt.show()
