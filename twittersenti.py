"""
Created on Wed Apr 17 13:53:12 2018

@author: sushilkulkarni (with references from Siraj Raval's repo)
"""


import tweepy
from textblob import TextBlob



# Step 1 - Authenticate
consumer_key= 'WWW'
consumer_secret= 'XXX'

access_token='YYY'
access_token_secret='ZZZ'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
client = tweepy.API(auth)

# Step 2 search for 'bitcoin'


tweets=client.search('bitcoin') 
#timeline = client.home_timeline()



# Step 3 perform sentiment analysis on results using 'textblob' 
for item in tweets:
    text = "%s says '%s'" % (item.user.screen_name, item.text)
    #print(text)
    analysis = TextBlob(item.text)
    print(item.user.screen_name, analysis.sentiment)
    print("")

# Step 4 Clean up
del tweets
del client
del auth