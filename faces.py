import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
  ret,frame = video_capture.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray , 1.1, 4)

  for(x,y,w,h) in faces:
    cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)

  cv2_imshow('video',frame)

  k = cv2.waitKey(1) & 0xff
  if k==27:
    break

cap.release()
