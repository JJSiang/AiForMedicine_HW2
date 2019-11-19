import os
import cv2
import glob
import os
import os.path
import numpy as np
from matplotlib import pyplot as plt
import time
#ekg crop
#test
img = cv2.imread("./Crop_Image/EKG/" + "crop_EKG_1.jpg", 0)
start = time.time()
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
#how many number in row
row = np.size(image_b, 0)
#how many number in col 
col = np.size(image_b, 1)
#print("--------------")
# print(size)
# print(col)
# print(row)


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

# Final_Q3
count = 0
speratept_list = []
for data in finalpt_list:
    col = data.split("-")[0]
    row = data.split("-")[1]
    if not count == 0:
        tmp_col = tmp.split("-")[0]
        tmp_row = tmp.split("-")[1]
        distance = int(int(col) - int(tmp_col))
        seperatept = str(int(col) - int(round((distance/2), 0)))
        speratept_list.append(seperatept)
    elif count == 0:
        tmp = data
    count = count + 1
print("Q3: ")
print("--------------")
print(speratept_list)
print(len(speratept_list))
print("--------------")

#Q3
x_position, y_position = 117, 800
width, height = 1233, 132
path = "./EKG_001_600/"
crop_data_newpath_EKG = "./Crop_Image/EKG_Q3/"
folder = os.listdir(path)
#def read_directory_EKG():
for filename in folder:
    print(filename) 
    #img is used to store the image data 
    img = cv2.imread(path + "/" + filename)
    # cv2.imshow("test", img)
    # cv2.waitKey(0)
    img = img[y_position:y_position + height, x_position:x_position + width]
    count = 0
    heartbeatcount = 0
    for seperatept in speratept_list:
        if not count == 0:
            cuttingimage = img[0:132, pre_col:int(seperatept)]
            pre_col = int(seperatept)
        elif count == 0:
            pre_col = 0
            cuttingimage = img[0:132, pre_col:int(seperatept)]
            pre_col = int(seperatept)

        heartbeatcount = heartbeatcount + 1
        count = count + 1

        filename_final = filename + "_" + str(heartbeatcount) + ".jpg"
        cv2.imwrite(crop_data_newpath_EKG + "heart_"+ filename_final, cuttingimage)
            

print("----------- Finished ! -----------")
end = time.time()
cost = round((end - start), 2)
print("Cost Time: " + str(cost) + "s")

    # x = 0
    # y = 0
    # h = 132
    # for c in speratept_list:
    #     # Origin top left x,y
    #     x = int(c)
    #     print("x: ")
    #     print(x)
    #     print("-------")
    #     # Length and width
    #     for t in range(0, (len(speratept_list)-1)):
    #         #print(t)
    #         p = int(t+1)
    #         tmp_cur = int(speratept_list[p])
    #         data = int(speratept_list[t])
    #         distance = (tmp_cur - data)
    #         #print(distance)
    #         #di = int(speratept_list[t]) - int(c)
    #         w = distance
    #         print("w: ")
    #         print(w)
    #         print("-------")
    #         break
        # # Crop
        # crop_img = img[y:y+h, x:x+w]
        # # Save data
        # cv2.imwrite(crop_data_newpath_EKG + "crop_EKG_" + filename, crop_img)

#read_directory_EKG("EKG")
#read_directory_EKG()
