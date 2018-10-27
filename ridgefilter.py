import cv2
import os

folder = os.listdir('Pudhina')
for file in folder:
	print(file)
	image = cv2.imread('./Pudhina/'+file)
	ridge_filter = cv2.ximgproc.RidgeDetectionFilter_create()
	ridges = ridge_filter.getRidgeFilteredImage(image)
	cv2.imwrite('./Ridged/Pudhina/'+file, ridges)
