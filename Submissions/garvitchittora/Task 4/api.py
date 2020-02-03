import requests
import pprint
import json

apino = '81ff2f9ef474fbcf7b264b37027e978d'

file = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=24&entity_type=city',headers = {'user-key': apino},)

for restaurants in file.json()['restaurants']:
    print(restaurants["restaurant"]["name"] + ":  " + restaurants["restaurant"]["location"]["address"])