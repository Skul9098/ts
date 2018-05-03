#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:53:12 2018

@author: sushilkulkarni (with references from Siraj Raval's repo)
"""

import time as tm
import tweepy
import csv
from textblob import TextBlob




# Step 1 - Authenticate
consumer_key= '0gn9sOLUJTZ44u2l38H6m11zs'
consumer_secret= 'XI9OVNvVHa9trAtL7Kekg4f323caQ73EJycbHPgcbKadtffSbg'

access_token='182727277-VFj81m5iH7OLWMY4CpjPVO0npKBx8DxkhXZPXFKc'
access_token_secret='RnBuWLCVVZeV8R5S4EAaTEZJHO8SZW9sZJRqatotyUlcT'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
client = tweepy.API(auth)

influencer=['@pmarca',	'@aantonop','@brian_armstrong',	'@gendal','@VitalikButerin','@niccary','@cdixon','@TimDraper','@NicTrades','@FEhrsam','@BitMEXdotcom','@bhorowitz','@SatoshiLite','@officialmfee',	'@PipCzar','@Catheryne_N','@barrysilbert','@jimmysong','@balajis','@ToneVays','@rogerkver',	'@ErikVoorhees']
#tweets=""
    
for x in influencer: 
    user = client.get_user(x)    
    print(user)
    print(x)
    tweets += client.user_timeline(screen_name=x,count=100)
    tm.sleep(3)

    
	

# Step 2 search for 'bitcoin'
    
tweets1=client.search('bitcoin')
   
#tweets=tweets+str(client.search('bitcoin'))
#timeline = client.home_timeline()



# Step 3 perform sentiment analysis on results using 'textblob' 

senti_arr=[]
temp=["date","polarity","subjectivity"]
senti_arr.append(temp)


for item in tweets:
    #text = "'%s'  createdate '%s' says '%s'" % (item.user.screen_name, item.created_at, item.text)
    text = item.user.screen_name, item.created_at, item.text
    print(text)
    analysis = TextBlob(item.text)
    temp=[str(item.created_at), str(analysis.sentiment[0]), str(analysis.sentiment[1])]
    senti_arr.append(temp)
    
    
    #print(item.user.screen_name, analysis.sentiment)
    print("")
   
    
for item in tweets1:
    #text = "'%s'  createdate '%s' says '%s'" % (item.user.screen_name, item.created_at, item.text)
    text = item.user.screen_name, item.created_at, item.text
    print(text)
    analysis = TextBlob(item.text)
    temp=[str(item.created_at), str(analysis.sentiment[0]), str(analysis.sentiment[1])]
    senti_arr.append(temp)
   
    from datetime import datetime
    df = pd.DataFrame(senti_arr, columns=temp)
    df=df.iloc[1:]
    df.dtypes
    df['subjectivity'] = pd.to_numeric(df['subjectivity'], errors='coerce')
    df['polarity'] = pd.to_numeric(df['polarity'], errors='coerce')
    
    then = datetime.strptime(str(df['date']), '%Y-%m-%d').date()
    df['date'] = [str(df['date']), 0]

    df['date']
    df.groupby(["date"]).mean()
# save sentiment to file 
with open('/Users/sushilkulkarni/Data Science/5703/senti_txt.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(senti_arr)


# Step 4 Clean up
del tweets
del client
del auth

 
