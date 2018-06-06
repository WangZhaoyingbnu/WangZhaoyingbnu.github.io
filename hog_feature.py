from skimage import feature as ft
from PIL import Image
import scipy.io as scio
image = Image.open('C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/picture_cut_hdv/35/3.JPEG')
img = image.convert('L')
ori = 9
ppc = (20,20)
cpb = (2,2)

features = ft.hog(img, #input image
                  orientations = ori, #number of bins
                  pixels_per_cell = ppc, #pixel per cell
                  cells_per_block = cpb, #cell per block
                  block_norm = 'L2-Hys', # block norm :
                  transform_sqrt = True, # power law compression (also known as gamma correction)
                  feature_vector = True, #flatten the final vectors
                  visualise = False) #return HOG map

print(features)
print(type(features))
print(features.shape)
parapath = 'C:/Users/lidongxue/Desktop/Ann_Wang/Thesis/processed_data1/degree.mat'
parameters = scio.loadmat(parapath)
print(parameters)