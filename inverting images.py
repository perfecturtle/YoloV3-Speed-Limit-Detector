import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil
import cv2
import json
import random
print(tf.__version__)

############################################################################################# This chunk of code attempts to randomise the cropping and annotates the images
IMGDIR = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\1images"
JSONDIR = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\1annotations'
SAVEIMG = r'C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\invert_images\\'
SAVEANNO = r"C:\Users\perfe\Documents\4th_yr\FYP\mtsd_fully_annotated\invert_images_annotations"
YOLODIR = r"C:\git\TensorFlow-2.x-YOLOv3/OIDv4_ToolKit/OID/Dataset/train\Train/"

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
            # print('data: ', data)
            if 'regulatory--maximum-speed-limit' in dict['label']:
                speedlimitlist.append(dict)
                annFile = open(os.path.join(SAVEANNO, dict['fname'] + '_inverted' + ".txt"), 'w')
                direct = f"{YOLODIR}{dict['fname']+'_inverted'}.jpg"
                annFile.write(direct)
                annFile.close()
print('speedlimitlist: ', len(speedlimitlist))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Matches  all json files with speed limit labels


for img in os.listdir(IMGDIR):
    for match in speedlimitlist:
        # print('match:', match)
        if match['fname'] in img and ('speed' in match['label']):
            img_array = cv2.imread(os.path.join(IMGDIR, img))  # converts directory to image
            #img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)



            xmin = round(match['xmin'])
            ymin = round(match['ymin'])
            xmax = round(match['xmax'])
            ymax = round(match['ymax'])
            start_point = (xmin, ymin)
            end_point = (xmax, ymax)

            #centre pixel of the image
            avgx = round((match['xmin'] + match['xmax']) / 2)
            avgy = round((match['ymin'] + match['ymax'])/2)
            # print('avgx', avgx)
            # print('avgy', avgy)

            #randomise crop location
            wbbox = xmax - xmin
            hbbox = ymax - ymin

            ImgSize = 416
            #changes image size incase bbox is bigger than crop
            if wbbox > ImgSize or hbbox > ImgSize:
                print('change size')
                if wbbox > hbbox:
                    ImgSize = wbbox
                else:
                    ImgSize = hbbox


            while True:
                xrand = random.randint(0, ImgSize - wbbox)
                xcrop1 = xmin - xrand
                xcrop2 = xcrop1 + ImgSize

                if (xcrop1 >= 0) and (xcrop2 <= match['width']):
                    # print('name: ', match['fname'])
                    # print('xmin:', match['xmin'])
                    # print('ymin:', match['ymin'])
                    # print('xmax:', match['xmax'])
                    # print('ymax:', match['ymax'])
                    # print('wbbox ', wbbox)
                    # print('hbbox ', hbbox)
                    # print('width', match['width'])
                    # print('height', match['height'])
                    # print('xcrop1 ', xcrop1)
                    # # print('ycrop1 ', ycrop1)
                    # print('xcrop2 ', xcrop2)
                    # # print('ycrop2 ', ycrop2)
                    break



            while True:
                yrand = random.randint(0, ImgSize - hbbox)
                ycrop1 = ymin - yrand
                ycrop2 = ycrop1 + ImgSize


                if (ycrop1 >= 0) and (ycrop2 <= match['height']):
                    # print('yrand:', yrand)
                    # print('ImgSize: ', ImgSize)
                    # print('name: ', match['fname'])
                    # print('xmin:', match['xmin'])
                    # print('ymin:', match['ymin'])
                    # print('xmax:', match['xmax'])
                    # print('ymax:', match['ymax'])
                    # print('wbbox ', wbbox)
                    # print('hbbox ', hbbox)
                    # print('width', match['width'])
                    # print('height', match['height'])
                    # print('xcrop1 ', xcrop1)
                    # print('ycrop1 ', ycrop1)
                    # print('xcrop2 ', xcrop2)
                    # print('ycrop2 ', ycrop2)
                    break
                # if (xcrop1 > 0) and (xcrop2 < match['width']) and ycrop1 > 0 and ycrop2 < match['height']:
                #     break


            #these draw bounding boxes for testing
            # img_array[avgy, avgx] = [255, 0, 0]
            # img_array = cv2.rectangle(img_array, start_point, end_point, (255, 0, 0), 3)  # add rectangle to image
            crop_img = img_array[ycrop1:ycrop2, xcrop1:xcrop2]
            invert_image = ~crop_img
            #creating the annotation file######################################################################################################################
            label = 'invalid'
            if 'regulatory--maximum-speed-limit' in match['label']:
                label = match['label']
                label = label.split("speed-limit-", 1)[1]
                label = label.split("--g", 1)[0]
                # print('label: ', label)

            else:
                def week(label):
                    switcher = {

                    }
                    return switcher.get(label, "other")


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
            XB1 = xmin - xcrop1
            XB2 = xmax - xcrop1
            YB1 = ymin - ycrop1
            YB2 = ymax - ycrop1
            #annFile = open(os.path.join(save_path, match['fname'] + ".txt"), 'w')
            #             # annFile.write(direct)
            yolov3_text = f"{XB1},{YB1},{XB2},{YB2},{week(label)}"
            annFile = open(os.path.join(SAVEANNO, match['fname'] + '_inverted' + ".txt"), 'a')
            annFile.write(" " + yolov3_text)
            annFile.close()

            # print(crop_img.shape)

            #this will save the image file after it's been cropped
            cv2.imwrite(SAVEIMG + match['fname'] + '_inverted' + '.jpg', invert_image)
            #show all pixels
            #plt.imshow(crop_img)
            #plt.show()

            # #show pixels that meet this criteria
            # if(match['xmax'] - match['xmin'] > 35):
            #     plt.imshow(crop_img)
            #     plt.show()

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


print('done')