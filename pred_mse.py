from skimage import feature as ft
from sklearn import tree
from matplotlib import pylab as plb 
from PIL import Image
from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
import os
import xlwt
import cv2
import xlsxwriter
import random
import math



path = '/Users/zhaoying/Desktop/Ann_Wang/Thesis/processed_data1/picture_cut_hdv'
ori = 2
ppc = (100,100)
cpb = (2,2)
depth = 8
len_fea = 120

cell_size = 74
parapath = '/Users/zhaoying/Desktop/Ann_Wang/Thesis/processed_data1/parameter.mat'
parameter = scio.loadmat(parapath)
parameter = parameter['Parameter']

depath = '/Users/zhaoying/Desktop/Ann_Wang/Thesis/processed_data1/degree.mat'
degree = scio.loadmat(depath)
degree = degree['Degree'] #[m,n]
#list_train = random.sample(list, 5)
list_all = os.listdir(path)  #len = 374
list_all = list(map(int, list_all))

#####################################

feature = np.zeros((450, len_fea + 4))
tag = np.zeros((450, 1))
for file in os.listdir(path):
    sub_path1 = path + '/' + file + '/3.JPEG'
    sub_path2 = path + '/' + file + '/4.JPEG'
    image1 = Image.open(sub_path1)
    #image2 = Image.open(sub_path2)
    img1 = image1.convert('L')
    #img2 = image2.convert('L')
    features = ft.hog(img1, #input image
                      orientations = ori, #number of bins
                      pixels_per_cell = ppc, #pixel per cell
                      cells_per_block = cpb, #cell per block
                      block_norm = 'L2-Hys', # block norm : str{'L1':'L1-sqrt','L2':'L2-Hys'}
                      transform_sqrt = True, # power law compression (also known as gamma correction)
                      feature_vector = True, #flatten the final vectors
                      visualise = False) #return HOG map
    feature[int(file)-1,:] = np.concatenate((features, parameter[int(file)-1,:]), axis = 0)
    tag[int(file)-1] = degree[int(file)-1,1]
#####################################

def slice_random_f(ind):
    return feature[ind-1,:]

def slice_random_t(Ind):
    return tag[Ind-1]
f = list(map(slice_random_f, list_all))
t = list(map(slice_random_t, list_all))
prediction1 = np.zeros((374, 5))
for i in range(5):
	list_train = random.sample(list_all, cell_size)
	#list_test = random.sample(list(set(list_all)-set(list_train)), cell_size)
	F_train = list(map(slice_random_f, list_train))
	T_train = list(map(slice_random_t, list_train))  
	#F_test = list(map(slice_random_f, list_test))
	#T_test = list(map(slice_random_t, list_test))
	clf = tree.DecisionTreeRegressor(max_depth = depth)
	clf = clf.fit(F_train, T_train)
	prediction1[:,i] = clf.predict(f)

prediction = prediction1.sum(axis = 1)/5
#prediction = sum(clf_0.predict(f) + clf_1.predict(f) + clf_2.predict(f) + clf_3.predict(f) + clf_4.predict(f))/5
#prediction_test = clf.predict(F_test)

def accuracy(x):
    return np.square(prediction[x]-t[x])/374

'''
def accuracy_test(X):
    if abs(prediction_test[X]-T_test[X])<=1:
        return 1
    else:
        return 0
'''


accurate = sum(map(accuracy, range(374)))
#accurate_test = sum(map(accuracy_test, range(74)))

print(accurate)
#print(accurate_test)

#prediction = clf.predict([x,y])
#probs = clf.predict_proba([x,y])






