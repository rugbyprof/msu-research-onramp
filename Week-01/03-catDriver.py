#!/usr/local/bin/python3
import json             # library to parse json files
import requests         # allows us to make "web" requests
import pprint           # print things to console in a formatted way
from PIL import Image   # image processing library
import os               # so we can do system calls (like checking files exist)

def getCatJson(imageType=None):
    """
    @description:   
        This function uses the `requests` libaray to download a json object from
        a freely available API. The json contains a link to an image that we will
        subsequently download later. Could have downloaded image here, but functions
        should be define to do one thing, and do it well ...

    @params:
         imageType : defaults to `None` but valid inputs are: ['png','jpg','gif']
    @returns:
        Example:
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
    # List of valid (allowable image types)
    valid = ['png','jpg','gif']

    # If the imageType is empty, make it ALL of them
    if imageType == None:
        imageType = "gif,jpg,png"
    else:
        # its not empty, so lets error check and see if
        # the value is in our "valid" List
        if not imageType in valid:
            print(f"Error=> imageType: {imageType} is not valid!")
            print("Stopping program ... ")
            return None

    # Go out to web and ask API for a cat image
    r = requests.get("https://api.thecatapi.com/v1/images/search?mime_types="+imageType)

    # get the status code of the request
    # 200 means good 400+ or 500+ is bad
    r.status_code 

    if r.status_code != 200:
       print("Error: failed to get resource from API call ... ")
       return None

    # Assumes everything worked out. We could have done more error checking
    # with `r.headers['content-type']` or possibly `r.encoding`
    return r.json()

def downLoadImage(url,ext,filename='cat'):
    """
    @description: 
        This function uses the `requests` libaray to download a cat image from
        a freely available API. Pics tend to be creepy, but it worked for our purposes.

    @params:
        url      : http resource path
        ext      : the file extension to help name the file
        filename : what to name the downloaded file
    """
    # Go get our image
    r = requests.get(url)

    # get the status code of the request
    # 200 means good 400+ or 500+ is bad
    r.status_code

    # open a local file for "w" = writing and "b" = binary 
    f = open(filename+"."+ext,"wb")

    # write out the contents of the request from above to our new file
    f.write(r.content)

    # close the file
    f.close()


def showCat(path):
    """
    @description: 
        This function uses PIL to open some image in a window
        for viewing purposes :)
    @params:
        path: the path to the image to be opened
    """

    if not os.path.isfile(path):
        print(f"Error => Path: {path} is not valid!")
        return None
    
    # to to path, and set `im` to be its "handle" (so we can run methods on it)
    im = Image.open(path)

    # .show() is a "method" being applied to `im` asking the operating system
    # to "show" this image.
    im.show()

    # return our image resource "im" allowing us to run more methods on the opened
    # image if we want.
    return im

def grayScale(im):

    imgray = im

    # im.size returns (width,height) and the
    # assignment below pulls them out into the
    #individual variables 
    height,width = imgray.size

    # get the pixel color values as a list
    # Example:
    #  [
    #    (123,234,124,255)
    #    ...
    #    (200,122,88,255) 
    #  ]
    pix = imgray.load()

    # loop through the list of colors and calculate
    # a grayscale value 
    # Grayscale means the R,G,B values in the color are 
    # all the same like (123,123,123). So if we average
    # the three values, then assign them back to the 
    # r and the g and the b, we make it grayscale.
    # The values .3,.6, and .1 are to give that particular
    # channel more weight in determining the color of gray 
    for i in range(height-1):
        for j in range(width-1):
            r = pix[i,j][0]
            g = pix[i,j][1]
            b = pix[i,j][2]
            #a = pix[i,j][3]
            gray = int(r*.3+g*.6+b*.1 / 3)
            r=0
            pix[i,j] = (gray,gray,gray,255)

    # return our grayscaled image
    return imgray

def main():
    # go to web and get us some json data with a cat image link in it. 
    catData = getCatJson("png")

    print(catData)

    # pull the url out of the "json" object that
    # was returned by `getCatJson("png")`
    url = catData[0]['url']

    # save image from API to our local disk so we can open it and edit it
    downLoadImage(url,'png')

    # Show the image!!
    im = showCat('cat.png')

    # print out some image info (just for us to see some info about the image)
    print(im.format, im.size, im.mode)

    # make our cat grayscale
    imgray = grayScale(im)

    # show the gray image
    imgray.show()

# This code block runs when the file is called directly
# for you new to programming, I'll explain in a subsequent
# meeting
if __name__=='__main__':
    # call our main function to make things happen
    main()