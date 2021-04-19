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
#for i in range(2):
#  response = requests.request("POST", url, headers=headers, data=payload)
#  print(response.text)



import requests
import json
import hashlib
import base64
import time
import hmac

#Account Info
AccessId ='48v2wRzfK94y53sq5EuF'
AccessKey ='H_D9i(f5~B^U36^K6i42=^nS~e75gy382Bf6{)P+'
Company = 'api'

#Request Info
httpVerb ='GET'
resourcePath = '/device/devices'
queryParams =''
data = ''

#Construct URL
url = "http://127.0.0.1:8000/bookstore/"

#Get current time in milliseconds
epoch =str(int(time.time() * 1000))

#Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

#Construct signature
hmac = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac.encode())

#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type':'application/json'}

#Make request
response = requests.get(url, data=data, headers=headers)

#Print status and body of response
print ('Response Status:',response.status_code)
print ('Response Body:',response.content)

