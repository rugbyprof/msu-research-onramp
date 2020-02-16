#!/usr/local/bin/python3
import json 
import requests


r = requests.get('https://api.thecatapi.com/v1/images/search')
r.status_code # status of 200 means good 400+ or 500+ is bad
r.headers['content-type']
r.encoding

catData = r.json()

print(catData)

f = open("catData.json","w") 
f.write(json.dumps(catData,indent=4))
f.close()

