
import cv2
import numpy as np
import pafy
import os
import pandas as pd

IMAGE_FORMAT = ".jpeg"
SAVE_IMAGE_ROOT = "./hospital_image"

def show_YOLO_detection():
    url = "https://www.youtube.com/watch?v=2Vpe-3dFm4w"
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")

    # 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
    vidcap = cv2.VideoCapture()
    vidcap.open(best.url)

    # YOLO 가중치 파일과 CFG 파일 로드
    YOLO_net = cv2.dnn.readNet("yolov2-tiny.weights","yolov2-tiny.cfg")

    # YOLO NETWORK 재구성
    classes = []
    with open("yolo.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = YOLO_net.getLayerNames()
    #output_layers = [ layer_names[i[0] - 1] for i in YOLO_net.getUnconnectedOutLayers() ]
    output_layers = [ layer_names[YOLO_net.getUnconnectedOutLayers()[0] - 1]]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    count,detect = 0,0
    labelName = "train.csv"

    while(vidcap.isOpened()):
        # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
        # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
        # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
        
        labelList = []

        ret, image = vidcap.read()
        #print(type(image))
        if image is None:
            break
        h, w, c = image.shape
    
        #20 프레임 마다 담기
        if(int(vidcap.get(1)) % 20 == 0):
            print('Saved frame number : ' + str(int(vidcap.get(1))))
            cv2.imwrite("mkdata/images/frame%d.jpg" % count, image)
            #cv2.imshow("YOLOv3", image)

            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break
            print('Saved frame%d.jpg' % count)
            count += 1
            #train set 만들기 위한 형식.
            fileName = f"{str(h)}/{count:07d}{IMAGE_FORMAT}"

			# CSV화를 위한 단계
            fullFileName = os.path.join(SAVE_IMAGE_ROOT,fileName)
            if not os.path.isfile(fullFileName):
                cv2.imwrite(fullFileName,image)

            oneLabel = [fullFileName]
            oneLabel.append(h)
            oneLabel.append(video)
            labelList.append(oneLabel)
        # Multiprocessing을 위한 처리, 모드는 덮어쓰기고 Header는 파일이 존재하지 않을시만 생성
        pd.DataFrame(labelList,columns=["file_name","label","video_name"]).to_csv(labelName, mode="a",header=not os.path.isfile(labelName),index=False)

        # YOLO 입력
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        YOLO_net.setInput(blob)
        outs = YOLO_net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:

            for detection in out:

                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * w)
                    center_y = int(detection[1] * h)
                    dw = int(detection[2] * w)
                    dh = int(detection[3] * h)
                    
                    # Rectangle coordinate
                    x = int(center_x - dw / 2)
                    y = int(center_y - dh / 2)
                    boxes.append([x, y, dw, dh])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
                    #detect 된 것만 저장.
                    cv2.imwrite("mkdata/images/detect%d.jpg" % detect, image)
                    print("detect ",detect)
                    detect+=1

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)


        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                score = confidences[i]
                color = colors[i]

                # 경계상자와 클래스 정보 이미지에 입력
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(image, label, (x, y - 20), cv2.FONT_ITALIC, 0.5, color, 1)

        #cv2.imshow("YOLOv3", image)

        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break

    vidcap.release()
    #cv2.destroyAllWindowss()


if __name__ == '__main__':
    show_YOLO_detection()

