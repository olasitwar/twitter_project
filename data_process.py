import pandas as pd
from twitter_project.credentials import *
from IPython.display import display
from twitter_project.scripts.TweetStaticDownload import get_static_tweets
from twitter_project.scripts.TweetCompare import static_stream_comparison


if __name__ == '__main__':
    columnNames = ['created_at', 'id', 'text', \
       'user_id', 'user_screen_name', 'user_created_at', 'user_followers_count', \
       'user_friends_count', 'user_statuses_count', 'user_favourites_count', \
       'entities_user_mentions', 'entities_hashtags', 'timestamp']
    df_stream = pd.read_csv(r"/home/lkw/ASW/fetched_tweets.csv", names=columnNames, header=None)

    df_users = df_stream[['user_id', 'user_screen_name']]\
        .drop_duplicates(subset=['user_id'], keep='first')\
        .copy()
    # df_users.to_csv(EXPORT_FOLDER + "users.csv", index=False)
    # get_static_tweets(df_users)

    # load data
    columnNamesStatic = ['id', 'created_at', 'source', 'text', 'is_quote_status',\
       'retweet_count', 'favorite_count', 'in_reply_to_status_id',\
       'in_reply_to_user_id', 'in_reply_to_screen_name', 'quoted_status_id',\
       'quoted_status_created_at', 'quoted_status_text',\
       'quoted_status_user_id', 'quoted_status_user_screen_name',\
       'quoted_status_user_created_at', 'retweeted_status_id',\
       'retweeted_status_created_at', 'retweeted_status_text',\
       'retweeted_status_user_id', 'retweeted_status_user_screen_name',\
       'retweeted_status_user_created_at', 'user_screen_name',\
       'entities_screen_name_list', 'entities_user_id_list',\
       'entities_hashtags_list', 'trackDate']

    df_static = pd.read_csv(EXPORT_FOLDER + 'static_tweets.csv', header=None, names=columnNamesStatic)
    static_stream_comparison(df_stream, df_static)





