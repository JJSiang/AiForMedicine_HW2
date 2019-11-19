import cv2
import os
import os.path
from matplotlib import pyplot as plt
import numpy as np
import time

path = "./EKG_001_600/"
crop_data_newpath_1 = "./Crop_Image/EKG_001_600_1/"
crop_data_newpath_2 = "./Crop_Image/EKG_001_600_2/"
crop_data_newpath_3 = "./Crop_Image/EKG_001_600_3/"
crop_data_newpath_4 = "./Crop_Image/EKG_001_600_4/"
crop_data_newpath_5 = "./Crop_Image/EKG_001_600_5/"
crop_data_newpath_6 = "./Crop_Image/EKG_001_600_6/"
crop_data_newpath_7 = "./Crop_Image/EKG_001_600_7/"
crop_data_newpath_8 = "./Crop_Image/EKG_001_600_8/"
crop_data_newpath_9 = "./Crop_Image/EKG_001_600_9/"
crop_data_newpath_10 = "./Crop_Image/EKG_001_600_10/"
crop_data_newpath_11 = "./Crop_Image/EKG_001_600_11/"
crop_data_newpath_12 = "./Crop_Image/EKG_001_600_12/"
# crop_data_newpath_EKG = "./Crop_Image/EKG/"

folder = os.listdir(path)
start = time.time()
#1 lead
def read_directory_1(EKG_001_600):
	for filename in folder:
		print("---------------")
		print("1_" + filename) 
		#img is used to read the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 117
		y = 365
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_1 + "crop_1_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")

#   cv2.namedWindow("image", cv2.WINDOW_NORMAL)
#   cv2.imshow("image", crop_img)
#   cv2.waitKey(0)
#   cv2.destroyAllWindows()
read_directory_1("EKG_001_600")

#2 lead
def read_directory_2(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("2_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 422
		y = 380
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_2 + "crop_2_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_2("EKG_001_600")

#3 lead
def read_directory_3(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("3_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 730
		y = 380
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_3 + "crop_3_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_3("EKG_001_600")

#4 lead
def read_directory_4(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("4_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 1035
		y = 380
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_4 + "crop_4_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_4("EKG_001_600")

#5 lead
def read_directory_5(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("5_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 115
		y = 505
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_5 + "crop_5_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_5("EKG_001_600")

#6 lead
def read_directory_6(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("6_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 423
		y = 505
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_6 + "crop_6_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_6("EKG_001_600")

#7 lead
def read_directory_7(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("7_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 728
		y = 528
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_7 + "crop_7_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_7("EKG_001_600")

#8 lead
def read_directory_8(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("8_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 1035
		y = 515
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_8 + "crop_8_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_8("EKG_001_600")

#9 lead
def read_directory_9(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("9_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 117
		y = 665
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_9 + "crop_9_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_9("EKG_001_600")

#10 lead
def read_directory_10(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("10_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 423
		y = 665
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_10 + "crop_10_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")


read_directory_10("EKG_001_600")

#11 lead
def read_directory_11(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("11_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 728
		y = 670
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_11 + "crop_11_" + filename, crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")

read_directory_11("EKG_001_600")

#12 lead
def read_directory_12(EKG_001_600):
	# this loop is for read each image in this folder,test is the folder name with images.
	for filename in folder:
		print("---------------")
		print("12_" + filename) 
		#img is used to store the image data 
		img = cv2.imread(EKG_001_600 + "/" + filename)
		# Origin top left x,y
		x = 1035
		y = 660
		# Length and width
		w = 310
		h = 132
		# Crop
		crop_img = img[y:y+h, x:x+w]
		# Save data
		cv2.imwrite(crop_data_newpath_12 + "crop_12_" + filename, crop_img)
		#t = type(crop_img)
		print("---------------")
		print(crop_img)
		print("---------------")

read_directory_12("EKG_001_600")

print("----------- Finished ! -----------")
end = time.time()
cost = round((end - start), 2)
print("Cost Time: " + str(cost) + "s")

#img to numpy
# def read_type():
# 	img = cv2.imread("./Crop_Image/EKG_001_600_1/" + "crop_1_1.jpg") # 0 raed file to gray
# 	t = type(img)
# 	#print("type: " + str(t))
# 	#print(img.shape)
# 	print(img)
	#show image
	# cv2.namedWindow("image", cv2.WINDOW_NORMAL)
	# cv2.imshow("image", img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
#read_type()