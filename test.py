# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt 


# Read in the cascade classifiers for ROI and eyes
ROI_cascade = cv2.CascadeClassifier('D:/haar_cascade_code/Source_code/cascade/cascade.xml')



# create a function to detect ROI
def adjusted_detect_ROI(img):
	
	ROI_img = img.copy()
	
	ROI_rect = ROI_cascade.detectMultiScale(ROI_img,
											scaleFactor = 1.2,
											minNeighbors = 5)
	
	for (x, y, w, h) in ROI_rect:
		cv2.rectangle(ROI_img, (x, y),
					(x + w, y + h), (255, 255, 255), 10)\
		
	return ROI_img



# Reading in the image
img = cv2.imread('input.jpg')
img_copy = img.copy()


# Detecting the ROI
ROI = adjusted_detect_ROI(img_copy)

cv2.imshow('input image',img)
cv2.imshow('output image',ROI)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
# Saving the image
cv2.imwrite('output.jpg', ROI)
