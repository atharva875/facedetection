import cv2

cap = cv2.VideoCapture(0)

faseCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faseCascade.detectMultiScale(
        gray,
        scaleFactor =1.2,
        minNeighbors=7,
        minSize=(40,40),
    )

    for (x,w,y,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (20,255,90),2)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

            cap.release()
            cv2.destoryAllWindows()