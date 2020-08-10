
cnn_breaking_news = api.user_timeline('cnnbrk')

cnn_breaking_news_df = tweepyToDataframe(cnn_breaking_news)

# Test that Twitter API connection is working
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (f"{tweet.user.name}: {tweet.text}")

public_tweets = pd.DataFrame(public_tweets)


# Searching data
tweets_fetched = api.search("game", count = 10)

for tweet in tweets_fetched:
    print (f"{tweet.user.name}: {tweet.text}")

