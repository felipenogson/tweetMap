# coding: utf-8
import praw
load_dotenv()
import os
client = os.getenv('CLIENT_ID')
secret = os.getenv('SECRET')
agent = os.getenv('AGENT')
reddit_client = praw.Reddit(client_id=client, client_secret=secret, user_agent=agent)
reddit_client.read_only
