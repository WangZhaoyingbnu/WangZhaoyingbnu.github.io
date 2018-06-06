from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab as plb 
import os
import cv2
import xlwt
import xlsxwriter

box_hsv = [830, 520, 1030, 680] #left top right under// size 200*160   //hsv
box_hdv = [750, 450, 1400, 850] #left top right under// size 400*650   //hdv
'''
path = r'C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/picture_hsv'
path1 = r'C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/picture_cut_hdv/35/1.JPEG'
'''
path = r'C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/picture_hdv'
path1 = r'C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/picture_cut_hdv'

def ensure_dir(f):
	if not os.path.exists(f):
		os.makedirs(f)

for file in os.listdir(path):
	ensure_dir(path1 + '/' + file)

	def sub_path(x):
		return path + '/' + file + '/' + str(x) + '.JPEG'
	def sub_path1(y):
		return path1 + '/' + file + '/' + str(x) + '.JPEG'

	'''
	for x in [1, 2]:
		img = Image.open(sub_path(x))
		img2 = img.crop(box_hsv)
		img2.save(sub_path1(x))
	
	'''
	for x in [3, 4]:
		img = Image.open(sub_path(x))
		img2 = img.crop(box_hdv)
		img2.save(sub_path1(x))
	


		





