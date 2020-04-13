import praw
from dotenv import load_dotenv
import os
import random

range_size = 1000000

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

def main():
    primes = [i for i in range(2,range_size) if is_prime(i)]
    prime_number_daily.submit(str(random.choice(primes)), '')

if __name__ == '__main__':
    main()