import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import json
print(tf.__version__)

############################################################################################# This chunk of code filters for only photos with speed limits and draws bounding boxes on them
IMGDIR = r"C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\Test_images"
JSONDIR = r'C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\Test_annotations'
training_data = []

# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80 ,90, 100, 110, 120]
#spd_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 100, 110, 120]

#############################################################################################Extracts all the json files with speed limit labels
speedlimitlist = []
widthlist = []
heightlist = []

for bound in os.listdir(JSONDIR):
    with open(os.path.join(JSONDIR, bound)) as f:
        data = json.load(f)
        widthlist.append(data['width'])
        heightlist.append(data['height'])
        for Extract in data["objects"]:
            dict = Extract['bbox']
            dict['label'] = Extract['label']
            dict['fname'] = bound[:-5]
            if 'speed' in dict['label']:
                speedlimitlist.append(dict)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
            start_point =(round(match['xmin']), round(match['ymin']))
            end_point = (round(match['xmax']), round(match['ymax']))

            #crop_img = boxed_array[Y1:Y2, X1:X2]
            #print('avgmin: ', avgy - ImgSize)
            #print('avgmax: ', avgy + ImgSize)
            #crop_img = boxed_array[round(match['ymin']):round(match['ymax']), round(match['xmin']): round(match['xmax'])]

            new_array = cv2.resize(img_array, (ImgSize, ImgSize))
            #############################################################################################This creates a bounding box around the image
            # Create figure and axes
            print('x2-x1: ', match['xmax'] - match['xmin'] )
            print('img shape: ', new_array.shape)
            #print('img shape: ', crop_img.shape)
            if(match['xmax'] - match['xmin'] > 100):
                #training_data.append()
                plt.imshow(new_array)
                plt.show()


            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('done')






