class Tweets:
    def __init__(self, tweets):
        self.tweets = tweets

    def clean(self):
        self.remove_urls()
        self.remove_empty_rows()
        # self.remove_retweets()
        return self.tweets

    def remove_retweets(self):
        self.tweets = self.tweets[~self.tweets.text.str.startswith("RT")]

    def remove_urls(self):
        self.tweets['text'].replace(r'(?:https?):\/\/?[\w/\-?=%.]+\.[\w/\-?=%.]+', '', inplace=True, regex=True)

    def remove_empty_rows(self):
        self.tweets = self.tweets[self.tweets['text'] != '']
