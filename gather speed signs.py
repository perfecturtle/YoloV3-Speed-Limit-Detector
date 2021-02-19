import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import json
import glob
import shutil
import os
print(tf.__version__)

############################################################################################# This chunk of code filters for only photos with speed limits and places them in a new folder
IMGDIR = r"C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\images"
JSONDIR = r'C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\annotations'

speedlimitlist = []

#print('direct:', os.listdir(JSONDIR))
#bound holds the file name
for bound in os.listdir(JSONDIR):

#    print(' bound direct:', bound)
    with open(os.path.join(JSONDIR, bound)) as f:
        data = json.load(f)
#        print("data:", data)
        for Extract in data["objects"]:
            dict = Extract['bbox']
            dict['label'] = Extract['label']
            dict['fname'] = bound[:-5]
#            print("dict: ", dict)
            if 'speed' in dict['label']:
#                print('Speed limit check: ', 'speed-limit' in dict['label'])
                speedlimitlist.append(dict)



src_dir = r"C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\images"

dst_dir = r"C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\speedsigns"

for img in os.listdir(IMGDIR):  # iterate over each image and json file
#    print('os: ', os.listdir(IMGDIR))
    for match in speedlimitlist:
        if match['fname'] in img:
            if (match['xmax'] - match['xmin'] > 100):
                addjpg = match['fname'] + ".jpg"
                SPEEDDIR = os.path.join(src_dir, addjpg)
                # print('speeddir: ', SPEEDDIR)
                shutil.copy(SPEEDDIR, dst_dir)



            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('done')
