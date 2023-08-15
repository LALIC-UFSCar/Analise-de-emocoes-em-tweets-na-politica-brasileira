from retrieve_tweets import get_tweets
from drive_utils import auth, get_folder_id, dump_drive
import pandas as pd

if __name__ == "__main__":
    drive = auth()

    query = {
    "query": {
        "match" : {
            "entities.Tweet.user.id_str": "128372940"
        }
    }
        }

    tweets = get_tweets(query)

    dic = {
        'tweet_id': [],
        'user_id': [],
        'created_at': [],
        'tweet_text': [],
        'is_retweet': []
    }

    for i in tweets:
        dic['tweet_id'].append(i['id_str'])
        dic['user_id'].append(i['user']['id_str'])
        dic['created_at'].append(i['created_at'])
        dic['tweet_text'].append(i['string'])
        if 'retweeted_status' in i.keys():
            dic['is_retweet'].append(True)
        else:
            dic['is_retweet'].append(False)

    df = pd.DataFrame(dic)

    id_BEPE = get_folder_id(drive, 'BEPE')
    id_tweets_bolso = get_folder_id(drive, 'tweets_bolsonaro', id_BEPE)

    filename = 'tweets_bolsonaro.csv'
    filepath = '../data/tweets_bolsonaro/' + filename
    dump_drive(drive, id_tweets_bolso, df, filename, filepath)
