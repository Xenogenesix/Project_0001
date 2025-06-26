
from pprint import pprint
import requests
URL = 'https://dummyjson.com/todos'

response = requests.get(url=URL)


response_json = response.json()
pprint(response_json)
