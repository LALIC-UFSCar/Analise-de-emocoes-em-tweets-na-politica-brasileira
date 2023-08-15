from elasticsearch import Elasticsearch
from yaml import safe_load

def elastic():
    config_path = '../config.yaml'
    with open(config_path) as f:
        complete = safe_load(f)
        endpoint = complete.get("elastic_endpoint")
    return Elasticsearch([endpoint])

def search_elastic(index, query):
    es = elastic()
    out = es.search(index=index,
                    body=query,
                    size=10000,
                    request_timeout=30)
    return out

def get_output(query, out, year, start, end):
    for week in range(start, end):
        if week < 10:
            week = '0' + str(week)
        index = 'covid-pt-' + str(year) + '-' + str(week)
        out.append(search_elastic(index, query))
    return out

def get_tweets(query):
    out = []
    out = get_output(query, out, 2020, 13, 53)
    out = get_output(query, out, 2021, 0, 53)
    out = get_output(query, out, 2022, 0, 22)
    tweets = []
    for output in out:
        for i in output['hits']['hits']:
            tweets.append(i['_source']['entities']['Tweet'][0])
    return tweets
