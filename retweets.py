import re
import json
from itertools import islice

data = []

with open('tweets.json', 'r') as file:
    for json_obj in file:
        tweet_dict = json.loads(json_obj)
        data.append(tweet_dict)

data.sort(key=lambda x:x["retweetCount"])

def ten(n, iterable):
    return list(islice(iterable, n))

top = ten(2, data)
print(top)

## ordered = sorted(data, key= lamda k: k["retweetCount"])