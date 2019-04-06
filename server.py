from flask import Flask, jsonify, request
from flask import url_for, redirect
app = Flask(__name__)
from TweetGenerator import TweetGenerator
from TrumpTweets import TrumpTweets
from BernieTweets import BernieTweets
from MonsterTweets import MonsterTweets

@app.route("/")
def home():
    return url_for('static', filename='home.html')

@app.route("/get-tweet")
def tweet():

    index = int(request.args.get('index'))
    author = request.args.get('author')

    if author == 'trump':
        tweets = TrumpTweets()
    elif author == 'bernie':
        tweets = BernieTweets()
    else:
        tweets = MonsterTweets()

    info = {
        "tweet" : tweets.new(index),
        "index" : tweets.new_index(index),
        "total_tweets" : tweets.total_tweets()
    }
    return jsonify(info)
