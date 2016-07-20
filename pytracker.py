from PIL import Image
im = Image.open("/Users/Abbad/Downloads/hell.png")
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((317,292))

print r, g, b

im.show(im)
