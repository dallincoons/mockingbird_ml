import pandas as pd
from tweets import Tweets

def main():
    # csv = pd.read_csv('bernie_tweets.csv')
    # csv.replace(r'"', '', inplace=True, regex=True)
    # print(csv)
    tweets = Tweets(pd.read_csv('bernie_tweets2.csv', sep='^')).clean()

    tweets.to_csv('cleaned_bernie_tweets.csv', index=False)

def remove_retweets(tweets):
    return tweets[~tweets.text.str.startswith("RT")]

if __name__ == '__main__':
    main()
