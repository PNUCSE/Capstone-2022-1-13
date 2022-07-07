
import xml.etree.ElementTree as ET
import os

#basic path
#filePath = "D:\졸과\\archive\LogoDet-3K\Transportationx2"
#dir 하나에 대해서만 수행
filelist = ["ac propulsion"] 
all_arr = []
for dir in filelist:
    filePath = "D:\졸과\\archive\LogoDet-3K\Transportationx2"
    filePath = filePath + '/' + dir
    print(filePath)
    i = 1
    #중간에 빈숫자채우는 방법 마땅히 안보여, 
    # 일단 이렇게시행.
    while i <=200:
        file = filePath +'/' + str(i) +'.xml'
        #print(file)    
        if os.path.isfile(file):
            print(file)
            tree = ET.parse(file)

            #ET.dump(tree)

            root = tree.getroot()

            parse_arr = []
            for child in root.findall('size'):
                width = child.find('width').text
                height = child.find('height').text
                parse_arr.append(width)
                parse_arr.append(height)
                
            for child in root.findall('object'):
                for gr_child in child.findall('bndbox'):
                    xmin = gr_child.find('xmin').text
                    ymin = gr_child.find('ymin').text
                    xmax = gr_child.find('xmax').text
                    ymax = gr_child.find('ymax').text
                    parse_arr.append(xmin)
                    parse_arr.append(ymin)
                    parse_arr.append(xmax)
                    parse_arr.append(ymax)

                
            print(parse_arr)
            all_arr.append(parse_arr)
        i+=1
for _ in all_arr:
    for line in _:
        print(line ,end=' ')
    print()
