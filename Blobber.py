from PIL import Image, ImageMath
from random import randint
from PIL import ImageOps
import time
start_time = time.time()

im = Image.open("thermalpng.png")
NumOfBlobs = 0
BlobColors = []
pixdata = im.load()
colorer = []
colorof = []


#Random Color Generator

r = randint(0, 255) 
g = randint(0, 255)
b = randint(0, 255)

randomcolor = (r, g, b, 255)



for y in xrange(im.size[1]):
	for x in xrange(im.size[0]):
		if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
			colorer.append([x, y])
			colorof.append(pixdata[x, y])




for [x, y] in colorer:
	pixdata[x, y] = randomcolor
	if (pixdata[x + 1, y] > 600):
		pixdata[x + 1, y] = randomcolor
		if (pixdata[x - 1, y] > 600):
			pixdata[x - 1, y] = randomcolor
			if (pixdata[x, y + 1] > 600):
				pixdata[x, y + 1] = randomcolor
		
	elif (pixdata[x + 1, y] < 600):
		r = randint(0, 255) 
		g = randint(0, 255)
		b = randint(0, 255)

		randomcolor = (r, g, b, 255)
'''


for x in range(im.size[0]):
	for y in xrange(im.size[1]):
		if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
			pixdata[x, y] = randomcolor
			if (pixdata[x + 1, y][0]+pixdata[x + 1, y][1]+pixdata[x + 1, y][2]>600):
				pixdata[x + 1, y] = randomcolor
				if (pixdata[x - 1, y][0]+pixdata[x - 1, y][1]+pixdata[x - 1, y][2]>600):
					pixdata[x - 1, y] = randomcolor
					if (pixdata[x, y + 1][0]+pixdata[x, y + 1][1]+pixdata[x, y + 1][2]>600):
						pixdata[x, y + 1] = randomcolor
						if (pixdata[x, y - 1][0]+pixdata[x, y - 1][1]+pixdata[x, y - 1][2]>600):
							pixdata[x, y - 1] = randomcolor
		elif (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]<600):
			r = randint(0, 255) 
			g = randint(0, 255)
			b = randint(0, 255)
			lmao = (r, g, b, 255)
'''
'''
for [x, y] in colorer:
	if (pixdata[x + 1, y] > 600):
		pixdata[x, y] = randomcolor
	el:
		r = randint(0, 255) 
		g = randint(0, 255)
		b = randint(0, 255)

		randomcolor = (r, g, b, 255)

'''

im.show(im)

print("--- %s seconds ---" % (time.time() - start_time))
