#!/usr/bin/python3

from PIL import Image
import numpy as np
import re

with open('jjofpbwvgk.txt') as f:
	s = f.read()
	
# Read all numbers
l = re.findall(r'\d+',s)

# Convert to array
data = np.array(l).reshape((600,400,3))

img = Image.fromarray(data.astype('unit8'), 'RGB')
img.save('result.png')