from PIL import Image, ImageMath
from random import randint

im = Image.open("thermalpng.png")
pixdata = im.load()
plouse = 0
coco = []
width, height = im.size
ply = []
mama = (255, 255, 255, 255)


r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

lmao = (r, g, b, 255)


for y in xrange(im.size[1]):
   for x in xrange(im.size[0]):
       if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
           coco.append([x, y])
           pixdata[x, y] = lmao


for [x, y] in coco:
	if ((pixdata[x+1, y] == lmao) and (pixdata[x-1, y] == lmao) and (pixdata[x, y+1] == lmao) and (pixdata[x, y-1] == lmao)):
		ply.append([x, y])
		plouse = plouse + 1
	else: 
		pixdata[x, y] = mama
		plouse = plouse + 1

for [x, y] in ply:
	pixdata[x, y] = lmao



print str(plouse)



im.show(im)