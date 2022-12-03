import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_FPS , 60)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

while True:
    _ , frame = cap.read()

    noBG = segmentor.removeBG(frame , (255 , 0 , 255) , threshold=0.5)
    fpsReader.update(noBG)
    cv2.imshow("Video" , frame)
    cv2.imshow("noBG" , noBG)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break