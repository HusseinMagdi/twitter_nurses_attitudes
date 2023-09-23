import pandas as pd
import numpy as np
import csv
import time
from textblob import TextBlob
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

# Improt data set from csv
df = pd.read_csv('file_name.csv')

# TextBlob Sentiment Analysis
text = df['tweet_text']

# Calculate time consumed 
start_time = time.time()

# Set a function for TextBlob sentiment analysis
def polarity(review):
    return TextBlob(review).sentiment.polarity

def subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

df['polarity'] = df['tweet_text'].apply(polarity)
df['subjectivity'] = df['tweet_text'].apply(subjectivity)

consumed_time = time.time() - start_time

# Vader Sentiment Analysis
text = df['tweet_text']

# Calculate time consumed 
start_time = time.time()

vader_sentiment = SentimentIntensityAnalyzer()

# Set a function for TextBlob sentiment analysis
def sentiment(text):
    df = vader_sentiment.polarity_scores(text)
    return df


df['sentiment'] = df['tweet_text'].apply(sentiment)

# Split sentiment column into two columns in Pandas
df[['sentiment', 'vader']] = df['sentiment'].apply(lambda x: pd.Series(str(x).split("'compound': ")))
df['vader'] = df['vader'].str.replace(r'}','') # remove } from the end of the vader column
df['vader'] = pd.to_numeric(df['vader']) # convery the vader column to numeric

consumed_time = time.time() - start_time

# Save data frame to CSV file
df.to_csv('file_name_sentiment.csv')
