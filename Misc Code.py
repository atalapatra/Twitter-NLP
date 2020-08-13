## API Rate Limit Status

data = api.rate_limit_status()

data['resources']['statuses']['/statuses/home_timeline']
data['resources']['users']['/users/lookup']


## Sentiment Analysis using TextBlob

# Create a custom search term and define the number of tweets
search_term = "#cyberpunk 2077 -filter:retweets"

tweets = tweepy.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   since='2020-01-01').items(10)

# Remove URLs
tweets_no_urls = [Module.remove_url(tweet.text) for tweet in tweets]
    
# Create textblob objects of the tweets
sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]

sentiment_objects[0].polarity, sentiment_objects[0]

sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]

# Create dataframe containing the polarity value and tweet text
sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])

# Plot histogram
fig, ax = plt.subplots(figsize=(8, 6))

# Plot histogram of the polarity values
sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="purple")

plt.show()



cnn_breaking_news = api.user_timeline('cnnbrk')

cnn_breaking_news_df = Module.tweepyToDataframe(cnn_breaking_news)

# Test that Twitter API connection is working
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (f"{tweet.user.name}: {tweet.text}")

public_tweets = pd.DataFrame(public_tweets)


# Searching data
tweets_fetched = api.search("game", count = 10)

for tweet in tweets_fetched:
    print (f"{tweet.user.name}: {tweet.text}")

