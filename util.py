from __future__ import division
from skimage.filters import gaussian
import cv2
import numpy


def blur(image):
    """ Returns a blurred (radius=2 pixels) version of the image """
    return gaussian(image.astype(float), sigma=2)


def resize(image_size, video_size):
	width_diff = image_size[0] - video_size[0]
	height_diff = image_size[1] - video_size[1]
	if max(width_diff, height_diff) > 1:
		if width_diff > width_diff:
			return video_size[0]/image_size[0]
		else:
			return video_size[1]/image_size[1]
	else:
		return 1

def avg_color(image):
	myimg = cv2.imread(image)
	avg_color_per_row = numpy.average(myimg, axis=0)
	avg_color = numpy.average(avg_color_per_row, axis=0)
	return avg_color[::-1]

def invert_color(color):
	return "#"+"".join([hex(int(255-color[0]))[2:], hex(int(255-color[1]))[2:], hex(int(255-color[2]))[2:]])

def insert_newlines(string, every=64):
    lines = []
    previous_text = ''
    j = 0
    for i in range(0, len(string), every):
    	text = string[i-j:i+every]
    	if len(text) >= every:
    		text = text.rpartition(' ')
    		previous_text = text[2].strip()
    		j = len(previous_text)
    		lines.append(text[0])
    	else:
    		lines.append(text)
    return '\n'.join(lines)

