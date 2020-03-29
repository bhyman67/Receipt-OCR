# Use the Taggun api to transcribe a reciept by uploading an image 
# file and then return the detailed result

# Dependencies
from TAGGUN_API_KEY import key
import pandas as pd
import requests
import json

# Web API that consists of HTTP request-response methods, all of the form
url = 'https://api.taggun.io/api/receipt/v1/simple/file'
 
# Data to pass along in the POST request
headers = {'apikey': key}
files = {
    'file': ('reciept.jpg', open('reciept.jpg', 'rb'), 'image/jpg'),
    'incognito': (None, 'false') 
  }

# API call (POST request to taggun at the simple/file endpoint)
resp = requests.post(url, headers = headers, files = files)
jsonResp = resp.json()

# Check out the response

print(json.dumps(jsonResp,indent=2, sort_keys=True))
print("+++++++")
print(resp.headers)

# put the data into a pandas data frame and export it to excel (the keys of the json should be the index of the DF)
# -> start off by looping thru all fo the keys 
listObj = []
for k in jsonResp:
  if k != "confidenceLevel":
    crntDict = jsonResp[k]
    listObj.append(
      (k,crntDict["data"],crntDict["confidenceLevel"])
    )

df = pd.DataFrame(listObj).set_index(0)
print(df)