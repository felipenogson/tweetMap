import os
import json
import tweepy
import redis
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from dotenv import load_dotenv
from flask import Flask, render_template
from threading import Thread
from shapely.geometry import mapping, shape
from flask_socketio import SocketIO
from flask_socketio import emit, send

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# Init redis
r = redis.Redis()

# Twitter Auth
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Server Config
app = Flask(__name__)
socketio = SocketIO(app)


def get_centroid(polygon):
    """
    params polygon: GeoJson polygon
    return: GoeJson Point
    """
    polygon = shape(polygon)
    point = polygon.centroid
    return mapping(point)

def parser(tweet):
    """
    params tweet: dict
    return: GeoJson dict
    """
    geoJson = {
        "type": "Feature",
        "properties": {
            "text": tweet['text'],
            "created_at": tweet['created_at'].split('+')[0],
            "user": "@" + tweet['user']['screen_name'],
            "url" : "https://twitter.com/"+ tweet['user']['screen_name'] + "/status/" + tweet['id_str']
        },
        "geometry": get_centroid(tweet['place']['bounding_box']) 
        }
    return geoJson


class MyListener(StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        try:
            if 'place' in data and data['place']:  # Only tweets with location info
                feature = parser(data)
                r.lpush('tweetList', json.dumps(feature))
                r.ltrim('tweetList',0,29)
                socketio.emit('addMarker', feature, json=True)  # Send the tweet to all connected clients
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

def start_filter(tags):
    twitter_stream = Stream(auth, MyListener())  # Create object for Twitter Streaming API
    twitter_stream.filter(track=tags) # Start getting all the tweets with the given tags

@socketio.on('my event')
def primer_encuentro(msg):
    print('recived msg:', msg) 
    tweets = r.lrange('tweetList', 0, -1)
    tweets = [json.loads(x) for x in tweets]
    emit('tweets', tweets, json=True)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    tags = ["#coronavirus"]
    # Create and start thread for get the tweets
    Thread(target=start_filter, args=(tags,)).start()
    # Start the server
    socketio.run(app, debug=True, host='0.0.0.0')
