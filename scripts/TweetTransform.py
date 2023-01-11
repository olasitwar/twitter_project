def transform_json(tweet):
    print(tweet['text'])
    tempArray = []
    tempArray.append(tweet['created_at'])
    tempArray.append(tweet['id'])
    tempArray.append(tweet['text'])
    tempArray.append(tweet['user']['id'])
    tempArray.append(tweet['user']['screen_name'])
    tempArray.append(tweet['user']['created_at'])
    tempArray.append(tweet['user']['followers_count'])
    tempArray.append(tweet['user']['friends_count'])
    tempArray.append(tweet['user']['statuses_count'])
    tempArray.append(tweet['user']['favourites_count'])
    tempArray.append(tweet['entities']['user_mentions'])
    tempArray.append(tweet['entities']['hashtags'])
    tempArray.append(tweet['timestamp_ms'])
    return tempArray


"""
['created_at', 'id', 'id_str', 'text', 'source', 'truncated', 'in_reply_to_status_id',
    'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name',
    'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'quote_count', 'reply_count',
    'retweet_count', 'favorite_count', 'entities', 'favorited', 'retweeted', 'filter_level', 'lang',
    'timestamp_ms']
"""
