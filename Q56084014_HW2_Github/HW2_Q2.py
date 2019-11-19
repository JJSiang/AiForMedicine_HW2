import os
import cv2
import glob
import os
import os.path
import numpy as np
from matplotlib import pyplot as plt
import time
start = time.time()
#ekg crop
path = "./EKG_001_600/"
crop_data_newpath_EKG = "./Crop_Image/EKG/"
folder = os.listdir(path)
def read_directory_EKG(EKG_001_600):
    # this loop is for read each image in this folder,test is the folder name with images.
    for filename in folder:
        print(filename) 
        #img is used to store the image data 
        img = cv2.imread(EKG_001_600 + "/" + filename)
        # Origin top left x,y
        x = 117
        y = 800
        # Length and width
        w = 1233
        h = 132
        # Crop
        crop_img = img[y:y+h, x:x+w]
        # Save data
        cv2.imwrite(crop_data_newpath_EKG + "crop_EKG_" + filename, crop_img)
        
        img = cv2.imread("./Crop_Image/EKG/" + "crop_EKG_" + filename, 0)

        #for gray
        #image_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # cv2.namedWindow("Gray image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Gray image", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        image_n = np.array(img)
        # print("--------------")
        # print(image_n)
        # print("--------------")

        #for binary:
        ret,image_b = cv2.threshold(img ,138, 255, cv2.THRESH_BINARY)
        # cv2.namedWindow("Binary image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Binary image",image_b)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        size = np.size(image_b)
        row = np.size(image_b, 0) #how many number in row 直
        col = np.size(image_b, 1) #how many number in col 橫
        #print("--------------")
        # print(size)
        # print(col)
        # print(row)
        #print(image_b)
        # print("--------------")
        # print(image_b)
        # print("--------------")

        #create 0 array
        x = np.zeros((1233,), dtype = np.int)
        '''
        print("--------------")
        print(x)
        print("--------------")
        '''
        num_list = []
        for c in range(1233):
            for r in range(132):
                i = image_b[r][c]
                if i == 0:
                    tmp = str(c) + "-" + str(r)
                    num_list.append(tmp)
                    break
        #print(num_list)

        count = 0
        peak_list = []
        for data in num_list:
            col = data.split("-")[0]
            row = data.split("-")[1]
            if not count == 0:
                tmp_col = tmp.split("-")[0]
                tmp_row = tmp.split("-")[1]
                if row < tmp_row:
                    peak_list.append(data)
                tmp = data
            elif count == 0:
                tmp = data
            count = count + 1
        #print(peak_list)

        sumtotal = 0
        for pt in peak_list:
            num = pt.split("-")[1]
            sumtotal = sumtotal + int(num)

        average = round(sumtotal / len(peak_list), 2)
        filter_list = []
        for pt in peak_list:
            value = int(pt.split("-")[1])
            if value < average:
                filter_list.append(pt)
        # print(filter_list)

        count = 0
        finalpt_list = []
        for data in filter_list:
            col = data.split("-")[0]
            row = data.split("-")[1]
            if not count == 0:
                tmp_col = tmp.split("-")[0]
                tmp_row = tmp.split("-")[1]
                if row > tmp_row:
                    finalpt_list.append(tmp)
                tmp = data
            elif count == 0:
                tmp = data
            count = count + 1
        print("Q2: ")
        print("--------------")
        print(finalpt_list)

        # Final_Q2
        hb = len(finalpt_list)

        print(hb)
        print("--------------")

read_directory_EKG("EKG_001_600")

print("----------- Finished ! -----------")
end = time.time()
cost = round((end - start), 2)
print("Cost Time: " + str(cost) + "s")