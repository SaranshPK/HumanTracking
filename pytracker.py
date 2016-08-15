from PIL import Image, ImageMath

im = Image.open("thermalpng.png")
pixdata = im.load()
aList = []
i = 0

for y in xrange(im.size[1]):
   for x in xrange(im.size[0]):
       if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
           pixdata[x, y] = (0, 255, 0, 255)
'''         

for y in xrange(im.size[1]):
    for x in xrange(im.size[0]):
        if (pixdata[x, y][1] == 255):
        	if (pixdata[x+1, y][1] != 255) or (pixdata[x-1, y][1] != 255) or (pixdata[x, y+1][1] != 255) or (pixdata[x, y-1][1] != 255):
        		aList.append([x, y])
        		
for coord in aList:
	pixdata[coord] = (0, 0, 0, 0)

'''       
        		

im.show(im)