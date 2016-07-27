from PIL import Image, ImageMath
from random import randint
from PIL import ImageOps


img = Image.open("thermalpng.png")
plouse = 0
list1 = []
mama = []
im = ImageOps.expand(img, border=1, fill='black')
pixdata = im.load()
threshold = 255

r = randint(0, 255) 
g = randint(0, 255)
b = randint(0, 255)
randomcol = (r, g, b, 255)

for y in xrange(im.size[1]):
	for x in xrange(im.size[0]):
		if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
			pixdata[x, y] = threshold


for x in xrange(im.size[1]):
	for y in xrange(im.size[0]):
		if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] == threshold):
			pixdata[x, y] =	randomcol
			if (pixdata[x + 1, y][0]+pixdata[x + 1, y][1]+pixdata[x + 1, y][2] == threshold) or (pixdata[x + 1, y][0]+pixdata[x + 1, y][1]+pixdata[x + 1, y][2] == 0):
				pixdata[x + 1, y] =	randomcol
				if (pixdata[x, y + 1][0]+pixdata[x, y + 1][1]+pixdata[x, y + 1][2] == threshold) or (pixdata[x, y + 1][0]+pixdata[x, y + 1][1]+pixdata[x, y + 1][2] == 0):
					pixdata[x, y + 1] =	randomcol
					if (pixdata[x - 1, y][0]+pixdata[x - 1, y][1]+pixdata[x - 1, y][2] == threshold) or (pixdata[x - 1, y][0]+pixdata[x - 1, y][1]+pixdata[x - 1, y][2] == 0):
						pixdata[x - 1, y] =	randomcol
						if (pixdata[x, y - 1][0]+pixdata[x, y - 1][1]+pixdata[x, y - 1][2] == threshold) or (pixdata[x, y - 1][0]+pixdata[x, y - 1][1]+pixdata[x, y - 1][2] == 0):		
							pixdata[x, y - 1] =	randomcol
			elif (pixdata[x + 1, y][0]+pixdata[x + 1, y][1]+pixdata[x + 1, y][2] != threshold):
				r = randint(0, 255) 
				g = randint(0, 255)
				b = randint(0, 255)
				randomcol = (r, g, b, 255)
				if (pixdata[x, y + 1][0]+pixdata[x, y + 1][1]+pixdata[x, y + 1][2] != threshold):
					r = randint(0, 255) 
					g = randint(0, 255)
					b = randint(0, 255)
					randomcol = (r, g, b, 255)
					if (pixdata[x, y - 1][0]+pixdata[x, y - 1][1]+pixdata[x, y - 1][2] != threshold):
						r = randint(0, 255) 
						g = randint(0, 255)
						b = randint(0, 255)
						randomcol = (r, g, b, 255)
						if (pixdata[x - 1, y][0]+pixdata[x - 1, y][1]+pixdata[x - 1, y][2] != threshold):
							r = randint(0, 255) 
							g = randint(0, 255)
							b = randint(0, 255)
							randomcol = (r, g, b, 255)
							plouse = plouse + 1
							pixdata[x, y] =	randomcol

print "The number of blobs is %s" % str(plouse)



im.show(im)