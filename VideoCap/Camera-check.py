#Open camera / webcam from your pc
import cv2
from cv2 import VideoCapture
from cv2 import COLOR_BGR2GRAY

"""
cap = VideoCapture(0)
#While function it will keep using cam
while(True):
    ret,frame = cap.read() #receive each frame
    cv2.imshow('frame',frame)
    #if press q, break while true loop
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
"""


#Open video from path
path = "D:\\GIT\\VISION_Turns_Red-1\\VideoCap\\FFXIV_duel.mp4"
cap = VideoCapture(path)
#While function it will keep using cam
while(True):
    ret,frame = cap.read() #receive each frame
    #cv2.imshow('frame',frame)    #this one is normal vid with no changes

    #Grayscale changing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray mode',gray)  #this one is gray version

    #if press q, break while true loop
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

#The next part will be face detection using human model, but let me find some good reference first
#Nopparuj J.