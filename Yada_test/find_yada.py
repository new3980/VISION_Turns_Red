#It is basically use this same code but instead of detecting face or etc.
#We use it to identify owner of the faces
#I'll try to show accuracy too na

import cv2
import numpy as np
import os 


faceCascade = cv2.CascadeClassifier("C:\\Users\\MBComputer\\anaconda3\\envs\\myenv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

yada = "D:\\GIT\\VISION_Turns_Red-1\\REF_path\\YADA.mp4"
taylor = "D:\\GIT\\VISION_Turns_Red-1\\REF_path\\Taylor.mp4"
#what is I use another yada video

#If found face then draw rectangle
def draw_box(img,classifier,scaleFactor,minNeighbors,color,clf):
    #Convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detect face position
    features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords = []

    for (x,y,w,h) in features:
        #Found face border at x ,then the end must be x+width of face detected in features
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        #compare new classifier with older
        id,acc = clf.predict(gray[y:y+h,x:x+w])


        #Accuracy section if not 100 then don't know
        if acc <= 100:
            cv2.putText(img,"It's Yada",(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
        else:
            cv2.putText(img,"Who's this ?",(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
        if (acc < 100): #If < 100 then show percent
            acc = " {0}%".format(round(100 - acc))
        else:
            acc = " {0}%".format(round(100 - acc))
        print(str(acc))

        coords = [x,y,w,h]
    return img,coords

#Detect face and call classifier
#1.1 = scale facter (must >1) & 5 = minNeighbors (higher = hard to detect but better quality)
def detect(img,faceCascade,img_id,clf):
    img,coords = draw_box(img,faceCascade,1.1,10,(255,0,0),clf)
    #if len(coords) == 4:
        #id = 1
        #result =  img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
    return img

img_id = 0
#cap = cv2.VideoCapture(yada)
cap = cv2.VideoCapture(taylor)
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("D:\\GIT\\VISION_Turns_Red-1\\Data_train\\YadaClass.xml")

while(True):
    ret,frame = cap.read()
    #Send each frame to identify whether face is found or not
    frame = detect(frame,faceCascade,img_id,clf)
    cv2.imshow('Where is Yada',frame)
    img_id = img_id + 1
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break

cap.release()
cv2.destroyAllWindows

#Discussion
#When I used Taylor videos instead the result is still yada so let's add accuracy consition

#Discuss 1 (false positive)
#According to 1true1false.png, the area that is not Yada face is identified "Whos's this?"

#Discuss 2 (Using Taylor Swift model)
#The results are approximately 35% maybe Taylor is a woman but for man in a video is worked
