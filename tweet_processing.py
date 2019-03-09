import pandas as pd
from tweets import Tweets

def main():
    tweets = Tweets(pd.read_csv('trumptweets.csv')).clean()

    tweets.to_csv('cleaned_tweets.csv', index=False)

def remove_retweets(tweets):
    return tweets[~tweets.text.str.startswith("RT")]

if __name__ == '__main__':
    main()
