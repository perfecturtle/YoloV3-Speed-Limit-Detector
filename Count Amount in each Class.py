import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil
import cv2
import json
import random


############################################################################################# This chunk of code attempts to  split the data equally in classes between train and test images at desired ratio
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\1images"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\1annotations'

LOAD_IMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\all_speed_signs\\'
LOAD_ANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\all_speed_signs_annotations\\"

SAVE_TRAIN_IMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_images\\'
SAVE_TRAIN_ANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_annotations\\"
SAVE_TEST_IMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_images\\'
SAVE_TEST_ANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_annotations\\"

#look through full image list
full_list = os.listdir(LOAD_IMG)
class_array = np.zeros(20)


for ann in os.listdir(LOAD_ANNO):
    with open(os.path.join(LOAD_ANNO, ann)) as txtFile:
        txtFile = txtFile.read()
        print("txtFile:", txtFile)
#        space_indx = []
    spd_indx = []

    #creates a list of indices for the spaces
#        for i in range(len(txtFile)):
#            if (txtFile[i] == ' '):
#                space_indx.append(i)

    #finds the comma from the back of the string
    comma = txtFile[txtFile.rfind(','):]
    split_file = txtFile.split()
    print("split file:", split_file)
    print(len(split_file))

    for i in range(len(split_file)):
        if i == 0:
            continue
        #this grabs the numerical values in the text file "172,190,234,250,3" in this case the 3
        spd_indx.append(split_file[i][split_file[i].rfind(',')+1:])

    for i in spd_indx:
        print("i: ", type(i))
        class_array[int(i)]+= 1
    print('spd_indx: ', spd_indx)



#choose the ratio of train to test images
Train_test_ratio = .9

#moves all regular images and annotations into temp files
amount = len(full_list)
iterate_train = round(amount*Train_test_ratio)
iterate_test = amount-iterate_train
counter = 0

class_array_counter = np.zeros(21)

for file_name in os.listdir(LOAD_ANNO):
    with open(os.path.join(LOAD_ANNO, file_name)) as txtFile:
        txtFile = txtFile.read()
    print("txtFile:", txtFile)
    spd_indx = []


    #finds the comma from the back of the string
    comma = txtFile[txtFile.rfind(','):]
    split_file = txtFile.split()

    for i in range(len(split_file)):
        if i == 0:
            continue
        #this grabs the numerical values in the text file "172,190,234,250,3" in this case the 3
        spd_indx = int(split_file[i][split_file[i].rfind(',')+1:])
    print("spd_indx: ", spd_indx)
    print("array_counter: ", class_array_counter[spd_indx])
    print("array: ", class_array[spd_indx])
        # save in test
    if class_array_counter[spd_indx] < class_array[spd_indx]*(1-Train_test_ratio):  # save in train
        class_array_counter[spd_indx] += 1
        shutil.copyfile(LOAD_IMG + file_name[:-4] + ".jpg", SAVE_TEST_IMG + file_name[:-4] + ".jpg")
        shutil.copyfile(LOAD_ANNO + file_name, SAVE_TEST_ANNO + file_name)

    else:  # save in train
        shutil.copyfile(LOAD_IMG + file_name[:-4] + ".jpg", SAVE_TRAIN_IMG + file_name[:-4] + ".jpg")
        shutil.copyfile(LOAD_ANNO + file_name , SAVE_TRAIN_ANNO + file_name)


#print("1ST:", space_indx)
print("numbers after comma:", comma)
print("class_array:", class_array)








