import os
import shutil

dir_path = 'C:\\Users\\me\\Downloads\\LogoDet-3K\\Electronic'#여기 경로 넣으면됨
subdir_names = os.listdir(dir_path)
subdir_names
"""
for subdir_name in subdir_names:
    src = os.path.join(dir_path, subdir_name)
    dst = os.path.join("C:\\Users\\me\\Downloads\\archive (1)\\LogoDet-3K\\labels",subdir_name)
    os.rename(src,dst)
"""
i=13584

for subdir_name in subdir_names:
    file_path = os.path.join(dir_path,subdir_name)
    file_names = os.listdir(file_path)
    for file_name in file_names:
        src = os.path.join(file_path,file_name)
        if(file_name[-3:]=="jpg"):
            dst = os.path.join("C:\\Users\\me\\Desktop\\GA2022\\LogoDet-3K\\Det-S_M_L_E","images")
            name = 'logo' + str(i) + ".jpg"
            dst = os.path.join(dst, name)
            #os.rename(src, dst)
            shutil.copy(src,dst)
        elif(file_name[-3:]=="xml"):
            dst = os.path.join("C:\\Users\\me\\Desktop\\GA2022\\LogoDet-3K\\Det-S_M_L_E", "labels")
            name = 'logo' + str(i) + '.xml'
            dst = os.path.join(dst, name)
            os.rename(src, dst)
            i=i+1
print(i)