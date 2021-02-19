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
SAVE_TEST_IMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_images\\'
SAVE_TEST_ANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_annotations\\"

#look through full image list
full_list = os.listdir(LOAD_IMG)
#choose the ratio of train to test images
Train_test_ratio = .9

#moves all regular images and annotations into temp files
amount = len(full_list)
iterate_train = round(amount*Train_test_ratio)
iterate_test = amount-iterate_train
counter = 0
for file_name in full_list:
    if counter <iterate_train:  # save in train
        shutil.copyfile(LOAD_IMG + file_name, SAVE_TRAIN_IMG + file_name)
        shutil.copyfile(LOAD_ANNO + file_name[:-4] + ".txt", SAVE_TRAIN_ANNO + file_name[:-4] + ".txt")
        counter += 1
    else:  # save in test
        shutil.copyfile(LOAD_IMG + file_name, SAVE_TEST_IMG + file_name)
        shutil.copyfile(LOAD_ANNO + file_name[:-4] + ".txt", SAVE_TEST_ANNO + file_name[:-4] + ".txt")
print("full_list: ", full_list)
#for i in range(iterate_inv):



