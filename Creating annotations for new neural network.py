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

############################################################################################ #saves image name
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_images"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\annotations'
save_path = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_test_annotations"
YOLODIR = r"C:\git\TensorFlow-2.x-YOLOv3/OIDv4_ToolKit/OID/Dataset/train\Train/"

# IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Gather_speedsigns"
# JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\annotations'
# save_path = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Gather_annotations"
# YOLODIR = r"C:\git\TensorFlow-2.x-YOLOv3/OIDv4_ToolKit/OID/Dataset/train\Train/"

speedlist = []
annolist = []

for img in os.listdir(IMGDIR):  # iterate over each image inside IMGDIR
    dict = img[:-4]
    speedlist.append(dict)


#create empty files for each annotation
for anno in os.listdir(JSONDIR):
    with open(os.path.join(JSONDIR, anno)) as f:
        data = json.load(f)
        for Extract in data["objects"]:
            dict = Extract['bbox']
            dict['fname'] = anno[:-5]
            dict['label'] = Extract['label']
            if anno[:-5] in speedlist:
                annFile = open(os.path.join(save_path,dict['fname'] + ".txt"), 'w')
                direct = f"{YOLODIR}{dict['fname']}.jpg"
                annFile.write(direct)
                annFile.close()



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
                print('dict ', dict)
                #if 'speed-limit-' in dict['label']:
                #for i in dict['label']:
                speedlimitlist.append(dict)
                # calculating values for yolov3 annotations
                xmax = int(round(dict['xmax']))
                xmin = int(round(dict['xmin']))
                ymax = int(round(dict['ymax']))
                ymin = int(round(dict['ymin']))
                height = data['height']
                width = data['width']
                label = 'invalid'

                if 'speed-limit' in dict['label']:
                    label = dict['label']
                    label = label.split("speed-limit-", 1)[1]
                    label = label.split("--g", 1)[0]
                    #print('label: ', label)

                else:
                    def week(label):
                        switcher = {

                        }
                        return switcher.get(label, "20")


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
                        '110': 18,
                        '120': 19,

                    }
                    return switcher.get(label, "20")

                yolov3_text = f"{xmin},{ymin},{xmax},{ymax},{week(label)}"
                annFile = open(os.path.join(save_path, dict['fname'] + ".txt"), 'a')
                annFile.write(" " +yolov3_text)
                annFile.close()
                print('yolov3_text: ', yolov3_text)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

