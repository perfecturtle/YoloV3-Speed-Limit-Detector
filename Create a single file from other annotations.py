import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import json
print(tf.__version__)
############################################################################################This code currently writes annotations in a new format because the this neural network requires different annotation set up
speedlimitlist = []
widthlist = []
heightlist = []

########################################################################################### #saves image name
set_path = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated"
IMGDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_images'
ANNDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_annotations"
speedlist = []
annolist = []
#create empty file annotations list
annFile = open(os.path.join(set_path, "Dataset_train" + ".txt"), 'w')
annFile = open(os.path.join(set_path, "Dataset_train" + ".txt"), 'a')


#
# set_path = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated"
# IMGDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_images'
# ANNDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_annotations"
# speedlist = []
# annolist = []
# #create empty file annotations list
# annFile = open(os.path.join(set_path, "Dataset_test" + ".txt"), 'w')
# annFile = open(os.path.join(set_path, "Dataset_test" + ".txt"), 'a')


for ann in os.listdir(ANNDIR):
    if ".txt" in ann:
        with open(os.path.join(ANNDIR, ann)) as txtFile:
        #txtFile = open(os.path.join(save_path, ann), 'r')
            txtFile = txtFile.read()
            print("txtFile:", txtFile)
            print("ann:", ann)
            annFile.write(txtFile + "\n")

annFile.close()
