import tweepy
import time

class FollowBot():
    
    def __init__(self, api):
        self.api = api

    def LimitHandled(self, cursor):
        i=0
        while True:
            try:
                yield next(cursor)

            except tweepy.RateLimitError:
                print('Sleeping, 15 Minutes remain.')
                time.sleep(5*60)
                print('Sleeping, 10 Minutes remain.')
                time.sleep(5*60)
                print('Sleeping, 5 Minutes remain.')
                time.sleep(4*60)
                print('Sleeping, 1 Minute remains.')
                time.sleep(60)


    def FollowID(self, ID, api):
        i=0


        for follower in FollowBot.LimitHandled(self, tweepy.Cursor(api.followers, ID).items()):
            try:
                follower.follow()
                i=i+1
                print(i + '. ' + follower.name)

            except tweepy.error.TweepError:
                pass





