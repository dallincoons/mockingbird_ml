from abc import ABC, abstractmethod

class TweetGenerator(ABC):
    @abstractmethod
    def getTweet(self, index):
        pass

    def new(self, index):
        if index >= self.total_tweets():
            index = 0
        tweet = self.getTweet(index)

        return tweet

    def new_index(self,index):
        if (index >= self.total_tweets() - 1):
            return 0
        else:
            return index + 1

    def total_tweets(self):
        return len(self.tweets)
