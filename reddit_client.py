# coding: utf-8
from dotenv import load_dotenv
import json
import redis
import praw
import os

r = redis.Redis()

load_dotenv()
client = os.getenv('CLIENT_ID')
secret = os.getenv('SECRET')
agent = os.getenv('AGENT')

reddit_client = praw.Reddit(client_id=client, client_secret=secret, user_agent=agent)
reddit_client.read_only


def download_articles():
    for submission in reddit_client.subreddit('coronavirus').hot(limit=20):
        if submission.stickied == True:
            continue
        article = {"title":submission.title, "thumbnail": submission.thumbnail, "url":submission.url}
        r.sadd('articles', json.dumps(article))

def get_random_article():
    return r.srandmember('articles').decode()


    
    
