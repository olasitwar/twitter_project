import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import os

import socket
import json

# def get_steamed_data(consumer_key, consumer_secret, access_token, access_secret):

def sendData(wordList, c_socket, auth):
  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=wordList)

class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True


