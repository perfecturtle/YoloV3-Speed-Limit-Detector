import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import json
print(tf.__version__)
############################################################################################This code currently writes annotations in yolov3 format however it has errors classifying non-speedlimits
speedlimitlist = []
widthlist = []
heightlist = []

############################################################################################# #saves image name
# IMGDIR = r"C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\Gather_speedsigns"
# JSONDIR = r'C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\annotations'
# save_path = r"C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\Gather_annotations"
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\sample_images"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\sample_annotations'
save_path = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\sample_Gather_speedsigns"


speedlist = []
annolist = []

for img in os.listdir(IMGDIR):  # iterate over each image inside IMGDIR
    dict = img[:-4]
    speedlist.append(dict)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# selects annotation in JSONDIR that matches with images and saves them in SAVEDIR
for anno in os.listdir(JSONDIR):
    if anno[:-5] in speedlist:
        with open(os.path.join(JSONDIR, anno)) as f:
            data = json.load(f)
            widthlist.append(data['width'])
            heightlist.append(data['height'])
            for Extract in data["objects"]:
                dict = Extract['bbox']
                dict['label'] = Extract['label']
                dict['fname'] = anno[:-5]
                if 'speed-limit-' in dict['label']:
                    speedlimitlist.append(dict)
                    # calculating values for yolov3 annotations
                    xmax = dict['xmax']
                    xmin = dict['xmin']
                    ymax = dict['ymax']
                    ymin = dict['ymin']
                    height = data['height']
                    width = data['width']

                    abs_x = ((xmax + xmin) / 2) / width
                    abs_y = ((ymax + ymin) / 2) / height
                    abs_width = (xmax - xmin) / width
                    abs_height = (ymax - ymin) / height
                    label = 'invalid'

                    if 'speed-limit' in dict['label']:
                        label = dict['label']
                        label = label.split("speed-limit-", 1)[1]
                        label = label.split("--g", 1)[0]
                        print('label: ', label)


                        def week(label):
                            switcher = {
                                '5': 0,
                                '10': 1,
                                '15': 2,
                                '20': 3,
                                '25': 4,
                                '30': 5,
                                '35': 6,
                                '40': 7,
                                '45': 8,
                                '50': 9,
                                '55': 10,
                                '60': 11,
                                '65': 12,
                                '70': 13,
                                '75': 14,
                                '80': 15,
                                '90': 16,
                                '100': 17,
                                '110': 19,
                                '120': 20,

                            }
                            return switcher.get(label, "21")
                    else:
                        def week(label):
                            switcher = {

                            }
                            return switcher.get(label, "21")

                    yolov3_text = f"{week(label)} {abs_x} {abs_y} {abs_width} {abs_height}"
                    print('yolov3_text: ', yolov3_text)

                    annFile = open(os.path.join(save_path, dict['fname'] + ".txt"), 'w')
                    annFile.write(yolov3_text + '\n')
                    annFile.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

