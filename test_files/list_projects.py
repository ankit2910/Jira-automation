import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL")
api_token = os.getenv("API_TOKEN")
email = os.getenv("EMAIL")

auth = HTTPBasicAuth(email, api_token)

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