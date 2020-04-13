import praw
from dotenv import load_dotenv
import os
import random
from datetime import *

range_size = 1000000

date_start = date(2020, 4, 13)

load_dotenv()
reddit = praw.Reddit(client_id = os.getenv('PNB_CLIENT_ID'),
                     client_secret = os.getenv('PNB_CLIENT_SECRET'),
                     username = os.getenv('PNB_USERNAME'),
                     password = os.getenv('PNB_PASSWORD'),
                     user_agent = os.getenv('PNB_USER_AGENT'))

prime_number_daily = reddit.subreddit('primenumberdaily')

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def get_nth_prime(n):
    p = 2
    i = 1
    while i < n:
        p += 1
        if is_prime(p):
            i += 1
    return p

def main():
    submissions_exist = False
    for submission in prime_number_daily.new(limit=1):
        submissions_exist = True
        if(datetime.now().date() != datetime.fromtimestamp(submission.created_utc).date()):
            prime_number_daily.submit(str(get_nth_prime((datetime.now().date() - date_start).days + 1)), '')
    if not submissions_exist:
        prime_number_daily.submit('2', '')

if __name__ == '__main__':
    main()