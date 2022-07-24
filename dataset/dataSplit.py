import os
import shutil
import random

dir_path = 'C:\\Users\\me\Downloads\\archive (1)\\LogoDet-3K'
dir_names = os.listdir(dir_path)
dir_names

#LogoDet-3K split
imagefile_path = os.path.join(dir_path,dir_names[0])
labelfile_path = os.path.join(dir_path,dir_names[1])
file_names = os.listdir(imagefile_path)

randomFileList = random.sample(file_names, 14000)
for file in randomFileList:
    dstsource = 'C:\\Users\\me\\Desktop\\GA2022\\LogoDet-3K'
    dstsource = os.path.join(dstsource, 'Det-C')

    #image
    src = os.path.join(imagefile_path,file)
    dst = os.path.join(dstsource, 'images')
    shutil.copy(src, dst)

    #label
    file = file[:-4] + ".xml"
    src = os.path.join(labelfile_path,file)
    dst = os.path.join(dstsource, 'labels')
    shutil.copy(src, dst)

#train/val split
for dir_name in dir_names:
    file_path = os.path.join(dir_path,dir_name) + "/"
    file_names = os.listdir(file_path)
    for name in file_names:
        src = os.path.join(file_path,name)
        if os.path.isdir(src):
            continue
        number = name[4:-4]
        if int(number)%5 ==0:
            dst_path = file_path + "val/"
            
        else:
            dst_path = file_path + "train/"
        dst = os.path.join(dst_path,name)
        os.rename(src,dst)