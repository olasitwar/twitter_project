import pandas as pd
from IPython.display import display


if __name__ == '__main__':
    columnNames = ['created_at', 'id', 'text', \
       'user_id', 'user_screen_name', 'user_created_at', 'user_followers_count', \
       'user_friends_count', 'user_statuses_count', 'user_favourites_count', \
       'entities_user_mentions', 'entities_hashtags', 'timestamp']
    df = pd.read_csv(r"/home/lkw/ASW/fetched_tweets.csv", names=columnNames, header=None)
    display(df)