import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil
import cv2
import json
import random


############################################################################################# This chunk of code attempts to randomly split the data between train and test images at desired ratio
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\1images"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\1annotations'

LOAD_IMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\all_speed_signs\\'
LOAD_ANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\all_speed_signs_annotations\\"

SAVE_TRAIN_IMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_images\\'
SAVE_TRAIN_ANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_annotations\\"
#LOAD_IMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_images\\'
#LOAD_ANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_annotations\\"

#look through full image list
full_list = os.listdir(LOAD_IMG)
class_array = np.zeros(20)



for ann in os.listdir(LOAD_ANNO):
    with open(os.path.join(LOAD_ANNO, ann)) as txtFile:
    #txtFile = open(os.path.join(save_path, ann), 'r')
        txtFile = txtFile.read()
        print("txtFile:", txtFile)
        space_indx = []
        spd_indx = []

        #creates a list of indices for the spaces
        for i in range(len(txtFile)):
            if (txtFile[i] == ' '):
                space_indx.append(i)

        #finds the comma from the back of the string
        comma = txtFile[txtFile.rfind(','):]


        split_file = txtFile.split()
        print("split file:", split_file)
        print(len(split_file))
        for i in range(len(split_file)):
            if i == 0:
                continue
            spd_indx.append(split_file[i][split_file[i].rfind(',')+1:])

        for i in spd_indx:
            print("i: ", type(i))


            class_array[int(i)]+= 1
        print('spd_indx: ', spd_indx)



        print("1ST:", space_indx)
        print("numbers after comma:", comma)




print("class_array:", class_array)






# #choose the ratio of train to test images
# Train_test_ratio = .9
# #moves all regular images and annotations into temp files
# amount = len(full_list)
# iterate_train = round(amount*Train_test_ratio)
# iterate_test = amount-iterate_train
# counter = 0
# for file_name in full_list:
#     if counter <iterate_train:  # save in train
#         shutil.copyfile(LOAD_IMG + file_name, SAVE_TRAIN_IMG + file_name)
#         shutil.copyfile(LOAD_ANNO + file_name[:-4] + ".txt", SAVE_TRAIN_ANNO + file_name[:-4] + ".txt")
#         counter += 1
#     else:  # save in test
#         shutil.copyfile(LOAD_IMG + file_name, SAVE_TEST_IMG + file_name)
#         shutil.copyfile(LOAD_ANNO + file_name[:-4] + ".txt", SAVE_TEST_ANNO + file_name[:-4] + ".txt")
# print("full_list: ", full_list)
# #for i in range(iterate_inv):
#
#
# string='0123 5 7 9ppi'
# space=' '
# lst= []
# for i in range(len(string)):
#     if (string[i] == s):
#         lst.append(i)
# print(lst)



