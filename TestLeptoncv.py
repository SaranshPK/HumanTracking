import numpy as np
import json
import cv2
import time
import sys
import os
from PIL import Image
from pylepton import Lepton
from random import randint
sys.setrecursionlimit(10000)


class Blob:
    def __init__(self, blobSize,color,midpoint,blobID):
        self.blobSize = blobSize
        self.color = color
        self.midpoint = midpoint
        self.blobID = blobID
        self.fresh = True


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
    global upCount, rightCount, leftCount, downCount, xMidSum, yMidSum, xSum, ySum, currentSize, r, g, b
    importantIndexes = []
    for y in xrange(image.size[1]):
        for x in xrange(image.size[0]):
            if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
                pixdata[x,y] = (0,255,0)
                importantIndexes.append([x, y])
    blobCount = 0
    for pixel in importantIndexes:
        if (checkValid(pixel[0],pixel[1])):
            reset()
            r = randint(0, 254)
            g = randint(0, 254)
            b = randint(0, 254)
            pixdata[pixel[0],pixel[1]] = (r,g,b)
            blobCount+=1
            fillAll(pixel[0],pixel[1])
            if(xSum == 0):

                xMid = pixel[0]
            else:
                xMid = xMidSum /(xSum) + pixel[0]

            if (ySum == 0):
                yMid = pixel[1]
            else:
                yMid = yMidSum /(ySum) + pixel[1]
            midpoint = [xMid,yMid]


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
        if(pixdata[x,y] == (0, 255, 0)):
            return True
        else:
            return False
    else:
        return False

while True:
    FileName = "output.png"
    with Lepton() as l:
        a,_ = l.capture()
    cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) # extend contrast

    np.right_shift(a, 8, a) # fit data into 8 bits
    cv2.imwrite(FileName,np.uint8(a))
    image = Image.open(FileName)
    image = image.convert('RGB')
    pixdata = image.load()
    analyze()

    quality_val = 80
    image.save(FileName)

    with open(FileName, 'rb') as f:
        imdata = f.read()
        f.close()

    outjson = {}
    outjson['img'] = imdata.encode('base64')
    outjson['blobs'] = blobs
    json_data = json.dumps(outjson)

    print json_data
    time.sleep(0.1) 
