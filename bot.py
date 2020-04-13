import praw
from dotenv import load_dotenv
import os

load_dotenv()
reddit = praw.Reddit(client_id = os.getenv('PNB_CLIENT_ID'),
                     client_secret = os.getenv('PNB_CLIENT_SECRET'),
                     username = os.getenv('PNB_USERNAME'),
                     password = os.getenv('PNB_PASSWORD'),
                     user_agent = os.getenv('PNB_USER_AGENT'))

prime_number_daily = reddit.subreddit('primenumberdaily')