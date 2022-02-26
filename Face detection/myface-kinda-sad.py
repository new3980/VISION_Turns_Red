#Face detection
#For reference pls see document: https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
import cv2
import numpy as np
import os
#Here is the point
#I want to try using face detection whether it will work for anime character or not, so I surfed for nice HD anime girl quality
#I am not SIMP okay? This is just for testing damn it (but she is cute by the way lol)

#Step: Detect face > train > remember
#This part detect face only i guess / Using drawing function
#usual it would be haarCasCade but I am SIMP now fuck, so I changed the module
faceCascade = cv2.CascadeClassifier("C:\\Users\\MBComputer\\anaconda3\\envs\\myenv\\Lib\\site-packages\\cv2\\data\\lbpcascade_animeface.xml")

marin = "D:\\GIT\\VISION_Turns_Red-1\\Face detection\\marin-chan.mp4"


#If found face then draw rectangle
def draw_box(img,classifier,scaleFactor,minNeighbors,color,text):
    #Convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detect face position
    features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords = []
    for (x,y,w,h) in features:
        #Found face border at x ,then the end must be x+width of face detected in features
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        #put text "It's Marin!"
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
    return img

#Detect face and call classifier
#1.1 = scale facter (must >1) & 5 = minNeighbors (higher = hard to detect but better quality)
def find_marin(img,faceCascade):
    img = draw_box(img,faceCascade,1.1,3,(255,0,0),"It's Marin")
    return img


cap = cv2.VideoCapture(marin)
while(True):
    ret,frame = cap.read()
    #Send each frame to identify whether face is found or not
    frame = find_marin(frame,faceCascade)
    cv2.imshow('Is this your face?',frame)
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break

cap.release()
cv2.destroyAllWindows