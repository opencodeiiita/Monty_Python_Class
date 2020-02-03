import requests
import pprint
import json

api_zomato = 'be1083e0f3d30bf3bc96fe21ad54220f'

resp = requests.get(
    'https://developers.zomato.com/api/v2.1/search?entity_id=24&entity_type=city',
    headers = {'user-key': api_zomato},
)

for num in resp.json()['restaurants']:
    print(num["restaurant"]["name"] + ":  " + num["restaurant"]["location"]["address"])