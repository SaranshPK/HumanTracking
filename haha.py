from PIL import Image, ImageMath

im = Image.open("thermalpng.png")
pixdata = im.load()
plouse = 0



for y in xrange(im.size[1]):
   for x in xrange(im.size[0]):
       if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
           plouse = plouse + 1
           


print str(plouse)


im.show(im)