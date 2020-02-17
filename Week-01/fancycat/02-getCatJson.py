#!/usr/local/bin/python3

"""
This file uses `requests` to go out to the internet and grabs a 
random json object that contains info about a random cat image.
"""
import json 
import requests


# do the request (go to that web link and pull the response back here)
# You can simple put the url from below into a web browser and "look" at the result
r = requests.get('https://api.thecatapi.com/v1/images/search')

# status of the request so we can determine if it was successful
r.status_code # status of 200 means good 400+ or 500+ is bad

# `content-type` tells us if its:
#   binary (like a program or a )
#   text   (like html or actual txt)
#   image  (png, jpg, gif, and more)
#   and more !
r.headers['content-type']

# what type of character encoding does this response have:
#    unicode
#    ascii
#    utf-8 **typical
#    and more !
r.encoding

# get the json data from the response
catData = r.json()

"""
Example response from previous line:
[
    {
        'breeds': [], 
        'id': 'MTUwNzA3Mw', 
        'url': 'https://cdn2.thecatapi.com/images/MTUwNzA3Mw.png', 
        'width': 500, 
        'height': 741
    }
]
"""

# dump json to console
print(catData)

# open a local file for writing
f = open("catData.json","w") 

# write the json to the local file making it 
# readable with indents of 4 spaces
f.write(json.dumps(catData,indent=4))

# close our local file
f.close()

