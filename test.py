from PIL import Image
from random import randint
class Blob:
    def __init__(self, blobSize,color,midpoint,blobID):
        self.blobSize = blobSize
        self.color = color
        self.midpoint = midpoint
        self.blobID = blobID
        self.fresh = True

r = randint(0, 255) 
g = randint(0, 255)
b = randint(0, 255)

rcolor = (r, g, b, 255)

currentSize = 0

upCount = 0
rightCount = 0
leftCount = 0
downCount = 0

xMidSum = 0
yMidSum = 0
xSum = 0
ySum = 0

blobs = []

im = Image.open("thermalpng.png")
pixdata = im.load()


def reset():
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
    importantIndexes = []
    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
                pixdata[x,y] = (0,255,0,255)
                importantIndexes.append([x,y])
    for pixel in importantIndexes:
        if (checkValid(pixel)):
            reset()
            pixdata[pixel[0],pixel[1]] = rcolor
            fillAll(pixel)
            if((xSum != 0) or (ySum != 0)):
                xMid = xMidSum /(xSum) + pixel[x]
                yMid = yMidSum /(ySum) + pixel[y]
                midpoint = [xMid,yMid]
                pixdata[midpoint[0],midpoint[1]] = rcolor
                print mindpoint
		elif:
			r = randint(0, 255) 
			g = randint(0, 255)
			b = randint(0, 255)

			rcolor = (r, g, b, 255)

def fillUp(pixel):
    if(checkValid(pixel)):
        pixdata[pixel[0],pixel[1]] = rcolor
        pixel[1] = pixel[1]-1
        ySum+=1
        upCount+=1
        downCount-=1
        yMidSum-=upCount
        fillAll(pixel)
    else:
		r = randint(0, 255) 
		g = randint(0, 255)
		b = randint(0, 255)

		rcolor = (r, g, b, 255)

def fillRight(pixel):
    if(checkValid(pixel)):
        pixdata[pixel[0],pixel[1]] = rcolor
        pixel[0] = pixel[0]+1
        xSum+=1
        rightCount+=1
        leftCount-=1
        xMidSum+=rightCount
        fillAll(pixel)
    else:
		r = randint(0, 255) 
		g = randint(0, 255)
		b = randint(0, 255)
		rcolor = (r, g, b, 255)

def fillDown(pixel):
    if(checkValid(pixel)):
        pixdata[pixel[0],pixel[1]] = rcolor
        pixel[1] = pixel[1]+1
        xSum+=1
        leftCount+=1
        rightCount-=1
        xMidSum-=leftCount
        fillAll(pixel)

	else:
       	r = randint(0, 255) 
		g = randint(0, 255)
		b = randint(0, 255)

		rcolor = (r, g, b, 255)



def fillLeft(pixel):
    if(checkValid(pixel)):
        pixdata[pixel[0],pixel[1]] = rcolor
        pixel[0] = pixel[0]-1
        ySum+=1
        downCount+=1
        upCount-=1
        yMidSum+=downCount
        fillAll(pixel)
    else:
		r = randint(0, 255) 
		g = randint(0, 255)
		b = randint(0, 255)
		rcolor = (r, g, b, 255)

def fillAll(pixel):
    fillUp(pixel)
    fillRight(pixel)
    fillDown(pixel)
    fillLeft(pixel)

def checkValid(pixel):
    if((pixdata[pixel[0],pixel[1]] == (0, 255, 0, 255)) and (pixel[0] >= 0) and (pixel[1] >= 0) and (pixel[0]<im.size[0]) and (pixel[1]<im.size[1])):
        return True
    else:
        return False

analyze()
im.show()
