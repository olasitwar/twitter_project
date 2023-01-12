from twitter_project.credentials import *
from tweepy import API, Cursor, OAuthHandler, TweepError
import pandas as pd
import numpy as np
import time
from datetime import datetime


def get_static_tweets(df_users):
    auth = OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    accountsToRecheckDict = {}
    for tempuser in df_users['user_screen_name'].values:
        accountsToRecheckDict[tempuser] = 3200

    for i, (tempName, tempStatusNumber) in enumerate(accountsToRecheckDict.items()):
        try:
            source__user_screen_name = tempName
            ids = []

            for fid in Cursor(api.user_timeline, id=source__user_screen_name).items(3200):
                ids.append(fid)
            data = [x._json for x in ids]
            df = pd.DataFrame(data)

            if 'retweeted_status' not in df.columns:
                df['retweeted_status'] = np.nan

            if 'quoted_status' not in df.columns:
                df['quoted_status'] = np.nan

            if 'quoted_status_id' not in df.columns:
                df['quoted_status_id'] = np.nan

            df = df[['id', 'created_at', 'user', 'entities', 'source', 'text', 'is_quote_status', 'retweet_count',
                     'favorite_count', \
                     'in_reply_to_status_id', 'in_reply_to_user_id', 'in_reply_to_screen_name', 'quoted_status_id',
                     'quoted_status', 'retweeted_status', \
                     ]]

            df['quoted_status_id'] = df['quoted_status'].apply(
                lambda x: x.get("id", 'NaN') if (type(x) is dict) == True else x)
            df['quoted_status_created_at'] = df['quoted_status'].apply(
                lambda x: x.get("created_at", 'NaN') if (type(x) is dict) == True else x)
            df['quoted_status_text'] = df['quoted_status'].apply(
                lambda x: x.get("text", 'NaN') if (type(x) is dict) == True else x)
            df['quoted_status_user'] = df['quoted_status'].apply(
                lambda x: x.get("user", 'NaN') if (type(x) is dict) == True else x)
            df['quoted_status_user_id'] = df['quoted_status_user'].apply(
                lambda x: x.get("id", 'NaN') if (type(x) is dict) == True else x)
            df['quoted_status_user_screen_name'] = df['quoted_status_user'].apply(
                lambda x: x.get("screen_name", 'NaN') if (type(x) is dict) == True else x)
            df['quoted_status_user_created_at'] = df['quoted_status_user'].apply(
                lambda x: x.get("created_at", 'NaN') if (type(x) is dict) == True else x)

            df['retweeted_status_id'] = df['retweeted_status'].apply(
                lambda x: x.get("id", 'NaN') if (type(x) is dict) == True else x)
            df['retweeted_status_created_at'] = df['retweeted_status'].apply(
                lambda x: x.get("created_at", 'NaN') if (type(x) is dict) == True else x)
            df['retweeted_status_text'] = df['retweeted_status'].apply(
                lambda x: x.get("text", 'NaN') if (type(x) is dict) == True else x)
            df['retweeted_status_user'] = df['retweeted_status'].apply(
                lambda x: x.get("user", 'NaN') if (type(x) is dict) == True else x)
            df['retweeted_status_user_id'] = df['retweeted_status_user'].apply(
                lambda x: x.get("id", 'NaN') if (type(x) is dict) == True else x)
            df['retweeted_status_user_screen_name'] = df['retweeted_status_user'].apply(
                lambda x: x.get("screen_name", 'NaN') if (type(x) is dict) == True else x)
            df['retweeted_status_user_created_at'] = df['retweeted_status_user'].apply(
                lambda x: x.get("created_at", 'NaN') if (type(x) is dict) == True else x)

            del df['retweeted_status_user']
            del df['quoted_status']
            del df['retweeted_status']
            del df['quoted_status_user']

            df['user_screen_name'] = df['user'].apply(lambda x: x.get("screen_name", 'NaN'))
            df['entities_user_mentions'] = df['entities'].apply(lambda x: x.get("user_mentions", 'NaN'))
            df['entities_hashtags'] = df['entities'].apply(lambda x: x.get("hashtags", 'NaN'))
            df['entities_screen_name_list'] = df['entities_user_mentions'].apply(
                lambda z: [x.get("screen_name", 'NaN') for x in [singleJSON for singleJSON in z]])
            df['entities_user_id_list'] = df['entities_user_mentions'].apply(
                lambda z: [x.get("id", 'NaN') for x in [singleJSON for singleJSON in z]])
            df['entities_hashtags_list'] = df['entities_hashtags'].apply(
                lambda z: [x.get("text", 'NaN') for x in [singleJSON for singleJSON in z]])
            df['source'] = df['source'].apply(lambda s: s[s.find('>') + 1:s.find('</a>')])

            del df['entities']
            del df['user']
            del df['entities_user_mentions']
            del df['entities_hashtags']
            df['entities_screen_name_list'] = [','.join(map(str, l)) for l in df['entities_screen_name_list']]
            df['entities_user_id_list'] = [','.join(map(str, l)) for l in df['entities_user_id_list']]
            df['entities_hashtags_list'] = [','.join(map(str, l)) for l in df['entities_hashtags_list']]
            df['trackDate'] = int(datetime.now().strftime('%Y%m%d%H%M%S'))

            df.to_csv(EXPORT_FOLDER + 'static_tweets.csv', mode='a',\
                               index=False, header=False)

            print(f"Account {tempName} has been added. ({i})")
            time.sleep(120)
        except Exception as e:
            print(f"Query for account {tempName} failed. ({i}) ({e})")



