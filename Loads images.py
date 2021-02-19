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

############################################################################################# This chunk of code filters for only photos with speed limits and draws bounding boxes on them
IMGDIR = r"C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\Test_images"
JSONDIR = r'C:\Users\perfe\Documents\4th yr\FYP\mtsd_fully_annotated\sample_annotations'


for img in os.listdir(IMGDIR):  # iterate over each image and json file
            img_array = cv2.imread(os.path.join(IMGDIR, img))  # converts directory to image
            print(img)


            img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
            plt.imshow(img_array)
            plt.show()

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('done')
