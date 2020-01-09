#!/usr/bin/python3

from PIL import Image
import numpy as np

# Convert Image to list
img = Image.open('image.png')
arr = np.array(img)
data = list(arr.ravel())

# White = 1, Black = 0
f = open('image.txt', 'w')
for count, num in enumerate(data, 0):
	if(count%3==0):
		if(num==0):
			f.write('0')
		else:
			f.write('1')

f.close()