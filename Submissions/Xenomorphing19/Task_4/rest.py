import requests
import pprint
import json

api= '091d7292e0db4bf029e41565346d8b33'

req = requests.get(
    'https://developers.zomato.com/api/v2.1/search?entity_id=24&entity_type=city',
    headers = {'user-key': api},
)

for rest in req.json()['restaurants']:
    print(rest["restaurant"]["name"] + ":   " + rest["restaurant"]["location"]["address"])
