from PIL import Image
class Blob:
    def __init__(self, blobSize,color,xValue,yValue,blobID):
        self.blobSize = blobSize
        self.color = color
        self.xValue = xValue
        self.yValue = yValue
        self.blobID = blobID
        self.fresh = True

xMidSum = 0
yMidSum = 0
xSum = 0
ySum = 0

up = False
right = False
left = False
down = False

upCount = 0
rightCount = 0
leftCount = 0
downCount = 0

currentSize = 0
blobs = []
filled = []
blobIDs = []

im = Image.open("thermalpng.png")
pix = im.load()
x = 100
y = 200
im.show()
print(im.size)
print(pix[x, y])
'''
def analyze():
    importantIndexes = []
    for x in 
'''
