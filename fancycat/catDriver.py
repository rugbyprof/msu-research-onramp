#!/usr/local/bin/python3
import json 
import requests
import pprint
from PIL import Image


def getCatJson(imageType=None):
    #valid = ['png','jpg','gif']

    if imageType == None:
        imageType = "gif,jpg,png"

    r = requests.get("https://api.thecatapi.com/v1/images/search?mime_types="+imageType)
    r.status_code # status of 200 means good 400+ or 500+ is bad
    r.headers['content-type']
    r.encoding
    return r.json()

def downLoadImage(url,ext,filename='cat'):
    r = requests.get(url)
    r.status_code # status of 200 means good 400+ or 500+ is bad
    r.headers['content-type']

    f = open(filename+"."+ext,"wb")
    f.write(r.content)
    f.close()

def showCat(path):
    im = Image.open(path)
    im.show()
    return im

    


catData = getCatJson("png")

url = catData[0]['url']

downLoadImage(url,'png')

im = showCat('cat.png')
print(im.format, im.size, im.mode)

height,width = im.size

pix = im.load()

for i in range(height-1):
    for j in range(width-1):
        r = pix[i,j][0]
        g = pix[i,j][1]
        b = pix[i,j][2]
        #a = pix[i,j][3]
        gray = int(r*.29+g*.58+b*.11 / 3)
        r=0
        pix[i,j] = (gray,gray,gray,255)

im.show()
