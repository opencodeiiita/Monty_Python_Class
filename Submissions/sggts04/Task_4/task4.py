import requests
import pprint

API_KEY = ''

response = requests.get(
    'https://developers.zomato.com/api/v2.1/search?entity_id=24&entity_type=city',
    headers = {'user-key': API_KEY},
)

for restaurant in response.json()['restaurants']:
    print(restaurant["restaurant"]["name"] + ": " + restaurant["restaurant"]["location"]["address"])