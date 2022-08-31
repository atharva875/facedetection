import cv2

cap = cv2.VideoCapture(0)

faseCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):

    ret, frame = cap.read()


