import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
url = os.getenv("URL")
api_token = os.getenv("API_TOKEN")
email = os.getenv("EMAIL")

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    
    auth = HTTPBasicAuth(email, api_token)

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "fields": {
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "Create Jira for first issue",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "issuetype": {
          "id": "10005"
        },
        "project": {
          "id": "10000"
        },
        "summary": "Bug Jira",
      },
      "update": {}
    } )

    response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run(host='0.0.0.0', port=5000)