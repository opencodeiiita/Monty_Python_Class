import requests
import pprint
import json

Api_key = '894589fb8362485d348556dc398dfba4'

RSP = requests.get(
    'https://developers.zomato.com/api/v2.1/search?entity_id=24&entity_type=city',
    headers = {'user-key': Api_key},
)

for REST in RSP.json()['restaurants']:
    print(REST["restaurant"]["name"] + ":  " + REST["restaurant"]["location"]["address"])
