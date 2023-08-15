from retrieve_tweets import get_tweets
from drive_utils import auth, get_folder_id, dump_drive, get_fileList, in_folder
import pandas as pd

def write_query(tweet_id):
    query = {
        "query": {
            "match": {
                "entities.Tweet.in_reply_to_status_id_str": tweet_id
            }
        }
    }
    return query

def get_df(tweets, tweet_id):
    dic = {
        'tweet_id': [],
        'created_at': [],
        'timestamp_ms': [],
        'tweet_text': [],
        'id_tweet_reply': []
    }
    for i in tweets:
        dic['tweet_id'].append(i['id_str'])
        dic['created_at'].append(i['created_at'])
        dic['timestamp_ms'].append(i['timestamp_ms'])
        dic['tweet_text'].append(i['string'])
        dic['id_tweet_reply'].append(tweet_id)
    return pd.DataFrame(dic)


if __name__ == "__main__":
    drive = auth()
    df = pd.read_csv('../data/tweets_bolsonaro/tweets_bolsonaro.csv')

    id_BEPE = get_folder_id(drive, 'BEPE')
    id_replies_bolso = get_folder_id(drive, 'replies_bolsonaro', id_BEPE)
    fileList = get_fileList(drive, id_replies_bolso)

    print(len(df))
    for index, i in enumerate(df.iloc()):
        if i['is_retweet'] == False:
            tweet_id = i['tweet_id']
            filename = str(tweet_id) + '.csv'
            if not in_folder(fileList, filename):
                filepath = '../data/replies_bolsonaro/' + filename
                query = write_query(tweet_id)
                tweets = get_tweets(query)
                df = get_df(tweets, tweet_id)
                dump_drive(drive, id_replies_bolso, df, filename, filepath)
            if index%500 == 0:
                print(index)
