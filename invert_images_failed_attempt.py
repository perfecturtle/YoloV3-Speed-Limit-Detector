import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import random
import json
import shutil



############################################################################################# This chunk of code attempts to randomise the selection of white speed signs and invert them
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\all_speed_signs"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\1annotations'
TXTDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\all_speed_signs_annotations\\'
INVDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\invert_images\\'
ANNODIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\invert_images_annotations\\'
amount = 100
speedlimitlist = []
for name in os.listdir(JSONDIR):
    f = open(os.path.join(JSONDIR, name))
    data = json.load(f)
    for Extract in data["objects"]:
        dict = Extract['bbox']
        dict['label'] = Extract['label']
        dict['fname'] = name[:-5]
        if 'regulatory--maximum-speed-limit' in dict['label']:
            speedlimitlist.append(dict)
print("spd list: ", speedlimitlist)
print("spd list: ", len(speedlimitlist))

#random.choice(os.listdir(IMGDIR)) #change dir name to whatever
# randolist = []
# for i in range(amount):
#     img = random.sample(os.listdir(IMGDIR))
#     randolist.append(img)
#     print('img: ', img)

randolist = random.sample(os.listdir(IMGDIR), amount)



# for i in range(amount):
#     while True: #randomise images and remove repeated matches
#         img = random.choice(os.listdir(IMGDIR))
#         if img not in randolist:
#             randolist.append(img)
#             break
#         print('img: ', img)


for img_name in randolist:
    for dict in speedlimitlist:
        if dict['fname'] == img_name[:-4]:
#            print('dict: ', dict['fname'])
#            print('img_name', img_name[:-4])
            img_array = cv2.imread(os.path.join(IMGDIR, img_name))  # converts directory to image
            inverted = ~img_array
            # print('img:', img)
            cv2.imwrite(INVDIR + "inverted" + img_name, inverted)

for anno in os.listdir(TXTDIR):
    #print('anno[:-4]: ', anno[:-4])
    #shutil.copyfile(TXTDIR + anno, ANNODIR + anno)
    randomatch = anno[:-4] + ".jpg"
    if randomatch in randolist:
        #print('randomatch: ', randomatch)

        shutil.copyfile(TXTDIR + anno, ANNODIR  + anno)



print('randolist', randolist)
print('randolist size', len(randolist))





    #img_array = cv2.imread(os.path.join(IMGDIR, img))  # converts directory to image
    # print('img:', img)
    #cv2.imwrite(IMGDIR + match['fname'] + '.jpg', crop_img)