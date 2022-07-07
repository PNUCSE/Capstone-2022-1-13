import os

dir_path = 'C:/Users/me/Desktop/archive (1)/LogoDet-3K/'
dir_names = os.listdir(dir_path)
dir_names

for dir_name in dir_names:
    file_path = os.path.join(dir_path,dir_name) + "/"
    file_names = os.listdir(file_path)
    for name in file_names:
        src = src = os.path.join(file_path,name)
        if os.path.isdir(src):
            continue
        number = name[4:-4]
        if int(number)%5 ==0:
            dst_path = file_path + "val/"
            
        else:
            dst_path = file_path + "train/"
        dst = os.path.join(dst_path,name)
        os.rename(src,dst)