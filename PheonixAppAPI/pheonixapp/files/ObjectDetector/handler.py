#Object detector -- Pheonix Studios

import cv2
import os
import sys

mainDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

if __name__ == "__main__":
    print(mainDir)

    os.chdir(mainDir)
    sys.path.append(mainDir)

from PheonixAppAPI.pheonixapp.files import LIB

subDir = os.path.join(mainDir, "ObjectDetector")

cocoP = os.path.join(subDir, "coco.names")

configPath = os.path.join(subDir, "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
weightsPaths = os.path.join(subDir, "frozen_inference_graph.pb")

# USE FOR IMG CONFIG ----img = cv2.imread()

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

classNames= []

with open(cocoP, 'rt') as f:
    classNames = f.read().rstrip("\n").split('\n')
print(classNames)

net = cv2.dnn_DetectionModel(weightsPaths,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=0.5)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img,box,color=(0,255,0), thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10, box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    cv2.imshow("Output", img)
    cv2.waitKey(1)
