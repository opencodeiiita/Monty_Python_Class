import requests
import pprint
import json

apiKey= '4c5df1c9495811bc66dd4bda6310a69c'

resp = requests.get(
    'https://developers.zomato.com/api/v2.1/search?entity_id=24&entity_type=city',
    headers = {'user-key': apiKey},
)

for i in resp.json()['restaurants']:
    print(i["restaurant"]["name"] + ":  " + i["restaurant"]["location"]["address"])