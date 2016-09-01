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


multiplicationFactor = 9

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        web.header("Access-Control-Allow-Origin","*")
        return json_data



if __name__ == "__main__":
    app.run()

class Blob:
    def __init__(self, blobSize,midpoint,blobID,blobPixels):
        self.blobSize = blobSize
        self.midpoint = midpoint
        self.blobID = blobID
        self.blobPixels = blobPixels


currentSize = 0
xSum = 0
ySum = 0
blobs = []
json_data = None
pixdata = None
image = None
localblobPixels = []


def reset():
    global xSum
    global ySum
    global currentSize
    xSum = 0
    ySum = 0
    currentSize = 0


def analyze():
    global xSum, ySum, currentSize, r, g, b, image, localblobPixels
    blobCount = 0
    tempBlobs = []
    for blob in blobs:
        tempBlobs.append(blob)
    for y in xrange(image.size[1]):
        for x in xrange(image.size[0]):
            if checkValid(x, y):
                localblobPixels = []
                reset()
                ySum += y
                xSum += x
                currentSize += 1
                pixdata[x, y] = (0, 0, 0)
                localblobPixels.append([x,y])
                fillAll(x, y)
                if currentSize > 10:
                    if xSum == 0:
                        xMid = x
                    else:
                        xMid = xSum / float(currentSize)

                    if ySum == 0:
                        yMid = y
                    else:
                        yMid = ySum / float(currentSize)
                    midpoint = [xMid, yMid]
                    minDist = 1000
                    closestBlob = None
                    for blob in tempBlobs:
                        dist = math.sqrt(math.pow(blob.midpoint[0] - midpoint[0], 2) + math.pow(blob.midpoint[1] - midpoint[1], 2))
                        if dist < minDist:
                            minDist = dist
                            closestBlob = blob
                    if (minDist < 20) and (minDist >= 0):
                        minIndex = blobs.index(closestBlob)
                        blobs[minIndex].midpoint = midpoint
                        blobs[minIndex].blobSize = currentSize
                        blobs[minIndex].blobPixels = localblobPixels
                        tempBlobs.remove(closestBlob)
                    else:
                        uid = uuid.uuid1()
                        uid_str = uid.urn
                        str = uid_str[9:]
                        blobs.append(Blob(currentSize, midpoint, str, localblobPixels))
    for blob in tempBlobs:
        blobs.remove(blob)


def fillUp(x, y):
    global ySum, xSum, currentSize, localblobPixels
    y -= 1
    if checkValid(x, y):
        pixdata[x, y] = (0, 0, 0)
        localblobPixels.append([x, y])
        ySum += y
        xSum += x
        currentSize += 1
        fillAll(x, y)


def fillRight(x, y):
    global ySum, xSum, currentSize, localblobPixels
    x += 1
    if checkValid(x, y):
        pixdata[x, y] = (0, 0, 0)
        localblobPixels.append([x, y])
        ySum += y
        xSum += x
        currentSize += 1
        fillAll(x, y)


def fillLeft(x, y):
    global ySum, xSum, currentSize, localblobPixels
    x -= 1
    if checkValid(x, y):
        pixdata[x, y] = (0, 0, 0)
        localblobPixels.append([x, y])
        ySum += y
        xSum += x
        currentSize += 1
        fillAll(x, y)


def fillDown(x, y):
    global ySum, xSum, currentSize, localblobPixels
    y += 1
    if checkValid(x, y):
        pixdata[x, y] = (0, 0, 0)
        localblobPixels.append([x, y])
        ySum += y
        xSum += x
        currentSize += 1
        fillAll(x, y)


def fillAll(x, y):
    fillUp(x, y)
    fillRight(x, y)
    fillDown(x, y)
    fillLeft(x, y)


def checkValid(x,y):
    if(x < image.size[0]) and (y < image.size[1] and (x >= 0) and (y >= 0)) and
        pixdata[x, y][0] + pixdata[x, y][1] + pixdata[x, y][2] > 350:
        return True
    else:
        return False


def obj_dict(obj):
    return obj.__dict__


def runCode():
    while True:
        global pixdata, json_data, image, multiplicationFactor
        FileName = "output.png"
        with Lepton() as l:
            a, _ = l.capture()
        cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)  # extend contrast

        np.right_shift(a, 8, a)  # fit data into 8 bits
        cv2.imwrite(FileName, np.uint8(a))
        image = Image.open(FileName)
        imageOrigin = Image.open(FileName)
        image = image.convert('RGB')
        pixdata = image.load()
        analyze()

        imageOrigin = imageOrigin.resize((80 * multiplicationFactor, 60 * multiplicationFactor))
        imageOrigin.save(FileName)

        with open(FileName, 'rb') as f:
            imdata = f.read()
            f.close()

        json_blobs = json.dumps(blobs, default=obj_dict)
        outjson = {
            "blobs": json.loads(json_blobs),
            "img": imdata.encode('base64'),
            "multiplicationFactor": multiplicationFactor
        }
        json_data = json.dumps(outjson)

try:
   thread.start_new_thread(runCode, ())
except:
   print "Error: unable to start thread"
