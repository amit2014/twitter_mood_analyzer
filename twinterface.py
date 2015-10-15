import tweepy

# consumer keys and access tokens, used for OAuth
consumer_key = 'ArJTlGOeA7rnIHyiPZkHmMhIJ'
consumer_secret = 'zr7Ldopc0QdwxvsMwBcFFYk3LsWUPeuKEkfo6wj9848W4x7eq0'
access_token = '1550061679-WpJunbZbtwCGXL84wQbyzmOuSre1tNh7iloJyQV'
access_token_secret = 'PusPCv8NgalPKSagKNMioU8xpP77TrhSXS9wKH0A5K8bE'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of actual interface, using authentication
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
