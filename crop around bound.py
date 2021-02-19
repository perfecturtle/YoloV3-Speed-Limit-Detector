import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import json
import random
print(tf.__version__)

############################################################################################# This chunk of code filters for only photos with speed limits and draws bounding boxes on them
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Test_images"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Test_annotations'
SAVEDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_images\\'

#############################################################################################Extracts all the json files with speed limit labels
speedlimitlist = []
for bound in os.listdir(JSONDIR):
    with open(os.path.join(JSONDIR, bound)) as f:
        data = json.load(f)
        for Extract in data["objects"]:
            dict = Extract['bbox']
            dict['label'] = Extract['label']
            dict['fname'] = bound[:-5]
            if 'speed' in dict['label']:
                speedlimitlist.append(dict)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Matches  all json files with speed limit labels
ImgName = []
ImgSize = 416
ImgSize = ImgSize/2
for img in os.listdir(IMGDIR):
    for match in speedlimitlist:
        if match['fname'] in img:
            img_array = cv2.imread(os.path.join(IMGDIR, img))  # converts directory to image
            ImgName.append(img)
            img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

            print('name: ', match['fname'])
            print('xmin:', match['xmin'])
            print('ymin:', match['ymin'])
            print('xmax:', match['xmax'])
            print('ymax:', match['ymax'])
            XB1 = round(match['xmin'])
            YB1 = round(match['ymin'])
            XB2 = round(match['xmax'])
            YB2 = round(match['ymax'])
            start_point = (XB1, YB1)
            end_point = (XB2, YB2)

            #centre pixel of the image
            avgx = round((match['xmin'] + match['xmax']) / 2)
            avgy = round((match['ymin'] + match['ymax'])/2)
            print('avgx', avgx)
            print('avgy', avgy)

            #randomise crop location
            print('random.randint(1, 100)', random.randint(0, 416))


            print('imgsize: ', ImgSize)
            Y1 = round((avgy - ImgSize))
            Y2 = round((avgy + ImgSize))
            X1 = round((avgx - ImgSize))
            X2 = round((avgx + ImgSize))
            print('x1', X1)
            print('x2', X2)
            print('y1', Y1)
            print('y2', Y2)
            img_array[avgy, avgx] = [255, 0, 0]
            boxed_array = cv2.rectangle(img_array, start_point, end_point, (255, 0, 0), 3)  # add rectangle to image
            crop_img = boxed_array[Y1:Y2, X1:X2]

            # Create figure and axes
            print('x2-x1: ', match['xmax'] - match['xmin'] )
            print(crop_img.shape)
            plt.imshow(crop_img)
            plt.show()
            # if(match['xmax'] - match['xmin'] > 35):
            #     plt.imshow(crop_img)
            #     plt.show()
            #this will save the image file after it's been cropped
            #cv2.imwrite(SAVEDIR + match['fname'] + '.jpg', crop_img)


            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('done')
