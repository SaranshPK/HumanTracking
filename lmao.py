from PIL import Image, ImageMath

im = Image.open("thermalpng.png")
pixdata = im.load()


for y in xrange(im.size[1]):
   for x in xrange(im.size[0]):
       if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2]>600):
           pixdata[x, y] = (0, 255, 0, 255)
         


im.show(im)