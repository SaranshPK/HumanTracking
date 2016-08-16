from PIL import Image, ImageMath
import operator
import math, os, sys
import inspect
import cv2
from matplotlib import pyplot as plt
import time

saransh = 0
vidcap = cv2.VideoCapture()

while saransh < 3:
	vidcap.open(0)
	retval, image = vidcap.retrieve()
	cv2.imwrite("hehe.png", image)
	im = Image.open("hehe.png")
	pixdata = im.load()
	width, height = im.size
	sectorsearch = im.size[0]/3
	sector1 = []
	sector2 = []
	sector3 = []
	sectors = []
	threshold = 1

	for y in xrange(im.size[1]):
		for x in range(0, sectorsearch):
			if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] < threshold):
				sector1.append([x, y])
		for x in range(sectorsearch, sectorsearch*2):
			if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] < threshold):
				sector2.append([x, y])
		for x in range(sectorsearch*2, (sectorsearch*3)+2):
			if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] < threshold):
				sector3.append([x, y])

	sectors.append(sector1)
	sectors.append(sector2)
	sectors.append(sector3)

	def my_sorted(in_list, key=lambda x:x):
	    key_map = map(lambda x: (key(x),x), in_list)
	    key_map.sort()
	    return [x for _,x in key_map]

	sortedsectors = my_sorted(sectors, key=len)

	print len(sortedsectors[0])
	print len(sortedsectors[1])
	print len(sortedsectors[2])

	i = 0
	for sector in sortedsectors:
		for [x, y] in sector:
			if(i==2):
				pixdata[x, y] = (255, 0, 0, 255)
			if(i==1):
				pixdata[x, y] = (255, 255, 0, 255)
			if(i==0):
				pixdata[x, y] = (0, 255, 0, 255)
		i+=1

	
	saransh += 1
	im.show()
	