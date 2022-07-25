import os
import shutil
import random
from sklearn.model_selection import train_test_split

dir_path = 'C:\\Users\\me\\Desktop\\GA2022\\LogoDet-3K\\Det-A'
dir_names = os.listdir(dir_path)
dir_names

imagefile_path = os.path.join(dir_path,dir_names[0])
labelfile_path = os.path.join(dir_path,dir_names[1])

"""
#LogoDet-3K split
file_names = os.listdir(imagefile_path)

randomFileList = random.sample(file_names, 100)
for file in randomFileList:
    dstsource = 'C:\\Users\\me\\Desktop\\GA2022\\LogoDet-3K'
    dstsource = os.path.join(dstsource, 'Det-A')

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
#train/val split
image_file_name = [file_name for file_name in os.listdir(imagefile_path) if os.path.isfile(os.path.join(imagefile_path, file_name))]
label_file_name = [file_name for file_name in os.listdir(labelfile_path) if os.path.isfile(os.path.join(labelfile_path, file_name))]
image_train, image_test, label_train, label_test = train_test_split(image_file_name, label_file_name, test_size=0.2, random_state=121)

for image in image_train:
    src = os.path.join(imagefile_path,image)
    dst = os.path.join(imagefile_path, "train")
    dst = os.path.join(dst,image)
    os.rename(src,dst)
for image in image_test:
    src = os.path.join(imagefile_path,image)
    dst = os.path.join(imagefile_path, "val")
    dst = os.path.join(dst,image)
    os.rename(src,dst)
for label in label_train:
    src = os.path.join(labelfile_path, label)
    dst = os.path.join(labelfile_path, "train")
    dst = os.path.join(dst,label)
    os.rename(src,dst)
for label in label_train:
    src = os.path.join(labelfile_path, label)
    dst = os.path.join(labelfile_path, "val")
    dst = os.path.join(dst,label)
    os.rename(src,dst)
#"""