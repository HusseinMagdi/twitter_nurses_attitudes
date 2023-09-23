import twitter
import pandas as pd
import numpy as np
import csv

# Import data file into data frame
df = pd.read_csv('file_name_sentiment.csv')

# Loop through each tweet and extract relevant information
tweet_text = df['tweet_text']

# Create a function to remove extra characters in tweet like URLs, mentions, and hashtags
def get_counts(tweet):
    for tweet in tweets:
        # Clean the tweet text by removing URLs, mentions, and hashtags
        tweet_text = tweet_text
        tweet_text = re.sub(r'http\S+', '', tweet_text)  # Remove URLs
        tweet_text = re.sub(r'@\S+', '', tweet_text)     # Remove mentions
        tweet_text = re.sub(r'#\S+', '', tweet_text)    # Remove hashtags
        tweet_text = tweet_text.strip()
        return new_tweet,
        except:
            print("Error retrieving data for")
            return None, None  

# Apply the function to the TwitterUsername column and create new columns for follower and friend counts
df[['new_tweet]] = df['User'].apply(lambda x: pd.Series(get_counts(x)))

# Save data frane to CSV file
df.to_csv('file_name_cleaned.csv')
