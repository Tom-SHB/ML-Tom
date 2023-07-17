import cv2 
import face_recognition
import pickle
from datetime import datetime

cap=VideoCapture(0)

width,height = 500,500

cap.set(cv2.CAP_DROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_DROP_FRAM_HEIGHT,height)

face_cascade=cv2.CascadeClassifier('haar_cascade_files/haarcascade_frontalface_default.xml')

name = input("Input your name: ")

access_input =input("Enter room access(comma-separated):")
access_list= access_input.split(",") 

face_data = []

capture_count = 0;

while True:
	ret,frame = cap.read()
	
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	face = face_cascade.detectMultiScale(gray,scaleFactor=1,minNeighbots=5,minSize=(30,30))

	for (x,y,w,h) in face:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	 	 
		rgb_fram =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		face_encodings = face_recognition.face_encodings(rgb_frame,[(y,x+w,y+h,x)])

		for face_encoding in face_encodings:


			face_data.append({"name":name,"face":frame[y:y+h,x:x+w],"face_encodin","access":access_list})

			print(f"Capture {capture_count+1} complete!")

	cv2.imshow('Register Face',frame)
	


