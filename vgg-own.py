import os
import random
import cv2
from imutils import paths
from loguru import logger
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
import pickle

# current working directory from which main.py is located
#cur_dir = os.getcwd()
dir = "G:\Pracamagisterska\Dataset"
# the data is located in this data_dir
#data_dir = os.path.join(cur_dir, 'Dataset')

# the output model and the graph is saved in this 'output_dir'
#output_dir = os.path.join(cur_dir, 'Output')

#logger.debug("[INFO] loading images...")

data = []
labels = []
# grab the image paths and shuffle them

imagePaths = sorted(list(paths.list_images(dir)))
random.seed(2)
random.shuffle(imagePaths)

#print(imagePaths)

IMAGE_WIDTH, IMAGE_HEIGHT = 256, 256

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
    
    # append the image to the data list
    data.append(image)
    #print(data)
    #print(image)
    # extract label from the image path and update the labels list
    label = imagePath.split(os.path.sep)[-3]
    labels.append(label)

#print(data)
print(labels)
print("koniec")

# scale the raw pixel intensities to the range [0, 1]
# data = np.array(data_loaded, dtype="float") / 255.0
# labels = np.array(labels_loaded)

# # Binarize labels
# lb = LabelBinarizer()
# labels = lb.fit_transform(labels)

# # save the encoder to output directory
# with open(os.path.join(output_dir,'labels'), 'wb') as f:
#     pickle.dump(lb, f)
    
# # Randomly split the data into test and train sets (15% test and 85% train)
# (trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.15, random_state=42)
