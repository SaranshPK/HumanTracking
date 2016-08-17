from PIL import Image, ImageMath
import operator
import math, os, sys
import inspect
import cv2
from matplotlib import pyplot as plt
import time

saransh = 0
vidcap = cv2.VideoCapture()

while saransh < 5:
	vidcap.open(0)
	retval, image = vidcap.retrieve()
	cv2.imwrite("hehe.png", image)
	im = Image.open("hehe.png")
	pixdata = im.load()
	width, height = im.size
	sectorsearch = im.size[0]/10
	sectorsearch2 = im.size[1]/10
	threshold = 1
	plouse = 0

	while plouse < 11:
		for y in range(sectorsearch2[plouse - 1], sectorsearch2[plouse]):
			for x in range(sectorsearch[plouse - 1], sectorsearch[plouse]):
				sectors.append(sector)
		for sector in sectors:
			for [x, y] in sector:
				if ((pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2])/len(sector) > 1):
					pixdata[x, y] = (0, 0, 0, 0)
	plouse = plouse + 1

	
	saransh += 1
	im.show()
