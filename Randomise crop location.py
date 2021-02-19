import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import json
import random
print(tf.__version__)

############################################################################################# This chunk of code attempts to randomise the cropping
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Test_images"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Test_annotations'
SAVEDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\Temp_images\\'

#############################################################################################Extracts all the json files with speed limit labels
speedlimitlist = []
for bound in os.listdir(JSONDIR):
    # with open(os.path.join(JSONDIR, bound)) as f:
        f =  open(os.path.join(JSONDIR, bound))
        data = json.load(f)
        for Extract in data["objects"]:
            dict = Extract['bbox']
            dict['label'] = Extract['label']
            dict['fname'] = bound[:-5]
            dict['width'] = data['width']
            dict['height'] = data['height']
            print('data: ', data)
            if 'speed' in dict['label']:
                speedlimitlist.append(dict)
            print('dict: ', dict)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Matches  all json files with speed limit labels

ImgSize = 416
for img in os.listdir(IMGDIR):
    for match in speedlimitlist:
        print('match:', match)
        if match['fname'] in img and ('speed' in match['label']):
            img_array = cv2.imread(os.path.join(IMGDIR, img))  # converts directory to image
            #img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

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
            wbbox = XB2 - XB1
            hbbox = YB2 - YB1
            print('wbbox ', wbbox)
            print('hbbox ', hbbox)
            print('width', match['width'])
            print('height', match['height'])

            #changes image size incase bbox is bigger than crop
            if wbbox > ImgSize or hbbox > ImgSize:
                if wbbox > hbbox:
                    ImgSize = wbbox
                else:
                    ImgSize = hbbox


            while True:
                xrand = random.randint(0, ImgSize - wbbox)
                yrand = random.randint(0, ImgSize - hbbox)
                xcrop1 = XB1 - xrand
                ycrop1 = YB1 - yrand
                xcrop2 = xcrop1 + ImgSize
                ycrop2 = ycrop1 + ImgSize
                if (xcrop1 > 0) and (xcrop2 < match['width']) and ycrop1 > 0 and ycrop2 < match['height']:
                    break
            print('xcrop1 ', xcrop1)
            print('ycrop1 ', ycrop1)
            print('xcrop2 ', xcrop2)
            print('ycrop2 ', ycrop2)

                    #lo
            img_array[avgy, avgx] = [255, 0, 0]
            boxed_array = cv2.rectangle(img_array, start_point, end_point, (255, 0, 0), 3)  # add rectangle to image
            crop_img = boxed_array[ycrop1:ycrop2, xcrop1:xcrop2]

            # Create figure and axes
            print('x2-x1: ', match['xmax'] - match['xmin'] )
            print(crop_img.shape)
            # #show all pixels
            # plt.imshow(crop_img)
            # plt.show()

            # #show pixels that meet this criteria
            # if(match['xmax'] - match['xmin'] > 35):
            #     plt.imshow(crop_img)
            #     plt.show()
            #this will save the image file after it's been cropped
            cv2.imwrite(SAVEDIR + match['fname'] + '.jpg', crop_img)


            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('done')