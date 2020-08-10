""" 
Useful Resources:
http://docs.tweepy.org/en/v3.5.0/getting_started.html 
https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25
http://docs.tweepy.org/en/latest/

Creating The Twitter Sentiment Analysis Program in Python with Naive Bayes Classification
https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed

Tweepy, TextBlob and Sentiment Analysis — Python
https://medium.com/@r.ratan/tweepy-textblob-and-sentiment-analysis-python-47cc613a4e51

TextBlob: Simplified Text Processing
https://textblob.readthedocs.io/en/dev/
https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/analyze-tweet-sentiment-in-python/
"""

import tweepy
import json
import pandas as pd

## Functions

def tweepyToDataframe (api_data):
    json_data = [i._json for i in api_data]
    df = pd.io.json.json_normalize(json_data)
    return df

def remove_url(txt): # From: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/analyze-tweet-sentiment-in-python/
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

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
    

