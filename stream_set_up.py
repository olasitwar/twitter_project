from credentials import *
from twitter_project.scripts.TweetRead import *

if __name__ == '__main__':

    wordList = ['bullshit', 'fuck' 'hate']
    auth = OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    s = socket.socket()         # Create a socket object
    host = "127.0.0.1"     # Get local machine name
    port = 5555                 # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    print("Listening on port: %s" % str(port))

    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()        # Establish connection with client.

    print( "Received request from: " + str( addr ) )

    sendData(wordList, c , auth)

