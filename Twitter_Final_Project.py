"""
This is a sample project to use Twitter Streaming API to get the top 5/10 tweets on your homepage along
with what your last 5 tweets and top 5 trending topics and their tweet volume. 
"""

#you have to install Tweepy module to use Twitter API - "pip install tweepy"

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pathlib
import sys
from collections import OrderedDict
from operator import itemgetter

#create your own app (https://apps.twitter.com) to interact with Twitter and generate the access token for authorization purpose.


access_token = "797190096948776960-A0C94ne8o4juZTB89ijzmZ9Rw6QNhQR"
access_token_secret="g3vaq5dYX7PUoBDs8EFMAqkoYynjWrZTsrVK0aXRziqqz"
consumer_key = "pRypIKSUGPrCGLpFIui29m7Iu"
consumer_secret = "sIDH0ZR2cdJH0nuHwV8vNVshZhNLhzmzLVswHiF1VzBoFHTTra"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)

class Twitter():

     #To Read Our Twitter Homepage - n records only on your homepage
     def HomepageTweets(self, n):
          for status in tweepy.Cursor(api.home_timeline).items(n):
               print(status.text)
               print ("\n")

               # here we are trying to write the content to file in your local (give your own path)
               try:
                   with open("C:/Users/Yatish/Documents/Yatish/Ana-Data/Python Scripts/Twitter Project/twitter.txt", "a") as f:
                       f.write(status.text)
                       f.write("\n")
                       f.close()
               except BaseException as e:
                       e = sys.exc_info()[0]  #fetching exception
                       print ('ERROR:',e)  #Printing exception
                       continue

     # To get the top nn tweets we have made on our profile
     def OwnTweets(self, n):
          for tweet in tweepy.Cursor(api.user_timeline).items(n):
              print (tweet.text)

     # To get the list of top 5 trendings topics and their tweet volume only
     def TopTrends(self, n):
          for tweet in tweepy.Cursor(api.user_timeline).items():
              trends1 = api.trends_place(1)

              data = trends1[0]['trends']

              names = set([trend['name'] for trend in data])
              volume = set([trend['tweet_volume'] for trend in data])

              result = dict(zip(names, volume)) # to take corressponding name with their tweet volume.

              result = {key: value for key, value in result.items() if value != None} # there could be few values whose tweets volume is None, we have to avoid those.

              top_trends = OrderedDict(sorted(result.items(), key=itemgetter(1), reverse=True)[:n]) # sorting the dictionary on values in decreasing order and taking top 5.

          print (top_trends)


object1 = Twitter()
object1.HomepageTweets(5)
object1.OwnTweets(5)
object1.TopTrends(5)


