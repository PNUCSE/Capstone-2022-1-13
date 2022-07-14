import os

dir_path = 'C:\\Users\\me\\Downloads\\archive (1)\\LogoDet-3K\\Electronic'#여기 경로 넣으면됨
subdir_names = os.listdir(dir_path)
subdir_names
"""
for subdir_name in subdir_names:
    src = os.path.join(dir_path, subdir_name)
    dst = os.path.join("C:\\Users\\me\\Downloads\\archive (1)\\LogoDet-3K\\labels",subdir_name)
    os.rename(src,dst)
"""
i=1
for subdir_name in subdir_names:
    file_path = os.path.join(dir_path,subdir_name)
    file_names = os.listdir(file_path)
    for file_name in file_names:
        src = os.path.join(file_path,file_name)
        if(file_name[-3:]=="jpg"):
            dst = "C:\\Users\\me\\Downloads\\archive (1)\\LogoDet-3K\\" +  "images"
            name = 'logo' + str(i) + ".jpg"
            dst = os.path.join(dst, name)
            os.rename(src, dst)
        elif(file_name[-3:]=="xml"):
            dst = "C:\\Users\\me\\Downloads\\archive (1)\\LogoDet-3K\\" +  "labels"
            name = 'logo' + str(i) + '.xml'
            dst = os.path.join(dst, name)
            os.rename(src, dst)
            i=i+1