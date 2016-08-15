from PIL import Image, ImageMath
import operator
import math, os, sys

im = Image.open("ok2.png")
pixdata = im.load()
width, height = im.size
sectorsearch = im.size[0]/3
sector1 = []
sector2 = []
sector3 = []
sectors = []


for y in xrange(im.size[1]):
	for x in range(0, sectorsearch):
		if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] < 1):
			sector1.append([x, y])
	for x in range(sectorsearch, sectorsearch*2):
		if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] < 1):
			sector2.append([x, y])
	for x in range(sectorsearch*2, sectorsearch*3):
		if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] < 1):
			sector3.append([x, y])

sectors.append(sector1)
sectors.append(sector2)
sectors.append(sector3)

print len(sector1)
print len(sector2)
print len(sector3)

i = 0
w = 0
j = 0
for sector in sectors:
	if(len(sector)>w):
		w = len(sector)
		i = j
	j+=1

for [x, y] in sectors[i]:
	pixdata[x, y] = (0, 255, 0, 255)


im.show()