import os
import shutil
import random
from sklearn.model_selection import train_test_split
from PIL import Image
import numpy as np
import cv2


dir_path = 'C:\\Users\\me\\Desktop\\GA2022\\LogoDet-3K\\Det-normalizeS_M_L_E_T'
dir_names = os.listdir(dir_path)
dir_names

imagefile_path = os.path.join(dir_path,dir_names[0])
labelfile_path = os.path.join(dir_path,dir_names[1])


"""
#cutout image create
for image in os.listdir(imagefile_path):
    image_path = os.path.join(imagefile_path, image)
    cutout = Image.open(image_path)
    cutout = np.asarray(cutout)
    label_path = os.path.join(labelfile_path, image.replace('.jpg','.txt'))
    label = open(label_path,'r')
    label_list = label.readlines()
    for line in label_list:
        line = line.split()
        x_center = float(line[1])*np.shape(cutout)[1]
        y_center = float(line[2])*np.shape(cutout)[0]
        width = float(line[3])*np.shape(cutout)[1]
        height = float(line[4])*np.shape(cutout)[0]

        x1=random.uniform(x_center-width/2,x_center+width/4) 
        y1=random.uniform(y_center-height/2,y_center+height/4)
        x_cutout = random.uniform(width/4 ,x_center+width/2-x1)
        y_cutout = random.uniform(height/4 ,y_center+height/2-y1)
        x2=x1+x_cutout
        y2=y1+y_cutout
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        cutout = cv2.rectangle(cutout, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 0), cv2.FILLED)
    cutout = Image.fromarray(cutout)
    os.remove(image_path)
    cutout.save(image_path)
"""
"""
#LogoDet-3K split
file_names = os.listdir(imagefile_path)

randomFileList = random.sample(file_names, 3000)
for file in randomFileList:
    dstsource = 'C:\\Users\\me\\Desktop\\GA2022\\LogoDet-3K'
    dstsource = os.path.join(dstsource, 'Det-normalizeS_M_L_E_T')

    #image
    src = os.path.join(imagefile_path,file)
    dst = os.path.join(dstsource, 'images')
    shutil.copy(src, dst)

    #label
    file = file[:-4] + ".txt"
    src = os.path.join(labelfile_path,file)
    dst = os.path.join(dstsource, 'labels')
    shutil.copy(src, dst)
"""

"""
#train/val split
image_file_names = [file_name for file_name in os.listdir(imagefile_path) if os.path.isfile(os.path.join(imagefile_path, file_name))]
label_file_names= [file_name for file_name in os.listdir(labelfile_path) if os.path.isfile(os.path.join(labelfile_path, file_name))]
image_train, image_test, label_train, label_test = train_test_split(image_file_names, label_file_names, test_size=0.2, random_state=121)

for image in image_train:
    src = os.path.join(imagefile_path,image)
    dst = os.path.join(imagefile_path, "train")
    dst = os.path.join(dst,image)
    os.rename(src,dst)
for image in image_test:
    src = os.path.join(imagefile_path,image)
    dst = os.path.join(imagefile_path, "test")
    dst = os.path.join(dst,image)
    os.rename(src,dst)
for label in label_train:
    src = os.path.join(labelfile_path, label)
    dst = os.path.join(labelfile_path, "train")
    dst = os.path.join(dst,label)
    os.rename(src,dst)
for label in label_test:
    src = os.path.join(labelfile_path, label)
    dst = os.path.join(labelfile_path, "test")
    dst = os.path.join(dst,label)
    os.rename(src,dst)
image_file_names = [file_name for file_name in os.listdir(os.path.join(imagefile_path,"train")) if os.path.isfile(os.path.join(imagefile_path,"train", file_name))]
label_file_names= [file_name for file_name in os.listdir(os.path.join(labelfile_path,"train")) if os.path.isfile(os.path.join(labelfile_path,"train", file_name))]
image_train, image_val, label_train, label_val = train_test_split(image_file_names, label_file_names, test_size=0.25, random_state=121)

for image in image_val:
    src = os.path.join(imagefile_path,"train",image)
    dst = os.path.join(imagefile_path, "val")
    dst = os.path.join(dst,image)
    os.rename(src,dst)
for label in label_val:
    src = os.path.join(labelfile_path, "train", label)
    dst = os.path.join(labelfile_path, "val")
    dst = os.path.join(dst,label)
    os.rename(src,dst)
"""