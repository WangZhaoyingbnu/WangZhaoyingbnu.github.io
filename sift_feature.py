import cv2


img = cv2.imread('path')
#cv2.imshow('original',img)

s = cv2.SIFT() #call sift
#s = cv2.SURF() #call surf

keypoints = s.detect(img)
#keypoints in img