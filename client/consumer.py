import requests
import json

url = "http://127.0.0.1:8000/bookstore/"

payload = json.dumps({
  "title": "Devendra k Jha",
  "author": "Alex",
  "book_description": "Python 3.6x engineering",
  "cost": 153,
  "create_time": "2021-04-21T00:33:41+00:00"
})
headers = {
  'Content-Type': 'application/json'
}
for i in range(2):
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
