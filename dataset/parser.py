from re import L
import xml.etree.ElementTree as ET
import os
#C:/Users/me/Downloads/archive (1)/LogoDet-3K/Clothes/2xist/
file_path = 'C:/Users/me/Desktop/GA2022/LogoDet-3K/Det-S_M_L_E/labels'
file_names = os.listdir(file_path)
file_names 

i = 143142
for name in file_names:
    name = os.path.join(file_path,name)
    if os.path.isfile(name):
        txtfile = name[:-4]+".txt"
        f = open(txtfile,"w")
        tree = ET.parse(name)

        root = tree.getroot()

        
        width,height,xmin,ymin,xmax,ymax ="","","","","",""
        for child in root.findall('size'):
            width = child.find('width').text
            height = child.find('height').text
            width = int(width)
            height = int(height)
                    
        for child in root.findall('object'):
            for gr_child in child.findall('bndbox'):
                xmin = gr_child.find('xmin').text
                ymin = gr_child.find('ymin').text
                xmax = gr_child.find('xmax').text
                ymax = gr_child.find('ymax').text

                xmin = int(xmin)
                ymin = int(ymin)
                xmax = int(xmax)
                ymax = int(ymax)
                
            strarr=""   
            for _ in range(5):
                if _ == 1:
                    strarr+=str(((xmax-xmin)/2+xmin)/width)
                    strarr+=' '
                elif _ == 2:
                    strarr+=str(((ymax-ymin)/2+ymin)/height)
                    strarr+=' '
                elif _ == 3:
                    strarr+=str((xmax-xmin)/width)
                    strarr+=' '
                elif _ == 4:
                    strarr+=str((ymax-ymin)/height)
                    strarr+='\n'
                elif _ == 0:
                    strarr+='0 '
            f.write(strarr)
        f.close()
        #print(parse_arr)
        os.remove(name)
    
#txtfile = os.path.join(file_path,file_name[:-4],.txt)
#f = open(file_path)