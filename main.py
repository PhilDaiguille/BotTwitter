import tweepy
import config
import time
client = tweepy.Client(bearer_token=config.BEAR_TOKEN)
client2 = tweepy.Client(consumer_key=config.API_KEY,
                        consumer_secret=config.API_SECRET,
                        access_token=config.ACCES_TOKEN,
                        access_token_secret=config.ACCES_TOKEN_SECRET)

#response2 = client2.create_tweet(text="Est ce que ce bot marche ou pas ? ")

#print(response2)

query = 'dessin'
response = client.search_recent_tweets(query=query,max_results=10, tweet_fields=['created_at', 'lang','text'], expansions=['author_id'])

api = tweepy.API(client)


users = {u['id']: u for u in response.includes['users']}



for tweet in response.data:
    if users[tweet.author_id]:

        user = users[tweet.author_id]
        print(user.username," |" ,tweet.lang, "| : " ,tweet.id , "- Commentaire : -", tweet.text)
        time.sleep(1)
        if(tweet.lang == "fr" or tweet.text == "premier dessin"):
            """
            Retweet = client2.retweet(tweet_id=tweet.id)
            print(Retweet)"""

            Like = client2.like(tweet_id=tweet.id)
            print(Like)


