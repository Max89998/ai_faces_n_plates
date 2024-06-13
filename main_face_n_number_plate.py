import time
import cv2
capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
number_plates_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
while True:
    ret, img = capture.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))
    plates = number_plates_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20,20))

    for (x, y, w, h) in faces:
        cv2.rectangle(img=img, pt1=(x, y), pt2=(x+w, y+h), color=(255,0,0), thickness=2)
    for (x, y, w, h) in plates:
        cv2.rectangle(img=img, pt1=(x, y), pt2=(x+w, y+h), color=(0,0,255), thickness=2)

    cv2.imshow("From Camera", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()