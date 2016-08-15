#!/usr/bin/env python

import socket
import sys
import os
import time
from PIL import Image
from random import randint
import numpy

from PIL import Image, ImageOps, ImageEnhance, ImageFont, ImageDraw

sys.setrecursionlimit(10000)

os.system("./agcenable.exe")

# font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",6)

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
    print blobCount

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


text = 1
tcolor = (255, 255, 0)
text_pos = (0, 0)
framecounter = 0

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the port
server_address = ('', 8080)
print 'starting up on %s port %s' % server_address

sock.bind(server_address)
sock.listen(1)
try:

    while True:

        print 'waiting for a connection'
        connection, client_address = sock.accept()

        connection.sendall("HTTP/1.1 200 OK\n")
        # headers = {'Content-Type': 'multipart/x-mixed-replace;boundary=--informs','Access-Control-Allow-Origin': '*'};
        connection.sendall("Content-Type: multipart/x-mixed-replace;boundary=--informs\n")
        connection.sendall("Access-Control-Allow-Origin: *\n")
        # connection.sendall("Transfer-Encoding: chunked\n")

        while (True):

            var = os.system("./frame.exe")

            if (var == 0):

                data = numpy.loadtxt("/run/shm/Numpey.dat", numpy.uint8)

                framecounter = framecounter + 1
                #print "frame: " + str(framecounter)

                image = Image.fromarray(data)

                # image.putpalette(HeatMap)
                image = image.convert('RGB')

                pixdata = image.load()
                analyze()
                
                # image = image.rotate(90).resize((80*5, 60*5), Image.ANTIALIAS)
                image = image.rotate(0).resize((80 * 9, 60 * 9))

                # draw = ImageDraw.Draw(image)
                # draw.text(text_pos, str(framecounter), fill=tcolor, font=font)

                TmpFileName = "/dev/shm/latest.jpg"

                quality_val = 80
                image.save(TmpFileName, quality=quality_val)

                connection.sendall("\n--informs\n")
                connection.sendall("Content-Type: image/jpeg\n")
                connection.sendall("Content-Length: " + str(os.stat(TmpFileName).st_size) + "\n\n")
                #print "Image Size: " + str(os.stat(TmpFileName).st_size)

                with open(TmpFileName, 'rb') as f:
                    data = f.read()
                    f.close()

                connection.sendall(data)
                connection.sendall("\n")
                connection.sendall("")

                time.sleep(.10)
            else:
                #print "\nWarning failed read"
                time.sleep(.05)


finally:
    # Clean up the connection
    connection.close()
