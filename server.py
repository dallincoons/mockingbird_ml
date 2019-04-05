from flask import Flask, jsonify, request
from flask import url_for, redirect
app = Flask(__name__)
from TweetGenerator import TweetGenerator

@app.route("/")
def home():
    return url_for('static', filename='home.html')

@app.route("/get-tweet")
def tweet():

    index = int(request.args.get('index'))

    info = {
        "tweet" : TweetGenerator.new(index),
        "index" : TweetGenerator.new_index(index),
        "total_tweets" : TweetGenerator.total_tweets()
    }
    return jsonify(info)
