# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

url = "https://luffy12.atlassian.net/rest/api/3/project"

load_dotenv()
api_token = os.getenv("API_TOKEN")

auth = HTTPBasicAuth("an.kit810716@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output[0]['name']
print(name)