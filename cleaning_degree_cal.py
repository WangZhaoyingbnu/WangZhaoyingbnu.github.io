#coding = utf-8
"""
@author: Ann
"""
import math
import numpy as np
import os
import scipy.io as scio
from scipy.misc import imread 
from PIL import Image
from numpy import reshape
#pixel in standard picture:[RGB]
#mode   [46, 60, 68]
#median [66, 79, 93]
#mean   [75, 85, 96]
#min    [21, 0, 50]
#max    [255, 156, 194]
R = [46, 75]
G = [60, 85]
B = [68, 96]



path = 'C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/picture_cut_hsv'
def per_pixel(P, x):
	if x < P[0]:
		return np.square((P[0] - x)/(P[1] - P[0]))
	elif x < P[1]:
		return 0
	else:
		return np.square((x - P[1])/(P[1] - P[0]))

def pixel(X):
	return np.sqrt((per_pixel(R, X[0]) + per_pixel(G, X[1]) + per_pixel(B, X[2])/3))
		
#Image_normalize = 
def image_cal(path_picture):
	
	Img = imread(path_picture)
	size = int(Img.size/3)
	Img = list(Img.reshape(size, 3))
	return sum(map(pixel, Img))/size*10

#print(image_cal(path_picture1))
Degree = np.zeros((450,2))
#os.listdir('C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/picture_cut_hsv')
for file in os.listdir(path):
	sub_path1 = path + '/' + file + '/' + '1.JPEG'
	sub_path2 = path + '/' + file + '/' + '2.JPEG'
	Degree[int(file)-1, 0] = image_cal(sub_path1)
	Degree[int(file)-1, 1] = image_cal(sub_path2)

scio.savemat('C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/degree.mat',{"Degree" : Degree})







