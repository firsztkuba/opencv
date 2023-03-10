import cv2, time

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

a=1

while True:
    check, frame = video.read()
    a += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.06, minNeighbors=4)


    for x, y, w, h in faces:
        gray = cv2.rectangle(gray, (x, y), (x+w, y+h), (0,255,0), 3)
    
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
print(a)
video.release()
cv2.destroyAllWindows