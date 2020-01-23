import requests
import pprint
import json

api_key = '9256c4da4cc392d6134b674430344128'

resp = requests.get(
    'https://developers.zomato.com/api/v2.1/search?entity_id=24&entity_type=city',
    headers = {'user-key': api_key},
)

for rst in resp.json()['restaurants']:
    print(rst["restaurant"]["name"] + ":  " + rst["restaurant"]["location"]["address"])