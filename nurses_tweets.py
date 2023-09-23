import tweepy
import twitter
import pandas as pd
import numpy as np
import csv
import time
from textblob import TextBlob
from datetime import datetime, timedelta, timezone
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Set up your Twitter API credentials
consumer_key = ' ' #'YOUR_CONSUMER_KEY'
consumer_secret = ' ' #'YOUR_CONSUMER_SECRET'
access_token = ' ' #'YOUR_ACCESS_TOKEN'
access_token_secret = ' ' #'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

startDate = datetime.strptime('2023-05-21 00:00:00+0000', '%Y-%m-%d %H:%M:%S%z')
#endDate = datetime.strptime('2023-05-10 00:00:00+0000', '%Y-%m-%d %H:%M:%S%z')

# Passing the parameters into the Cursor constructor method
public_tweets = tweepy.Cursor(api.search_tweets,
                              q= keywords,
                              count=100,
                              since_id=startDate,
                              lang=language,
                              tweet_mode="extended").items(limit)

# Defining Arrays to save results for each attribute seperatly
user_id_list = []
tweet_id_list = []
tweet_text_list = []
tweet_location_list = []
tweet_geo_list = []
tweet_place_list = []
user_screen_name_list = []
tweet_created_list = []
tweet_contributors_list = []
tweet_entities_list =[]
tweet_retweet_count_list = []
tweet_source_list = []
tweet_username_list = []
tweet_followers_count_list = []
friends_count_List = []
user_url_list = []
tweet_url_list = []
user_desc_list = []
favourites_count_list = []
favorite_count_list = []
listed_count_list = []
statuses_count_list = []
verified_list = []

# Iterating through the results to extract the results
for tweet in public_tweets:
    if tweet.created_at > startDate:
        user_id_list.append(tweet.user.id)
        tweet_id_list.append(tweet.id)
        tweet_text_list.append(tweet.full_text)
        tweet_location_list.append(tweet.user.location)
        tweet_geo_list.append(tweet.geo)
        tweet_place_list.append(tweet.place)
        user_screen_name_list.append(tweet.user.screen_name)
        user_url_list.append('https://twitter.com/' + str(tweet.user.id))
        tweet_url_list.append('https://twitter.com/i/web/status/' + str(tweet.id))
        user_desc_list.append(tweet.user.description)
        tweet_source_list.append(tweet.source)
        tweet_created_list.append(tweet.created_at)
        tweet_contributors_list.append(tweet.id_str)
        tweet_entities_list.append (tweet.entities)
        tweet_retweet_count_list.append(tweet.retweet_count)
        tweet_username_list.append(tweet.user.name)
        tweet_followers_count_list.append(tweet.user.followers_count)
        friends_count_List.append(tweet.user.friends_count)
        favourites_count_list.append(tweet.user.favourites_count)
        favorite_count_list.append(tweet.favorite_count)
        listed_count_list.append(tweet.user.listed_count)
        statuses_count_list.append(tweet.user.statuses_count)
        verified_list.append(tweet.user.verified)
        #time.sleep(0.5)
    
# Creating a Pandas dataframe to organize the data into a table
df = pd.DataFrame({'user_id': user_id_list,
                   'tweet_id': tweet_id_list,
                   'tweet_text': tweet_text_list,
                   'tweet_location': tweet_location_list,
                   'tweet_geo':tweet_geo_list,
                   'tweet_place': tweet_place_list,
                   'user_screen': user_screen_name_list,
                   'user_url' : user_url_list,
                   'tweet_url' : tweet_url_list,
                   'user_desc': user_desc_list,
                   'tweet_source': tweet_source_list,
                   'tweet_created': tweet_created_list,
                   'tweet_contributors': tweet_contributors_list,
                   'tweet_entities': tweet_entities_list,
                   'tweet_retweet_count': tweet_retweet_count_list,
                   'tweet_username': tweet_username_list,
                   'tweet_followers_count': tweet_followers_count_list,
                   'friends_count': friends_count_List,
                   'favourites_count': favourites_count_list,
                   'favorite_count': favorite_count_list,
                   'listed_count': listed_count_list,
                   'statuses_count': statuses_count_list,
                   'verified': verified_list})

consumed_time = time.time() - start_time

df.to_csv('file_name.csv')

