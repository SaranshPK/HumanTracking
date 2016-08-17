from PIL import Image, ImageMath
import operator
import math, os, sys
import inspect
import cv2
import json
from pylepton import Lepton
import time
import os
import sys
import numpy as np

saransh = 0


while saransh < 5:
        FileName = "hehe.png"
        with Lepton() as l:
                a,_ = l.capture()
        cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
        np.right_shift(a, 8, a)
        cv2.imwrite(FileName,np.uint8(a))
        image = Image.open(FileName)
        im = image.convert('RGB')
        pixdata = im.load()
	width, height = im.size
	sectorsearch = im.size[0]/3
	sector1 = []
	sector2 = []
	sector3 = []
	sectors = []
	threshold = 500

	for y in xrange(im.size[1]):
		for x in range(0, sectorsearch):
			if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] > threshold):
				sector1.append([x, y])
		for x in range(sectorsearch, sectorsearch*2):
			if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] > threshold):
				sector2.append([x, y])
		for x in range(sectorsearch*2, (sectorsearch*3)+2):
			if (pixdata[x, y][0]+pixdata[x, y][1]+pixdata[x, y][2] > threshold):
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

        quality_val = 80
        im.save(FileName)
        with open(FileName, 'rb') as f:
                imdata = f.read()
                f.close()
        outjson = {}
        outjson['im'] = imdata.encode('base64')
	saransh += 1
	im.show()
	
