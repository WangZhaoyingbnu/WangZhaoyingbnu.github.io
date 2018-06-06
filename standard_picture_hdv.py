#coding=utf-8
import string
import os
import time
import types
import pdb
import math
from scipy.misc import imread 
import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#RGB [46, 60, 68]

#standard_input_hdv = 'F:/HDV/153_0027_01/153_0027_01.MP4'
os.system('ffmpeg -ss 0:00:01 -i F:/HDV/153_0027_01/153_0027_01.MP4 -frames:v 1 C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/standard.JPEG')
box_hdv = [750, 450, 1200, 850] # 450*400


img = Image.open('C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/standard.JPEG')
img2 = img.crop(box_hdv)
img2.save('C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/standard_cut.JPEG')

Img = imread('C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/standard_cut.JPEG')
dataFile = 'C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/standard.mat'
scio.savemat('C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/%s.mat' % 'standard',{"Img1" : Img})

