# Griffin did the following two lines to force his computer to 
# find cv2. There is a better way, this is just faster for now.
import sys
sys.path.append("/usr/local/lib/python3.7/site-packages/")

# import necessary libraries 
import glob
import cv2
import os

def getFileName(imagePath):
    """
    param   : string imagePath - path to pull file name from
    returns : string filename OR None if path doesn't have "/"
    """
    parts = imagePath.split("/")
    if len(parts) > 0:
        return parts[-1]
    return None

def findFace(imagePath,outPath):
    """ 
    Description:
        Implements Face Detection (not recognition)
        The function gets an input path for an image, then processes it looking 
        for the face(s). It then writes processed image to the out folder. 
        Future, we will write ONLY the part of the image with the face, so we can 
        do actual facial recognition on the images.
    Params:
        string imagePath : path of input image to process
        string outPath   : path of where to save processed images
    Returns:
        None

    """
    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    # print(faces)

    # Print how many faces found in image (not necessary)
    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # save our file to the specified folder
    fileName = getFileName(imagePath)
    cv2.imwrite(os.path.join(outPath,fileName),image)


# Set up where things are ...
inPath = "./input_files/"
outPath = "./output_files/"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# I added os.path.join to join our path parts correctly
# In lab, we used string concatenation
images = glob.glob(os.path.join(inPath,"*.jpg"))

for image in images:
    print(f"Processing: {getFileName(image)} ...")
    findFace(image,outPath)



