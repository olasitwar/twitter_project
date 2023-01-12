from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_project.scripts.TweetTransform import *
import os
import pandas as pd

import socket
import json

class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads( data )
            tempArray = transform_json(msg)
            tweetsTable = pd.DataFrame([tempArray])

            tweetsTable.to_csv('/home/lkw/ASW/fetched_tweets.csv', mode='a',\
                               index=False, header = False)

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