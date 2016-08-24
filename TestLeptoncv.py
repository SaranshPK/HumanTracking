import numpy as np
import json
import cv2
import time
import sys
import os
import thread
import uuid
import math
import web
from PIL import Image
from pylepton import Lepton
from random import randint
sys.setrecursionlimit(10000)

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        return json_data


if __name__ == "__main__":
    app.run()

class Blob:
    def __init__(self, blobSize,midpoint,blobID):
        self.blobSize = blobSize
        self.midpoint = midpoint
        self.blobID = blobID


currentSize = 0
upCount = 0
rightCount = 0
leftCount = 0
downCount = 0
xMidSum = 0
yMidSum = 0
xSum = 0
ySum = 0
r = 0
g = 0
b = 0
blobs = []
json_data = None
pixdata = None
image = None


def reset():
    global upCount
    global rightCount
    global leftCount
    global downCount
    global xMidSum
    global yMidSum
    global xSum
    global ySum
    global currentSize
    upCount = 0
    rightCount = 0
    leftCount = 0
    downCount = 0
    xMidSum = 0
    yMidSum = 0
    xSum = 0
    ySum = 0
    currentSize = 0


def analyze():
    global upCount, rightCount, leftCount, downCount, xMidSum, yMidSum, xSum, ySum, currentSize, r, g, b, image
    blobCount = 0
    tempBlobs = blobs
    for y in xrange(image.size[1]):
        for x in xrange(image.size[0]):
            if (checkValid(x,y)):
                reset()
                r = randint(0, 100)
                g = randint(0, 100)
                b = randint(0, 100)
                currentSize+=1
                fillAll(x,y)
                if currentSize > 10:
                    if xSum == 0:
                        xMid = x
                    else:
                        xMid = xMidSum /xSum + x

                    if ySum == 0:
                        yMid = y
                    else:
                        yMid = yMidSum /ySum + y
                    midpoint = [xMid,yMid]
                    minDist = 1000
                    closestBlob = None
                    for blob in tempBlobs:
                        dist = math.sqrt(math.pow(blob.midpoint[0], 2) + math.pow(blob.midpoint[1], 2))
                        if dist < minDist:
                            minDist = dist
                            closestBlob = blob
                    if (minDist < 40) and (minDist >= 0):
                        minIndex = blobs.index(closestBlob)
                        blobs[minIndex].midpoint = midpoint
                        blobs[minIndex].blobSize = currentSize
                        tempBlobs.remove(closestBlob)
                    else:
                        uid = uuid.uuid1()
                        uid_str = uid.urn
                        str = uid_str[9:]
                        blobs.append(Blob(currentSize, midpoint, str))
    for blob in tempBlobs:
        blobs.remove(blob)


def fillUp(x,y):
    global upCount, downCount, yMidSum, ySum, currentSize, r, g, b
    y = y - 1
    if(checkValid(x,y)):
        pixdata[x,y] = (r, g, b)

        ySum+=1
        upCount+=1
        downCount -= 1
        yMidSum -= upCount
        currentSize += 1
        fillAll(x,y)


def fillRight(x,y):
    global rightCount, leftCount, xMidSum, xSum, currentSize, r, g, b
    x = x + 1
    if(checkValid(x,y)):
        pixdata[x,y] = (r, g, b)

        xSum += 1
        rightCount += 1
        leftCount -= 1
        xMidSum += rightCount
        currentSize += 1
        fillAll(x,y)


def fillLeft(x,y):
    global rightCount, leftCount, xMidSum, xSum, currentSize, r, g, b
    x = x - 1
    if(checkValid(x,y)):
        pixdata[x,y] = (r, g, b)

        xSum+=1
        leftCount+=1
        rightCount-=1
        xMidSum-=leftCount
        currentSize += 1
        fillAll(x,y)


def fillDown(x,y):
    global upCount, downCount, yMidSum, ySum, currentSize, r, g, b
    y = y + 1
    if(checkValid(x,y)):
        pixdata[x,y] = (r, g, b)

        ySum+=1
        downCount+=1
        upCount-=1
        yMidSum+=downCount
        currentSize += 1
        fillAll(x,y)


def fillAll(x,y):
    fillUp(x,y)
    fillRight(x,y)
    fillDown(x,y)
    fillLeft(x,y)


def checkValid(x,y):
    if(x<image.size[0]) and (y<image.size[1] and (x >= 0) and (y >= 0)):
        if(pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>400):
            return True
        else:
            return False
    else:
        return False

def obj_dict(obj):
    return obj.__dict__

def runCode():
    while True:
        global pixdata, json_data, image
        FileName = "output.png"
        with Lepton() as l:
            a, _ = l.capture()
        cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)  # extend contrast

        np.right_shift(a, 8, a)  # fit data into 8 bits
        cv2.imwrite(FileName, np.uint8(a))
        image = Image.open(FileName)
        image = image.convert('RGB')
        pixdata = image.load()
        analyze()
        image = image.resize((80 * 9, 60 * 9))

        quality_val = 80
        image.save(FileName)

        with open(FileName, 'rb') as f:
            imdata = f.read()
            f.close()

        outjson = {}
        outjson['img'] = imdata.encode('base64')
        json_blobs = json.dumps(blobs, default=obj_dict)
        outjson['blobs'] = json_blobs
        json_data = json.dumps(outjson)

try:
   thread.start_new_thread(runCode, ())
except:
   print "Error: unable to start thread"
