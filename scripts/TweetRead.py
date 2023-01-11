import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_project.scripts.TweetTransform import *
import os

import socket
import json

# def get_steamed_data(consumer_key, consumer_secret, access_token, access_secret):



class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads( data )
            tempArray = transform_json(msg)
            tweets = pd.DataFrame(tempArray, columns=['created_at', 'id', 'text',\
                'user_id', 'user_screen_name', 'user_created_at', 'user_followers_count',\
                'user_friends_count', 'user_statuses_count', 'user_favourites_count',\
                'entities_user_mentions', 'entities_hashtags' 'timestamp'])
            tweets.to_csv('/home/lkw/ASW/fetched_tweets.csv', mode='a', index=False)

            self.client_socket.send( msg['text'].encode('utf-8') )
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def sendData(wordList, c_socket, auth):
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=wordList)